from django.urls import path
from .views import FinanciamentoVeiculoListCreateView 

urlpatterns = [
    path('financiamentoVeiculo/',FinanciamentoVeiculoListCreateView.as_view())
]
