from django.shortcuts import render
from .models import Member
# Create your views here.


# View a list of all members
def index(request):
    return render(request, "Members/index.html", {
        "membersList": Member.objects.all()
        })

# Shows details of a member, and all of its loans
def member(request, memberId):
    member = Member.objects.get(pk=memberId)
    return render(request, "Members/member.html",{
        # which book is rendered
        "member":member,
        # copies
    })