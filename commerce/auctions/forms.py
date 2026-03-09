from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Listing, Bid, Comment

class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("email",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # We are making the email optional here
        self.fields['email'].required = False
        self.fields['email'].help_text = "Optional: Used for account recovery."


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'starting_bid', 'image_url']
        # Adding Bootstrap classes to make it look nice
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'starting_bid': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control'}),
        }

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']
        widgets = {
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Bid Amount',
                'step': '0.01'
            }),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Add a comment...',
                'rows': 3
            }),
        }