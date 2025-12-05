from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'data_postagem']
    list_filter = ['data_postagem']
    search_fields = ['titulo', 'conteudo']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['autor', 'post', 'data_postagem']
    list_filter = ['data_postagem']
    search_fields = ['texto', 'autor__username']
