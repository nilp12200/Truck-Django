from django.urls import path
from . import views

urlpatterns = [
    # default route

    path('', views.login, name='login'),  # Login page
    path('home/', views.home, name='home'),  # Home page
    path('staff/', views.staff, name='staff'),  # Staff page
    path('gate/', views.gatekeeper, name='gatekeeper'),  # Gate keeper
    path('truck/', views.truck_transaction, name='truck_transaction'),  # Truck transactions
    path('plantmaster/', views.plant_master, name='plant_master'),  # Plant master

]
