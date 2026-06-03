def home(request):
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