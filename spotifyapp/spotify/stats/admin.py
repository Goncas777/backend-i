from django.contrib import admin
from .models import UploadedFile

class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ("id", "file", "user", "uploaded_at")  # Adicionei 'id' como primeiro campo
    search_fields = ("user__username", "file")  # Permite pesquisar por utilizador e nome do ficheiro
    list_filter = ("uploaded_at",)  # Filtro por data de upload
    list_editable = ("file", "user")  # Permite editar 'file' e 'user' diretamente na lista

admin.site.register(UploadedFile, UploadedFileAdmin)