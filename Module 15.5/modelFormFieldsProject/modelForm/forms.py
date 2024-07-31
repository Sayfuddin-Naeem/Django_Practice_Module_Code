from django import forms
from modelForm.models import Medium, Medium2

class MediumForm(forms.ModelForm):
    class Meta:
        model = Medium
        fields = '__all__'

class MediumForm2(forms.ModelForm):
    class Meta:
        model = Medium2
        fields = '__all__'
    