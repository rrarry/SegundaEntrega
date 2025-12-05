from django.contrib import admin
from .models import Post, Comment, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome', 'descricao']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'data_postagem']
    list_filter = ['data_postagem', 'categorias']
    search_fields = ['titulo', 'conteudo']
    filter_horizontal = ['categorias']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['autor', 'post', 'data_postagem']
    list_filter = ['data_postagem']
    search_fields = ['texto', 'autor__username']
