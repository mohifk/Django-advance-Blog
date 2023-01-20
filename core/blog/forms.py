from django import forms
from.models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','author','content','status','category','published_date'
]