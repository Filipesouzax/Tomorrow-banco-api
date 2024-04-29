from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import SimulacaoEmprestimosSerializer
from emprestimos.models import SimulacaoEmprestimo

class SimulacaoEmprestimoCreateView(generics.ListCreateAPIView):
    serializer_class = SimulacaoEmprestimosSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request':request})

        if serializer.is_valid():
            retorno_salvamento = serializer.save()

        return Response ({
            "data":SimulacaoEmprestimosSerializer(retorno_salvamento,
                                                  context=self.get_serializer_context()).data,
            "result": "Dados salvos com sucesso"                                             
        }, status=status.HTTP_201_CREATED)
     
class SimulacaoEmprestimoDetailView(generics.RetrieveAPIView):
    queryset = SimulacaoEmprestimo.objects.all()
    serializer_class = SimulacaoEmprestimosSerializer

class SimulacaoEmprestimoListView(generics.ListAPIView):
    queryset = SimulacaoEmprestimo.objects.all()
    serializer_class = SimulacaoEmprestimosSerializer

class SimularEmprestimoGetView(generics.ListAPIView):
    serializer_class = SimulacaoEmprestimo

    def get(self,request,*args,**kwargs):
        try:
            id_solicitacao = kwargs['id']

            emprestimo_obj = SimulacaoEmprestimo.objects.filter(id=id_solicitacao).first()

            if (emprestimo_obj != None):
                calculo_montante = emprestimo_obj.valor_emprestimo * emprestimo_obj.taxa_juros * emprestimo_obj.prazo_meses
                
                return Response ({
                    'juros_total': calculo_montante
                },status.HTTP_200_OK)
            else:
                raise Exception ("Não existe solicitação")


        except:
            return Response({'error': "requisição não pode ser atendida"},
                            status=status.HTTP_400_BAD_REQUEST)

