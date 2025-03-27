from django.shortcuts import redirect, render
from django.http import HttpResponseForbidden
from django.views.generic import ListView, TemplateView, FormView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user, logout
from spotify.models import Task
from spotify.forms import TaskForm



#  def index(request):
#     tasks = Task.objects.all()
#     return render(request,"spotify/index.html", {"foo":"BOT", "tasks": tasks})
class TaskListView(LoginRequiredMixin, CreateView):
    login_url = "/signin"
    success_url = "tasks"
    form_class = TaskForm
    template_name = "spotify/task_list.html"

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Task.objects.filter(user=self.request.user).all()
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
class IndexView(TemplateView):
    http_method_names = ['get']
    template_name = "spotify/index.html"

class SignUpView(FormView):
    template_name = "registration/signup.html"
    success_url="/signin"
    form_class = UserCreationForm
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")


def upload_arquivo(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)  # Importante: request.FILES é necessário para arquivos
        if form.is_valid():
            form.save()
            return redirect('sucesso')  # Redirecionar para uma página de sucesso
    else:
        form = TaskForm()
    return render(request, 'upload.html', {'form': form})


# Create your views here.
