
import email
from django import forms
from . models import Student
from django.core.exceptions import ValidationError
class Studentform(forms.ModelForm):
    class Meta: 
        model=Student
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
            're_password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }
    def clean(self):
        cleaned_data=super().clean()
        pass1=self.cleaned_data['password']
        pass2=self.cleaned_data['re_password']
        if len(pass1) < 8:
            raise forms.ValidationError('Password should be minimum 8 charecter')
        if pass1 !=  pass2:
            raise forms.ValidationError('Password didnot mathched!')
        


    
        
