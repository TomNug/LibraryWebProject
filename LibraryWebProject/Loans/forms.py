

# loans/forms.py
from django import forms
from .models import Loan


class LoanFilterForm(forms.Form):
    show_open_loans = forms.BooleanField(required=False, initial=True)
    show_returned_loans = forms.BooleanField(required=False, initial=True)