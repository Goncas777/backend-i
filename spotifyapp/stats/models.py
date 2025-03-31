import os
import logging
from django.db import models
from django.contrib.auth import get_user_model
from django.core.files.storage import default_storage

logger = logging.getLogger(__name__)

def user_directory_path(filename):
    return f"uploads/{filename}"

class UploadedFile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        existing_files = UploadedFile.objects.exclude(id=self.id)
        for obj in existing_files:
            if obj.file.name.endswith('.zip'):
                logger.info(f"Deleting old ZIP file: {obj.file.name}")
                default_storage.delete(obj.file.name)
        logger.info(f"Saving new file: {self.file.name}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.file.name} ({self.user.username if self.user else 'No user'})"

class GeneratedJSON(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    file = models.FileField(upload_to="json_files/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"JSON from {self.user.username} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

# Create your models here.
