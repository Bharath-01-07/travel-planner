from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-trip/', views.add_trip, name='add_trip'),
    path('add-destination/', views.add_destination, name='add_destination'),
    path('add-expense/', views.add_expense, name='add_expense'),
    path('add-schedule/', views.add_schedule, name='add_schedule'),
    path('weather/', views.weather_view, name='weather'),
]