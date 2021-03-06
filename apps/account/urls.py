from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# app_name = 'account'

urlpatterns = [
    # previous login view
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    # change password urls
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # reset password urls
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.register, name='register'),
    # активация аккаунта
    path('activate/<str:email>/', views.activate_account, name='activate_account'),
    # путь для старта демо-доступа
    path('make_session_not_permanent/', views.make_session_not_permanent, name='make_session_not_permanent'),
    path('', views.profile, name='profile'),
]
