from django.shortcuts import render
from django.urls import reverse
# Create your views here.


# View the homepage
def index(request):
    return render(request, "LibraryWebProject/index.html")
