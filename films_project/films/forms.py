from django import forms
from .models import Film

# django ModelForm
class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
