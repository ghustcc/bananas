from django.urls import path
from . import views

urlpatterns = [
    path('', views.listLots, name='Lotes'),
    path('lot/<int:id>', views.viewLot, name='Lote'),
    path('deleteLot/<int:id>', views.deleteLot, name='Delete Lote'),
    # path('deleteCut/<int:id>', views.deleteLot, name='Delete Corte'),
    path('dashboard/', views.dashboard, name='Dashboard'),
]
