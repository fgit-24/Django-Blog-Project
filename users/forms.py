from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ProfileModel, ContactMessage, NewsletterSubscriber
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email']:
            self.fields[fieldname].help_text = None


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['image']


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email', 'name']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if NewsletterSubscriber.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already subscribed.')
        return email