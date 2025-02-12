from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm, LoginForm, RoleUpgradeRequestForm, FormInfor
from django.http import HttpResponseForbidden, HttpResponse 
from .models import CustomUser
from games.models import Game
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



def home(request):
    gamehay = Game.objects.all()
    return render(request, 'home.html', {'games': gamehay,'user': request.user})

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



def change_pass(request):
    return render(request, 'password_change_for.html')

def information(request):
    user = request.user
    if request.method == "POST":
        form = FormInfor(request.POST,  instance=user)
        if form.is_valid():
            form.save()
    else:
        form = FormInfor( instance=user)
    return render(request, "information.html", {'form': form})

def reset_password(request):
    return render(request, 'password_reset.html')

def login_register(request):
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

    return render(request, 'login_register.html', {
        'login_form': login_form,
        'register_form': register_form,
    })