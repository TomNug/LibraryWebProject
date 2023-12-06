# members / urls
from django.urls import path
from . import views

# from . import views
app_name = "members"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:memberId>", views.member, name = "member_detail"),
    path("members/add_member", views.add_member, name = "add_member"),
    path("delete_member/<int:id>", views.delete_member, name = "delete_member"),
    path("update/<int:id>", views.update_member, name = "update_member")
    ]