from django.contrib.auth.forms import *
from .models import MyUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['first_name', 'email']