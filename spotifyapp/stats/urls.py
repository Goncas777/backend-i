from django.urls import path
from django.contrib.auth.views import LoginView
from .views import signup_view, home_view, upload_file, download_summary
from . import views

urlpatterns = [
    path("", home_view, name="home"),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path("signup/", signup_view, name="signup"),
    path('upload/', views.upload_file, name='upload_file'),
    path('upload/success/', views.upload_success, name='upload_success'),
    path('process-file/', views.process_file, name='process_file'),
    path("summary/", views.show_summary, name="show_summary"),
    path("download-summary/", download_summary, name="download_summary"),
]
