from  django import forms
from . models import Library

class MovieForm(forms.ModelForm):
    class Meta:
        model = Library
        fields=['name','image','author','descreption','year']