from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from stats.forms import SignupForm, UploadFileForm
from stats.models import UploadedFile
import os



class CustomLoginView(LoginView):
    template_name = 'login.html'

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)  # Faz login automático após o registro
            return redirect("home")  # Redireciona para a página inicial (ou outra que quiseres)
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form})

def home_view(request):
    return render(request, "home.html")


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.user = request.user  # Associa o ficheiro ao utilizador autenticado
            uploaded_file.save()
            return redirect("/")  # Redireciona para uma página de sucesso
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})


# Create your views here.
