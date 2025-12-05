from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Post


def post_list(request):
    """Lista todos os posts"""
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, pk):
    """Exibe detalhes de um post específico"""
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404("Post não encontrado")
    return render(request, 'post_detail.html', {'post': post})


def post_create(request):
    """Cria um novo post"""
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        
        post = Post(titulo=titulo, conteudo=conteudo)
        post.save()
        
        return redirect('post_detail', pk=post.pk)
    
    return render(request, 'post_form.html')


def post_edit(request, pk):
    """Edita um post existente"""
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404("Post não encontrado")
    
    if request.method == 'POST':
        post.titulo = request.POST.get('titulo')
        post.conteudo = request.POST.get('conteudo')
        post.save()
        
        return redirect('post_detail', pk=post.pk)
    
    return render(request, 'post_form.html', {'post': post})


def post_delete(request, pk):
    """Deleta um post"""
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404("Post não encontrado")
    
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    
    return render(request, 'post_confirm_delete.html', {'post': post})
