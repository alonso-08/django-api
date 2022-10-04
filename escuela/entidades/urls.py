from entidades.views import MaestroAPIView, SalonesMaestroAPIView,SumSueldoAPIView, SalonesCodAPIView, MaestrosSalonCodAPIView
from django.urls import path
from rest_framework import routers
router=routers.DefaultRouter()

app_name="api"
urlpatterns=[
    path("v1/maestros",MaestroAPIView.as_view()),
    path("v1/maestros/<int:pk>/",SalonesMaestroAPIView.as_view()),
    path("v1/sum-sueldo",SumSueldoAPIView.as_view()),
    path("v1/salones-cod",SalonesCodAPIView.as_view()),
    path("v1/maestros-total-salones",MaestrosSalonCodAPIView.as_view()),
]