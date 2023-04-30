from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    CHOICES = (
        ('option1', 'Meal Swipe Requests'),
        ('option2', 'Points Requests'),
        ('option3', 'Club Announcements'),
        ('option4', 'Selfless Swipes'),
    )

    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    category = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = Post
        fields = ['title', 'category', 'content']


