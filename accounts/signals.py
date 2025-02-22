from allauth.socialaccount.models import SocialAccount
from allauth.account.signals import user_logged_in
from django.dispatch import receiver
from .models import CustomUser  # Import model của bạn

@receiver(user_logged_in)
def set_role_on_google_login(sender, request, user, **kwargs):
    print("có sing")
    if not isinstance(user, CustomUser):
        return  

    if SocialAccount.objects.filter(user=user, provider='google').exists():
        print("oke")
        if not user.role or user.role == CustomUser.ROLE_PLAYER:  
            print("thêm")
            user.role = CustomUser.ROLE_PLAYER  
            user.request_status = CustomUser.STATUS_PENDING  
            user.requested_role = CustomUser.ROLE_PLAYER
            user.is_verified = True  
            user.save()