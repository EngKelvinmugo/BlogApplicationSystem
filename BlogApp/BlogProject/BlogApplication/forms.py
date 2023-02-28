from .models import *
from django import forms
from django.forms import ModelForm

class blogForm(ModelForm):
    class Meta:
        model=Blogs
        fields='__all__'
        exclude=['likes','date']