from django.urls import path
from bananas.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='Index'),
    path('dashboard/', DashboardView.as_view(), name='Dashboard'),
]
