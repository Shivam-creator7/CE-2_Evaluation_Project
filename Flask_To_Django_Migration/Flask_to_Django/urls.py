from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_expense, name='add_expense'),
    path('edit/<int:expense_id>/', views.edit_expense, name='edit_expense'),
    path('delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
]

