from django.shortcuts import render
from django.urls import reverse
# Create your views here.


# View a list of all books
def index(request):
    return render(request, "LibraryWebProject/index.html")
