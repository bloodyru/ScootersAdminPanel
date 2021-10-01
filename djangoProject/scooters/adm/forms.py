from .models import User,Zone
from django.forms import ModelForm,TextInput,SelectMultiple
from django import forms

class GaeParamsForm(forms.Form):
    hex_color = forms.CharField(label='hex_color', max_length=7,
        widget=forms.TextInput(attrs={'type': 'color'}))
    font_size = forms.IntegerField(label='font_size',
        min_value=1, max_value=400)

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
                "type": "color"
            }),
        }



class NewZoneForm(ModelForm):
    class Meta:
        model = Zone
        fields = ['Name', 'TypeZone', 'GPSPoints', 'ColorZone']
        hex_color = forms.CharField(label='hex_color', max_length=7,
                                    widget=forms.TextInput(attrs={'type': 'color'}))
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
