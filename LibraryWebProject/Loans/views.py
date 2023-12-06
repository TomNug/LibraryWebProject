from django.shortcuts import render
from .models import Loan


# Create your views here.
# View a list of all members
def index(request):
    return render(request, "Loans/index.html")

# View a list of all members
def view_all(request):
    return render(request, "Loans/view_all.html", {
        "loansList": Loan.objects.all()
        })