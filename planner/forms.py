from django.forms import ModelForm
from .models import Trip, Destination, Expense, Schedule


class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = '__all__'


class DestinationForm(ModelForm):
    class Meta:
        model = Destination
        fields = '__all__'


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'