# tracker/views.py
from django.shortcuts import render, redirect
from .models import Income, Expense, Goal
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after sign-up
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'

@login_required
def income(request):
    if request.method == "POST":
        amount = request.POST['amount']
        source = request.POST['source']
        Income.objects.create(user=request.user, amount=amount, source=source, date=request.POST['date'])
        return redirect('dashboard')
    return render(request, 'income.html')

@login_required
def expense(request):
    if request.method == "POST":
        amount = request.POST['amount']
        category = request.POST['category']
        Expense.objects.create(user=request.user, amount=amount, category=category, date=request.POST['date'])
        return redirect('dashboard')
    return render(request, 'expense.html')

@login_required
def dashboard(request):
    incomes = Income.objects.filter(user=request.user)
    expenses = Expense.objects.filter(user=request.user)
    goals = Goal.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'incomes': incomes, 'expenses': expenses, 'goals': goals})

