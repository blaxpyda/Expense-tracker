# tracker/urls.py
from django.urls import path
from .views import home, income, expense, signup, login
from tracker import views

urlpatterns = [
    path('', home, name='home'), #landing page
    path('signup/', views.signup, name='signup'),  # Sign-up page
    path('login/', views.CustomLoginView.as_view(), name='login'),  # Login page
    path('income/', income, name='income'),
    path('expense/', expense, name='expense'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
