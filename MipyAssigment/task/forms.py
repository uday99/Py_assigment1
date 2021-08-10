from  django import forms
from .models import User

class UserForm(forms.ModelForm):
    dob=forms.CharField(label='Date of Birth',widget=forms.SelectDateWidget(years=range(1900,2100)))
    class Meta:
        model=User
        fields="__all__"
        labels={
            'phoneno':'PhoneNumber',

        }

