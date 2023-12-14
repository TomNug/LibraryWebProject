from django.shortcuts import render
from .models import Loan, Book
from .forms import LoanFilterForm, LoanForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Count

# Create your views here.
# View a list of all loans
def index(request):
    return render(request, "Loans/index.html")


# Shows details of a loan
def loan(request, id):
    loan = Loan.objects.get(pk=id)
    return render(request, "Loans/loan.html",{
        # which loan to render
        "loan":loan,
    })


# View a list of all loans
def view_all(request):
    
    # Names of all of the books
    loanBookNames = Loan.objects.values('bookCopy__book__name') 
    # Count based on name
    loanBookCounts = loanBookNames.annotate(loanCount = Count("bookCopy__book__name"))
    # Descending order
    loanBookOrdered = loanBookCounts.order_by("-bookCopy__book__name")


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
        'filter_form': filter_form,
        'loan_counts': loanBookOrdered
        })




def add_loan(request):
    # if user submitted some form data
    if request.method == "POST":
        # request.POST contains all of the data when the
        # form was submitted
        form = LoanForm(request.POST)
        # did user provide necessary data?
        if form.is_valid():
            # Save
            loan = form.save()
            # Need to mark the copy as loaned
            loan.bookCopy.onLoan = True
            loan.bookCopy.save()
            return HttpResponseRedirect(reverse("loans:index"))
        else:
            # render the form but pass in data so far
            return render(request, "Loans/add_loan.html", {
                "form": form})
    # if the request wasn't post at all, render an empty form
    return render(request, "Loans/add_loan.html", {
        "form": LoanForm()})




def return_loan(request, loan_id):
    loan = Loan.objects.get(pk = loan_id)

    # Has it already been returned?
    if not loan.returned:
        # Set the loan to returned
        loan.returned = True
        loan.save()

        # Set the bookCopy to not on loan
        bookCopy = loan.bookCopy
        bookCopy.onLoan = False
        bookCopy.save()
    # Return to the view_all page
    return HttpResponseRedirect(reverse("loans:view_all"))
