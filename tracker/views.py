# tracker/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db.models import Sum

def home(request):
    return render(request, 'home.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("tracker:login")
    template_name = "signup.html"

@login_required
def income(request):
    if request.method == "POST":
        amount = request.POST['amount']
        source = request.POST['source']
        Income.objects.create(user=request.user, amount=amount, source=source, date=request.POST['date'])
        return redirect('dashboard')
    return render(request, 'income.html')

@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'expense_list.html', {'expenses': expenses})

@login_required
def add_expense(request):
    if request.method == 'POST':
        category = Category.objects.get(id=request.POST['category'])
        amount = request.POST['amount']
        date = request.POST['date']
        description = request.POST['description']
        Expense.objects.create(
            user=request.user, category=category, amount=amount, date=date, description=description
        )
        return redirect('tracker:expense_list')
    categories = Category.objects.filter(user=request.user)
    return render(request, 'add_expense.html', {'categories': categories})

@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    if request.method == 'POST':
        expense.delete()
        return redirect('tracker:expense_list')
    return render(request, 'delete_expense.html', {'expense': expense})

@login_required
def dashboard(request):
    user = request.user

    total_income = Income.objects.filter(user=request.user).aggregate(Sum('amount'))['amount__sum'] or 0
    total_expenses = Expense.objects.filter(user=request.user).aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expenses

    # Category-wise expense distribution
    category_expenses = Expense.objects.filter(user=request.user).values('category__name').annotate(
        total=Sum('amount')
    )

    context = {
        'user': user,
        'total_income': total_income,
        'total_expense': total_expenses,
        'balance': balance,
        'category_expenses': category_expenses,
    }

    return render(request, 'dashboard.html', context)

