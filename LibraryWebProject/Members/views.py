from django.shortcuts import render
from .models import Member
from .forms import MemberForm
from django.urls import reverse
from django.http import HttpResponseRedirect
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

def add_member(request):
    # if user submitted some form data
    if request.method == "POST":
        # request.POST contains all of the data when the
        # form was submitted
        form = MemberForm(request.POST)
        # did user provide necessary data?
        # added method to ensure ISBN is unique
        if form.is_valid():
            # Save
            form.save()
            return HttpResponseRedirect(reverse("members:index"))
        else:
            # render the form but pass in data so far
            return render(request, "members/add_member.html", {
                "form": form})
    # if the request wasn't post at all, render an empty form
    return render(request, "members/add_member.html", {
        "form": MemberForm()})