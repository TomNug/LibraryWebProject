

# loans/forms.py
from django import forms
from .models import Loan
from Books.models import BookCopy

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

    def __init__(self, *args, **kwargs):
        super(LoanForm, self).__init__(*args, **kwargs)
        # Limits the available books
        # Only books which aren't on loan could be loaned
        self.fields['bookCopy'].queryset = BookCopy.objects.filter(onLoan=False)
