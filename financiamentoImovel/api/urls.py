from django.urls import path
from .views import FinanciamentoImovelListCreate


urlpatterns = [
    path('financiamento_imovel/', FinanciamentoImovelListCreate.as_view()),
]