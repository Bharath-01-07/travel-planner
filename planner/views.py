from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Trip, Expense
from .forms import TripForm, DestinationForm, ExpenseForm, ScheduleForm
from .weather import get_weather


def home(request):
    return HttpResponse("Travel Planner Working Successfully!")


@login_required
def add_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)

        if form.is_valid():
            trip = form.save(commit=False)
            trip.user = request.user
            trip.save()
            return redirect('/')
    else:
        form = TripForm()

    return render(request, 'add_trip.html', {'form': form})


# Leave all your other functions unchanged