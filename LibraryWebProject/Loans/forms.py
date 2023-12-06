

# loans/forms.py
from django import forms
from .models import Loan


class LoanFilterForm(forms.Form):
    show_open_loans = forms.BooleanField(required=False, initial=True)
    show_returned_loans = forms.BooleanField(required=False, initial=True)

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['member', 'bookCopy']
        labels = {
            'member': 'Member ID',
            'bookCopy': 'Book',
        }
