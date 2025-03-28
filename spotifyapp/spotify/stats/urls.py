from django.urls import path
from django.contrib.auth.views import LoginView
from .views import signup_view, home_view, upload_file

urlpatterns = [
    path("", home_view, name="home"),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path("signup/", signup_view, name="signup"),
    path("upload/", upload_file, name="upload"),
]
