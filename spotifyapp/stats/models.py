import os
from django.db import models
from django.contrib.auth import get_user_model

# Função que define o caminho do upload
def user_directory_path(filename):
    # Diretório será 'uploads/nome_do_ficheiro.ext'
    return f"uploads/{filename}"


class UploadedFile(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to="uploads/")  # Guarda o ficheiro na pasta uploads/
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} ({self.user.username})"

# Create your models here.
