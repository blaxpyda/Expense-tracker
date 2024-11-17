# tracker/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = "tracker"

urlpatterns = [
    path('', home, name='home'), #landing page
    # path('signup/', signup, name='signup'),  # Sign-up page
    path('signup/', SignUpView.as_view(), name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('income/', income, name='income'),
    path('expense/', expense, name='expense'),
    path('dashboard/', dashboard, name='dashboard'),
]
