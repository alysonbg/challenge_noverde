from django.urls import path

from loan_service.api import views

app_name = 'api'
urlpatterns = [
    path('loan/', views.create_loan, name='loan'),
]
