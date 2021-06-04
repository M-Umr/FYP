from django.urls import path
from . import views

urlpatterns = [

    path('', views.PaymentPageView.as_view(), name='pay_patient'),

    path('charge/', views.charge, name="charge"),
]
