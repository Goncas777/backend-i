from django.contrib import admin
from .models import UploadedFile

@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'user', 'uploaded_at')
    search_fields = ('file', 'user__username')
    list_filter = ('uploaded_at',)

    formfield_overrides = {
        UploadedFile._meta.get_field('file'): {'widget': admin.widgets.AdminFileWidget},
    }
