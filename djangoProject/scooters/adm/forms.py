from .models import User,Zone
from django.forms import ModelForm,TextInput,SelectMultiple

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
class ZoneredactorForm(ModelForm):
    class Meta:
        model = Zone
        fields = ['Name','TypeZone','GPSPoints','ColorZone']
        widgets = {
            "Name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            "TypeZone": SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'TypeZone'
            }),
            "GPSPoints": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'GPSPoints'
            }),
            "ColorZone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ColorZone'
            }),
        }

class NewZoneForm(ModelForm):
    class Meta:
        model = Zone
        fields = ['Name', 'TypeZone', 'GPSPoints', 'ColorZone']
        widgets = {
            "Name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            "TypeZone": SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'TypeZone'
            }),
            "GPSPoints": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'GPSPoints'
            }),
            "ColorZone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ColorZone'
            }),

        }
