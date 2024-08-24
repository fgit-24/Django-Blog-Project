from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def sign_up(request):
    return render(request, 'users/sign_up.html')