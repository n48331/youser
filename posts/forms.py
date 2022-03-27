
from random import choices
from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    POST_TYPE = (
        ('ad', 'Advertisment'),
        ('event', 'Event'),
    )
    type = forms.ChoiceField(
        choices=POST_TYPE, widget=forms.RadioSelect)

    class Meta:
        model = Post
        fields = ['title', 'image', 'type', 'desc']
