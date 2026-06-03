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


@login_required
def add_destination(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST)
        if form.is_valid():
            destination = form.save(commit=False)
            if hasattr(destination, 'user'):
                destination.user = request.user
            destination.save()
            return redirect('/')
    else:
        form = DestinationForm()

    return render(request, 'add_destination.html', {'form': form})


@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)

        if form.is_valid():
            expense = form.save(commit=False)
            if hasattr(expense, 'user'):
                expense.user = request.user
            expense.save()
            return redirect('/')
    else:
        form = ExpenseForm()

    return render(request, 'add_expense.html', {'form': form})


@login_required
def add_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)

        if form.is_valid():
            schedule = form.save(commit=False)
            if hasattr(schedule, 'user'):
                schedule.user = request.user
            schedule.save()
            return redirect('/')
    else:
        form = ScheduleForm()

    return render(request, 'add_schedule.html', {'form': form})


def weather_view(request):
    weather_data = None
    if request.method == 'POST':
        city = request.POST.get('city')
        weather_data = get_weather(city)

    return render(
        request,
        'weather.html',
        {
            'weather': weather_data
        }
    )