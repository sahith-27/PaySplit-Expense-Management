"""
URL configuration for expense_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from expenseapp import views


urlpatterns = [

    # Django admin
    path('admin/', admin.site.urls),

    # Add expense
    path('add/', views.add_expense, name='add-expense'),

    # Display expenses
    path('expenses/', views.expense_list, name='expense-list'),

    # Update expense
    path('update/<int:id>/', views.update_expense, name='update-expense'),

    # Delete expense
    path('delete/<int:id>/', views.delete_expense, name='delete-expense'),

    # Register
    path('register/', views.register, name='register'),

    # Login
    path('login/', views.user_login, name='login'),

    # Logout
    path('logout/', views.user_logout, name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    path('', views.home, name='home'),
]