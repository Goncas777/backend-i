from django.contrib.auth.views import LoginView
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from spotify import views
from spotify.views import upload_arquivo

urlpatterns = [
    path("tasks/", views.TaskListView.as_view(), name="task_list"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signin/", LoginView.as_view(), name="signin"),
    path("logout/", views.logout_view, name="logout"),
    path("", views.IndexView.as_view(), name="index"),
    path('upload/', upload_arquivo, name='upload_arquivo'),
]