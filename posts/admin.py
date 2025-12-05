from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'data_postagem']
    list_filter = ['data_postagem']
    search_fields = ['titulo', 'conteudo']
