from spotify import views
from django.contrib.auth.views import LoginView
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("tasks", views.TaskListView.as_view(), name="task_list"),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("signin", LoginView.as_view(), name="signin"),
    path("logout", views.logout_view, name="logout"),
    path("", views.IndexView.as_view(), name="index"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)