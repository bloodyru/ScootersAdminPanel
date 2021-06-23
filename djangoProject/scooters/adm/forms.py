from .models import User
from django.forms import ModelForm,DateTimeInput,TextInput

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['DateOfRegistration','Name']
        widgets = {
            "Name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),

            "DateOfRegistration":DateTimeInput(attrs={
                'class':'form-control',
                'placeholder':'date'
            })
        }
