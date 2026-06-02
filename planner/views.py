from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Trip, Expense
from .forms import TripForm, DestinationForm, ExpenseForm, ScheduleForm
from .weather import get_weather


def home(request):
    # If users should only see their own trips, change this to: Trip.objects.filter(user=request.user)
    trips = Trip.objects.all()
    total_expense = sum(
        expense.amount for expense in Expense.objects.all()
    )
    return render(
        request,
        'home.html',
        {
            'trips': trips,
            'total_expense': total_expense
        }
    )


@login_required
def add_trip(request):
    if request.method == 'POST':
        # FIX: Pass request.POST directly to the form instead of rebuilding it manually.
        # This ensures all hidden attributes and validations map accurately.
        form = TripForm(request.POST)

        if form.is_valid():
            # 1. Stop the database from saving instantly
            trip = form.save(commit=False)

            # 2. Explicitly bind the logged-in user to the trip object
            trip.user = request.user

            # 3. Save to database safely
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
        # FIX: Clean up manual dictionary binding to avoid validation drops
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
        # FIX: Clean up manual dictionary binding to avoid validation drops
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