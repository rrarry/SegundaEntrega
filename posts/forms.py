from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo', 'categorias']
        widgets = {
            'titulo': forms.TextInput(attrs={'size': '50'}),
            'conteudo': forms.Textarea(attrs={'rows': 10, 'cols': 60}),
            'categorias': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'categorias': 'Categorias (selecione uma ou mais)'
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 4, 'cols': 60}),
        }
        labels = {
            'texto': 'Comentário'
        }
