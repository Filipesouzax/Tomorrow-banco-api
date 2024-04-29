from rest_framework import generics
from rest_framework.response import Response
from financiamentoImovel.api.serializers import FinanciamenoImovelSerializer
from financiamentoImovel.models import FinanciamentoImovel

class FinanciamentoImovelListCreate(generics.ListCreateAPIView):
    queryset = FinanciamentoImovel.objects.all()
    serializer_class = FinanciamenoImovelSerializer