from django.urls import path
from authen import views

urlpatterns=[
    path('login_',views.login_,name='login_'),
    path('register/',views.register,name='register'),
    path('logout_/',views.logout_,name='logout_'),
    path('profile_/',views.profile_,name='profile_'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('update_password/',views.update_password,name='update_password'),



]