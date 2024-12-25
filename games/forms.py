from django import forms
from .models import Review  # Assuming you have a Review model

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment'] 