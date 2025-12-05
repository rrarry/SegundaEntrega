from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo']
        widgets = {
            'titulo': forms.TextInput(attrs={'size': '50'}),
            'conteudo': forms.Textarea(attrs={'rows': 10, 'cols': 60}),
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
