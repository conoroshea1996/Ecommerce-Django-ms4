from django import forms
from .models import Comment


class Message(forms.ModelForm):
    class Meta:
        model = Comment
        widgets = {'date_posted': forms.HiddenInput()}
        fields = ('comment', 'rating', 'product')
