from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView
from .views import profile_view
from .views import SignUpView, PasswordChangeView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('profile/', profile_view.as_view(), name='profile'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change')
]
