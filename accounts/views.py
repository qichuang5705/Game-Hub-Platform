from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm, LoginForm, RoleUpgradeRequestForm, FormInfor
from django.http import HttpResponseForbidden, HttpResponse 
from .models import CustomUser
from games.models import Game
from django.core.mail import send_mail
import random, os
from django.conf import settings
def redirect_base_on_role(user):
    if user.is_superuser:
    # Đăng nhập người dùng và chuyển hướng đến admin
        user.role = 'admin'
        user.save()
        return redirect('/admin/')  # Trang admin của Django
    else:
        return redirect('home')  # Trang mặc định nếu không phải các vai trò trên  # Nếu không khớp vai trò nào, mặc định là home

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {user.username}")
                return redirect_base_on_role(user)
            else:
                form.add_error(None, 'Invalid username or password')  # Thêm thông báo lỗi nếu thông tin sai
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Đăng nhập người dùng sau khi đăng ký
            messages.success(request, f"Welcome, {user.username}")
            return redirect_base_on_role(user)
        else:
            messages.error(request, "Invalid information")
    else:
        form = RegistrationForm()
    return render(request, 'home.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

def upgrade_role(request):
    if not request.user.is_authenticated:
        # Nếu người dùng chưa đăng nhập, trả về lỗi 403
        return HttpResponseForbidden("You must be logged in to request a role upgrade.")
    
    user = request.user  # Lấy người dùng đã đăng nhập
    if user.role != 'player':
        # Nếu người dùng không phải là player, không thể yêu cầu nâng cấp
        return HttpResponseForbidden("You do not have permission to upgrade your role.")

    # Nếu người dùng là player và đã đăng nhập, xử lý yêu cầu nâng cấp
    if request.method == 'POST':
        form = RoleUpgradeRequestForm(request.POST)
        if form.is_valid():
            # Lưu yêu cầu nâng cấp vai trò
            user.requested_role = form.cleaned_data['requested_role']
            user.request_status = CustomUser.STATUS_PENDING
            user.save()
            messages.success(request, "Your role upgrade request has been submitted.")
            return redirect('home')  # Redirect đến trang home hoặc trang phù hợp
    else:
        form = RoleUpgradeRequestForm()

    return render(request, 'role_upgrade.html', {'form': form})



@login_required
def information(request):
    user = request.user
    if request.method == "POST":
        form = FormInfor(request.POST, request.FILES, instance=user)
        name = os.path.basename(user.avatar.name)
        parent = os.path.dirname(user.avatar.path)
        if form.is_valid():
            if 'avatar' in request.FILES and name != 'gojo.jpg':
                path = os.path.join(parent, name)
                if os.path.exists(path):
                    os.remove(path)
            form.save()
    return redirect('home')

def reset_password(request):
    return render(request, 'password_reset.html')


def home(request):
    game = Game.objects.all()
    login_form=LoginForm()
    register_form=RegistrationForm()
    if request.method == "POST":
        if 'login' in request.POST:
            login_form = LoginForm(data = request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user =authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(request, f"Welcome, {user.username}")
                    return redirect_base_on_role(user)
                else:
                    messages.error(request, "Invalid username or password")
        elif 'register' in request.POST:
            register_form = RegistrationForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                login(request, user)
                messages.success(request, f"Welcome, {user.username}")
                return redirect_base_on_role(user)
            else:
                messages.error(request, "Invalid information")
    else:
        login_form=LoginForm()
        register_form=RegistrationForm()

    return render(request, 'home.html', {
        'login_form': login_form,
        'register_form': register_form,
        'games': game
    })

def send_otp_email(email, otp):
    subject = "Your Password Reset OTP"
    message = f"Your OTP code for password reset is: {otp}"
    sender_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    
    send_mail(subject, message, sender_email, recipient_list)

def forgot_password_request(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            user = CustomUser.objects.get(email=email)
            otp = random.randint(100000, 999999) # tao otp 6 chu so
            otp = random.randint(100000, 999999)  # Tạo OTP 6 số
            request.session["reset_email"] = email
            request.session["reset_otp"] = str(otp)  # Lưu OTP vào session
            send_otp_email(email, otp)  # Gửi OTP qua email
            messages.success(request, "OTP has been sent to your email.")
            return redirect("verify_otp")  # Chuyển hướng sang trang nhập OTP

        except CustomUser.DoesNotExist:
             messages.error(request, "Email is not registered.")
    return render(request, "forgot_password.html")

def verify_otp(request):
    if request.method == "POST":
        entered_otp = request.POST.get("otp")
        stored_otp = request.session.get("reset_otp")

        if entered_otp == stored_otp:
            request.session["otp_verified"] = True  # Đánh dấu OTP hợp lệ
            messages.success(request, "OTP verified successfully. You can reset your password.")
            return redirect("reset_password_form")  # Chuyển sang trang đặt mật khẩu mới
        else:
            messages.error(request, "Invalid OTP. Please try again.")

    return render(request, "verify_otp.html")

def reset_password_form(request):
    if not request.session.get("otp_verified"):
        return redirect("forgot_password")  # Nếu chưa xác minh OTP, quay lại bước đầu

    if request.method == "POST":
        new_password = request.POST.get("password1")
        confirm_password = request.POST.get("password2")

        if new_password == confirm_password:
            email = request.session.get("reset_email")
            user = CustomUser.objects.get(email=email)
            user.set_password(new_password)
            user.save()

            # Xóa session sau khi đặt lại mật khẩu thành công
            del request.session["reset_email"]
            del request.session["reset_otp"]
            del request.session["otp_verified"]

            messages.success(request, "Your password has been reset successfully.")
            return redirect("login_register")  # Quay về trang đăng nhập
        else:
            messages.error(request, "Passwords do not match.")

    return render(request, "reset_password.html")

def error(request):
    return render(request, 'error.html')