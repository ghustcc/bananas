from django.urls import path
from . import views

urlpatterns = [
    path('', views.listLots, name='Lotes'),
    path('dashboard/', views.dashboard, name='Dashboard'),
]
