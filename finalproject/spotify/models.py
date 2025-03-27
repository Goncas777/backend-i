from django.db import models
from django.contrib.auth import get_user_model



class Task(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to='uploads/', null = True)
    

    class Meta:
        db_table = "spotify_tasks"
        verbose_name = "Task"
        verbose_name_plural = "Tasks"    
