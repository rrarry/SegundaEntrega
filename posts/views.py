from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Post, Comment
from .forms import PostForm, CommentForm


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


@method_decorator(login_required, name='dispatch')
class CommentCreateView(CreateView):
    """Cria um novo comentário"""
    model = Comment
    form_class = CommentForm
    template_name = 'comment_form.html'
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['pk']})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.kwargs['pk'])
        return context
