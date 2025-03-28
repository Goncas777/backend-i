import os
from django.db import models
from django.contrib.auth.models import User

# Função que define o caminho do upload
def user_directory_path(instance, filename):
    # Diretório será 'uploads/user_<id>/nome_do_ficheiro.ext'
    return f"uploads/user_{instance.user.id}/{filename}"

class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associa ao usuário
    file = models.FileField(upload_to=user_directory_path)  # Usa a função personalizada
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Data do upload

# Create your models here.
