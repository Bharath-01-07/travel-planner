from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
    trip_name = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination_city = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.trip_name


class Destination(models.Model):
    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE,
        related_name='destinations'
    )
    place_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.place_name


class Expense(models.Model):
    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE,
        related_name='expenses'
    )
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.category
class Schedule(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    activity = models.CharField(max_length=200)
    date_time = models.DateTimeField()

    def __str__(self):
        return self.activity