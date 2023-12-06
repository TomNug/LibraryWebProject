from django.shortcuts import render
from .models import Loan
from .forms import LoanFilterForm, LoanForm
from django.urls import reverse
from django.http import HttpResponseRedirect

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




def add_loan(request):
    # if user submitted some form data
    if request.method == "POST":
        # request.POST contains all of the data when the
        # form was submitted
        form = LoanForm(request.POST)
        # did user provide necessary data?
        # added method to ensure ISBN is unique
        if form.is_valid():
            # Save
            form.save()
            return HttpResponseRedirect(reverse("loans:index"))
        else:
            # render the form but pass in data so far
            return render(request, "loans/add_loan.html", {
                "form": form})
    # if the request wasn't post at all, render an empty form
    return render(request, "loans/add_loan.html", {
        "form": LoanForm()})