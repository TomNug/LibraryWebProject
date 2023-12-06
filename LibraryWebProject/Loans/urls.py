
# loans / urls
from django.urls import path
from . import views

# from . import views
app_name = "loans"
urlpatterns = [
    path("", views.index, name="index"),
    path("Loans", views.view_all, name = "view_all"),
    ]