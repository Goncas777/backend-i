from todo import views
from django.contrib.auth.views import LoginView
from django.urls import include, path

urlpatterns = [
    path("tasks", views.TaskListView.as_view(), name="task_list"),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("signin", LoginView.as_view(), name="signin"),
    path("", views.IndexView.as_view(), name="index"),
]