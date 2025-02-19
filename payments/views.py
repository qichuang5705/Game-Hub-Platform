from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Wallet, TransactionHistory  # Import TransactionHistory
from django.contrib import messages
from django.core.paginator import Paginator
import paypalrestsdk
from payments.models import Wallet
from decimal import Decimal
@login_required
def create_payment(request):
    amount = request.GET.get("amount")
    if not amount or float(amount) <= 0:
        return JsonResponse({"error": "Số tiền không hợp lệ"}, status=400)

    wallet, _ = Wallet.objects.get_or_create(user=request.user)  # Tránh lỗi khi user chưa có ví
    return_url = request.build_absolute_uri(reverse("execute_payment"))
    cancel_url = request.build_absolute_uri(reverse("payment_failed"))
    
    payment_url = wallet.create_paypal_payment(amount, return_url, cancel_url)
    
    if payment_url:
        return JsonResponse({"payment_url": payment_url})
    return JsonResponse({"error": "Không thể tạo thanh toán PayPal. Vui lòng thử lại sau."}, status=500)

@login_required
def execute_payment(request):
    payment_id = request.GET.get("paymentId")
    payer_id = request.GET.get("PayerID")
    
    if not payment_id or not payer_id:
        messages.error(request, "Thiếu thông tin thanh toán")
        return redirect('home')

    wallet = Wallet.objects.get(user=request.user)
    if wallet.process_paypal_payment(payment_id, payer_id):
        messages.success(request, "Nạp tiền thành công!")
    else:
        messages.error(request, "Nạp tiền thất bại.")

    return redirect('home')

@login_required
def payment_failed(request):
    return JsonResponse({"error": "Giao dịch bị hủy"}, status=400)

@login_required
def deposit_page(request):
    return render(request, "deposit.html")

@login_required
def transaction_history(request):
    # Kiểm tra xem có phải lọc đúng theo người dùng hiện tại hay không
    transactions = TransactionHistory.objects.filter(user=request.user).order_by("-timestamp")
    
    # Kiểm tra xem có dữ liệu hay không
    print(transactions)  # In ra danh sách giao dịch trong console

    paginator = Paginator(transactions, 5)  # Số giao dịch hiển thị mỗi trang
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, "transaction_history.html", {"page_obj": page_obj})

@login_required
def withdraw_to_paypal(request):
    if request.method == "POST":
        amount = Decimal(request.POST.get('amount'))  # Số tiền người dùng muốn rút
        paypal_email = request.POST.get('paypal_email')  # Email PayPal của người dùng

        wallet = Wallet.objects.get(user=request.user)
        # Kiểm tra số dư trong ví điện tử của người dùng
        if wallet.balance < amount:
            messages.error(request, "Số dư không đủ để thực hiện giao dịch!")
            return redirect("withdraw_to_paypal")
        
        #Tạo một Paypal paymen
        payout = paypalrestsdk.Payout({
            "sender_batch_header": {
                "email_subject": "You have a payout!",
                "email_message": "You have received a payout! Thank you for using our service.",
            },
            "items": [
                {
                    "recipient_type": "EMAIL",
                    "amount": {
                        "value": str(amount),
                        "currency": "USD"
                    },
                    "receiver": paypal_email,
                    "note": "Thank you for using our service!",
                    "sender_item_id": "item_1"
                }
            ]
        })
         # Gửi yêu cầu rút tiền
        if payout.create():
            # Cập nhật số dư ví sau khi rút tiền
            wallet.balance -= amount
            wallet.save()

            # Ghi lại lịch sử giao dịch
            TransactionHistory.objects.create(
                user=request.user,
                transaction_type="withdraw",
                amount=amount,
                status="success",
                balance_after_transaction=wallet.balance,
            )

            messages.success(request, "Rút tiền thành công!")
            return redirect("home")  # Điều hướng đến trang ví sau khi thành công

        else:
            messages.error(request, "Rút tiền thất bại. Vui lòng thử lại sau!")
            return redirect("withdraw_to_paypal")
        
    return render(request, "withdraw_to_paypal.html")