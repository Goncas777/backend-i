from django.contrib import admin

from spotify.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ("user", "file")
    list_display_links = ("user",)  # Define o campo clicável
    list_editable = ("file", )
    sortable_by = ("user", )

admin.site.register(Task, TaskAdmin)

# Register your models here.
