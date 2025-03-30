import os
from django.db import models
from django.contrib.auth import get_user_model
from django.core.files.storage import default_storage
from django.core.exceptions import ObjectDoesNotExist

# Função que define o caminho do upload
def user_directory_path(filename):
    # Diretório será 'uploads/nome_do_ficheiro.ext'
    return f"uploads/{filename}"


class UploadedFile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to="uploads/")  # Define sempre o mesmo caminho
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Se já existir um arquivo ZIP (independente do usuário), apaga o antigo
        existing_files = UploadedFile.objects.exclude(id=self.id)  # Exclui o atual (caso esteja sendo editado)
        for obj in existing_files:
            if obj.file.name.endswith('.zip'):
                default_storage.delete(obj.file.name)  # Apaga o arquivo ZIP anterior

        # Chama o método save do modelo
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.file.name} ({self.user.username if self.user else 'No user'})"


    
class GeneratedJSON(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # Relacionado ao utilizador
    file = models.FileField(upload_to="json_files/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"JSON de {self.user.username} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"


# Create your models here.
