

from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

route = routers.DefaultRouter()


schema_view = get_schema_view(
    openapi .Info(
        title ="BANCO API" ,  
        default_version ='v1',
        description ="Estamos gerando documentação para nossa API banco(sistema financeiro)" ,
        terms_of_service ="",
        license =openapi.License(name ="BSD License" ),
    ),
    public =True,
    permission_classes =(permissions .AllowAny,),
    )

urlpatterns = [
    path( 'swagger<format>/' , schema_view .without_ui(cache_timeout =0), name='schema-json' ),
    path( 'swagger/' , schema_view .with_ui( 'swagger' , cache_timeout =0), name='schema-swagger-ui' ),
    path( 'redoc/' , schema_view .with_ui( 'redoc', cache_timeout =0), name='schema-redoc' ), 
    path("admin/", admin.site.urls),
    path('api/emprestimos/', include("emprestimos.api.url")),
    path('api/financiamentoImovel/', include('financiamentoImovel.api.urls')),
    path ('api/financiamentoVeiculo/', include('financiamentoVeiculo.api.urls'))
   
]
