from django.shortcuts import render
from .models import Member
# Create your views here.


# View a list of all members
def index(request):
    return render(request, "Members/index.html", {
        "membersList": Member.objects.all()
        })
