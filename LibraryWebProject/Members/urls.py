# members / urls
from django.urls import path
from . import views

# from . import views
app_name = "members"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:memberId>", views.member, name = "member_detail"),
    ]