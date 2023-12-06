

# members/forms.py
from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstName', 'lastName', 'email']
        labels = {
            'firstName': 'First Name',
            'lastName': 'Last Name',
            'email': 'Email',
        }