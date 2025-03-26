from django.contrib import admin

from spotify.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ("title","description", "due_date", "is_done")
    list_editable = ("due_date", "is_done", "description")
    sortable_by = ("due_date", "is_done", "title")

admin.site.register(Task,TaskAdmin)

# Register your models here.
