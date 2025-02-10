from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm, LoginForm, RoleUpgradeRequestForm
from django.http import HttpResponseForbidden, HttpResponse 
from .models import CustomUser

def redirect_base_on_role(user):
    if user.is_superuser:
    # Đăng nhập người dùng và chuyển hướng đến admin
        user.role = 'admin'
        user.save()
        return redirect('/admin/')  # Trang admin của Django
    # Kiểm tra vai trò và chuyển hướng đến trang phù hợp
    elif user.role == 'developer':
        return redirect('home')  # Trang dành cho developer
    elif user.role == 'designer':
        return redirect('home')  # Trang dành cho designer
    elif user.role == 'player':
        return redirect('home')  # Trang dành cho player
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


def huy(request):
    return HttpResponse("Hello HUy")

def home(request):
    return render(request, 'home.html')

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
    return render(request, 'register.html', {'form': form})

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
