from django.urls import path
from .views import SimulacaoEmprestimoCreateView, SimulacaoEmprestimoDetailView, SimulacaoEmprestimoListView,SimularEmprestimoGetView

urlpatterns = [
    path('criar_emprestimo/', SimulacaoEmprestimoCreateView.as_view()),
    path('listar_emprestimo/', SimulacaoEmprestimoListView.as_view()),
    path('lista_um_emprestimo/<int:pk>/', SimulacaoEmprestimoDetailView.as_view()),
    path('resultado_simulacao_emprestimo/<str:id>',SimularEmprestimoGetView.as_view()),
]