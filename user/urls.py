from django.urls import path, include
from .views import profile_view, edit_profile_view, profile_setting_view,delete_profile

urlpatterns = [
    path('user_profile', profile_view, name='user-profile'),
    path('edit_user_profile', edit_profile_view, name='edit-profile'),
    path('onboarding', edit_profile_view, name='profile_onboarding'),
    path('profile_setting', profile_setting_view, name='profile_setting'),
    path('delete_profile',delete_profile,name="profile-delete")

]
