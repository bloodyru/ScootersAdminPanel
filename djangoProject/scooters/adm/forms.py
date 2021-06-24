from .models import User
from django.forms import ModelForm,TextInput

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['Name']
        widgets = {
            "Name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),

        }
