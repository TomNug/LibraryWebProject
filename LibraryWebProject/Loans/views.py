from django.shortcuts import render
from .models import Loan
from .forms import LoanFilterForm

# Create your views here.
# View a list of all members
def index(request):
    return render(request, "Loans/index.html")

# View a list of all members
def view_all(request):
    
    filter_form = LoanFilterForm(request.GET)

    if filter_form.is_valid():
        # Get checkboxes from page
        show_open = filter_form.cleaned_data.get('show_open_loans')
        show_returned = filter_form.cleaned_data.get('show_returned_loans')

        # Filter based on options
        if (show_open and show_returned):
            loans = Loan.objects.all()
        elif show_open and not show_returned:
            loans = Loan.objects.filter(returned=False)
        elif not show_open and show_returned:
            loans = Loan.objects.filter(returned=True)
        else:
            loans = Loan.objects.none()

    return render(request, "Loans/view_all.html", {
        "loans": loans,
        'filter_form': filter_form
        })