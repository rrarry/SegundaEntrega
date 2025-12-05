from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo']
        widgets = {
            'titulo': forms.TextInput(attrs={'size': '50'}),
            'conteudo': forms.Textarea(attrs={'rows': 10, 'cols': 60}),
        }
