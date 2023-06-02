from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category, Real_estate, MyUser
from .serializer import CateSerializer, RS_Serializer

class CateViewSet(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        queryset = Category.objects.all()
        serializer = CateSerializer(queryset, many=True)
        return Response(serializer.data)

class RS_ViewSet(APIView):
    authentication_classes = []
    permission_classes = []
    
    def get(self, request, format=None):
        queryset = Real_estate.objects.all()
        serializer = RS_Serializer(queryset, many=True)
        return Response(serializer.data)
    
class LandMark(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        queryset = Real_estate.objects.filter(category__name="랜드마크")
        serializer = RS_Serializer(queryset, many=True)
        return Response(serializer.data)

class Residential(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        queryset = Real_estate.objects.filter(category__name="주거용")
        serializer = RS_Serializer(queryset, many=True)
        return Response(serializer.data)

class Commercial(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        queryset = Real_estate.objects.filter(category__name="상업용")
        serializer = RS_Serializer(queryset, many=True)
        return Response(serializer.data)
    
class Signup(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request, format=None):
        if MyUser.objects.filter(email=request.data['username']).count()>=1:
            return Response("email Error")
        else:
            email = request.data['username']
            name = request.data['nickname']
            password = request.data['password']
            MyUser.objects.create_user(email=email, name=name, password=password)
            return Response(email)