from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import  Document

class UserRegistrationForm(UserCreationForm):
    
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    


class DocumentForm(forms.ModelForm) :
	class Meta:
		model = Document
		fields = ('description', 'document', )

class DataLoadForm(forms.Form):
    file = forms.FileField() # for creating file input 



class addForm(forms.Form):
    email = forms.EmailField(max_length = 150, required=True)