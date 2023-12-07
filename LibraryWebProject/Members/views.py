from django.shortcuts import render
from .models import Member
from Books.models import BookCopy
from Loans.models import Loan
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
    loans = Loan.objects.filter(member = memberId)
    return render(request, "Members/member.html",{
        # which book is rendered
        "member":member,
        # loans
        "loans":loans
    })

def add_member(request):
    # if user submitted some form data
    if request.method == "POST":
        # request.POST contains all of the data when the
        # form was submitted
        form = MemberForm(request.POST)
        # did user provide necessary data?
        if form.is_valid():
            # Save
            form.save()
            return HttpResponseRedirect(reverse("members:index"))
        else:
            # render the form but pass in data so far
            return render(request, "Members/add_member.html", {
                "form": form})
    # if the request wasn't post at all, render an empty form
    return render(request, "Members/add_member.html", {
        "form": MemberForm()})


def delete_member(request, id):
    memberToDelete = Member.objects.get(pk=id)

    if request.method == 'POST':
        memberToDelete.delete()
        return HttpResponseRedirect(reverse("members:index"))
    return render(request, "Members/delete_member.html", {
        # which member is rendered
        "member":memberToDelete,})


def update_member(request, id):
    memberToUpdate = Member.objects.get(pk=id)
   # if user submitted some form data
    if request.method == "POST":
        # request.POST contains all of the data when the
        # form was submitted
        form = MemberForm(request.POST, instance=memberToUpdate)

        # did user provide necessary data?
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("members:member_detail", args=(memberToUpdate.id,)))
        else:
            # render the form but pass in data so far
            return render(request, "Members/update_member.html", {
                "form": form, "member": memberToUpdate})
    else:
        # if the request wasn't post at all, prepopulate form
        populatedForm = MemberForm(instance=memberToUpdate)
    return render(request, "Members/update_member.html", {
            "form": populatedForm, "member": memberToUpdate})
