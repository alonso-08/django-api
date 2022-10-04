from operator import itemgetter
from django.shortcuts import render
from .models import Maestro, Salon
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MaestroSerializer, SalonSerializer
# Create your views here.

class MaestroAPIView(APIView):

    def post(self,request,format=None,*args,**kwards):
        serializers=MaestroSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self,format=None,*args,**kwards):
        maestros=Maestro.objects.all()
        serializer=MaestroSerializer(maestros,many=True)
        return Response(serializer.data)


class SalonesMaestroAPIView(APIView):
    def get(self,request,pk,format=None,*args,**kwards):
        maestro=Maestro.objects.get(id=pk)
        salones_del_maestro=Salon.objects.filter(maestro=pk)
        
        salones_list=[]
        for salon in salones_del_maestro:
            object_salon={
                "letra":salon.letra,
                "codio":salon.codigo
                }
            salones_list.append(object_salon)
        data={
            "id":maestro.id,
            "nombre_completo":maestro.nombre_completo,
            "sueldo":maestro.sueldo,
            "salones":salones_list
            }
        return Response(data)

class SumSueldoAPIView(APIView):
    def get(self,request,format=None,*args,**kwards):
        maestros=Maestro.objects.all()
        total = sum(maestro.sueldo for maestro in maestros)
        data={"El sueldo total es":total}
        return Response(data)

class SalonesCodAPIView(APIView):
    def get(self,request,format=None,*args,**kwards):
        total_salones=Salon.objects.filter(codigo="COD").count()
        data={"El total de salones son:",total_salones}
        return Response(data=data)

class MaestrosSalonCodAPIView(APIView):
    def get(self,request,format=None,*args,**kwards):
        maestros=Maestro.objects.all()
        data=[]
        for maestro in maestros:
            salones=Salon.objects.filter(maestro=maestro.id).count()
            object_data={"Maestro":maestro.nombre_completo,"Total salones":salones}
            data.append(object_data)
            return Response(data=data)