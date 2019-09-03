from django import forms
from .models import Comment


class Message(forms.ModelForm):
    class Meta:
        model = Comment
        rating_choices = (
            ('', 'Rating'),
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5')
        )
        widgets = {
            'date_posted': forms.HiddenInput(),
            'rating': forms.Select(choices=rating_choices, attrs={'class': 'form-control'})
        }
        fields = ('comment', 'rating', 'product')
