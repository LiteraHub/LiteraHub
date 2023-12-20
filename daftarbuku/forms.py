from django import forms
from .models import *


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review']
        exclude = ['user', 'book', 'created_at', 'username']

    review = forms.CharField(
        label='',
        required=True,
        max_length=255,
        error_messages={
            'required': 'Please type',
        },
        widget=forms.Textarea(
            attrs={
                'id': 'review_body',
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Insert your review',
            }
        ),
    )
