from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'partials/index.html'

class DashboardView(TemplateView):
    template_name = 'partials/dashboard.html'