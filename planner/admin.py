from django.contrib import admin
from .models import Trip, Destination, Expense, Schedule

admin.site.register(Trip)
admin.site.register(Destination)
admin.site.register(Expense)
admin.site.register(Schedule)