from django import forms
from .models import Comment


class Message(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', 'rating', 'product')
