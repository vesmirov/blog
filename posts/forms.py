from django import forms

from .models import Post, PostComment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'preview', 'text')
        labels = {
            'title': 'Post title',
            'preview': 'Post preview',
            'text': 'Post text',
        }
        help_text = {
            'title': 'Add your title',
            'preview': 'Add your preview',
            'text': 'Add your text',
        }
        widgets = {'text': forms.Textarea(attrs={'cols': '70', 'rows': '20'})}


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('text',)
        labels = {'text': 'Text'}
        help_text = {'text': 'Comment text'}
        widgets = {'text': forms.Textarea(attrs={'cols': '40', 'rows': '4'})}
