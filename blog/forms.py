from django import forms
from .models import Coment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Coment
        exclude = ["post"]
        labels = {
            "user_name": "Your Name",
            "user_email": "Your Email",
            "text": "Your Comment"
        }