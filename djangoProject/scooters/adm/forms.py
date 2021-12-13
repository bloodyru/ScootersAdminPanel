from .models import User,Zone, TypeOfZone
from django.forms import ModelForm,TextInput,SelectMultiple,CheckboxInput
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
class TypeOfZoneForm(ModelForm):
    class Meta:
        # status = UserProfile._meta.get_field('CanYouScooterOnThisArea').formfield(empty_label=u'Не указан', required=False)
        model = TypeOfZone
        fields = ['TypeZone', 'ColorZone', 'CanYouScooterOnThisArea', 'CanYouParkingOnThisArea', 'MaxSpeed', 'Description']
        widgets = {
            "TypeZone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тип зоны'
            }),
            "ColorZone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цвет зоны',
                'style': 'width: 15%; margin-left:10'
            }),
            "CanYouScooterOnThisArea": CheckboxInput(attrs={
            } ),
            "CanYouParkingOnThisArea": CheckboxInput(attrs={
            }),
            "MaxSpeed": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Максимальная скорость'
            }),

        }


