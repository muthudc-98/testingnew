from django import forms
from application1.models import Registerdata

class Registerform(forms.ModelForm):
    class Meta:
        model=Registerdata
        fields='__all__'