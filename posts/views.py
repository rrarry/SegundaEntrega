from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm


class PostListView(ListView):
    """Lista todos os posts"""
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    """Exibe detalhes de um post específico"""
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    """Cria um novo post"""
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})


class PostUpdateView(UpdateView):
    """Edita um post existente"""
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    context_object_name = 'post'
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})


class PostDeleteView(DeleteView):
    """Deleta um post"""
    model = Post
    template_name = 'post_confirm_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post_list')
