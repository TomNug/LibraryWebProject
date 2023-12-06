
# loans / urls
from django.urls import path
from . import views

# from . import views
app_name = "loans"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>", views.loan, name = "loan_detail"),
    path("Loans", views.view_all, name = "view_all"),
    path("add_loan", views.add_loan, name = "add_loan"),
    path('return/<int:loan_id>/', views.return_loan, name='return_loan'),
    ]