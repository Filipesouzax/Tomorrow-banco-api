from rest_framework import serializers
from financiamentoImovel.models import FinanciamentoImovel

class FinanciamenoImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanciamentoImovel
        fields = '__all__'