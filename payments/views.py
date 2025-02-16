import paypalrestsdk
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect

paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE,  
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET,
})

def create_payment(request):
    amount = request.GET.get("amount", "10")  # Lấy số tiền từ request
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {"payment_method": "paypal"},
        "redirect_urls": {
            "return_url": "http://localhost:8000/paypal-success/",
            "cancel_url": "http://localhost:8000/paypal-cancel/"
        },
        "transactions": [{
            "amount": {"total": amount, "currency": "USD"},
            "description": "Nạp tiền vào ví điện tử"
        }]
    })

    if payment.create():
        for link in payment.links:
            if link.rel == "approval_url":
                return redirect(link.href)  # Chuyển người dùng đến PayPal
    return JsonResponse({"error": "Không thể tạo thanh toán"}, status=400)
def paypal_success(request):
    payment_id = request.GET.get("paymentId")
    payer_id = request.GET.get("PayerID")

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        # Cập nhật số dư ví của người dùng ở đây
        return JsonResponse({"message": "Nạp tiền thành công!"})
    return JsonResponse({"error": "Thanh toán thất bại!"}, status=400)

def paypal_cancel(request):
    return JsonResponse({"error": "Bạn đã hủy thanh toán!"}, status=400)
