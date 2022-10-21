from django import forms
from .models import *


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = '__all__'

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'
