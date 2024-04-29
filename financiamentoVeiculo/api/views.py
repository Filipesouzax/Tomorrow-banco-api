from rest_framework import generics
from rest_framework.response import Response
from .serializers import FinanciamenoVeiculoSerializer
from financiamentoVeiculo.models import FinanciamentoVeiculo


class FinanciamentoVeiculoListCreateView(generics.ListCreateAPIView):
    queryset = FinanciamentoVeiculo.objects.all()
    serializer_class = FinanciamenoVeiculoSerializer