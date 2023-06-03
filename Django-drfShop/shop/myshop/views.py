from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category, Real_estate, MyUser, Like, Message
from .serializer import CateSerializer, RS_Serializer, RS_detail_Serializer, Message_Serializer

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

class Detail(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, id, format=None):
        queryset = Real_estate.objects.get(id = id)
        serializer = RS_detail_Serializer(queryset, many=False)
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
        
class Recommand(APIView):
    def post(self, request, id, format=None):
        queryset = Real_estate.objects.get(id = id)
        user_email= request.data['username']
        user = MyUser.objects.get(email= user_email)
        Recommand_object = Like.objects.filter(user=user, realestate_post=queryset)
        if Recommand_object.count()>=1:
            Recommand_object.delete()
        else:
            Like.objects.create(user=user, realestate_post=queryset)

        queryset.likecount = Like.objects.filter(realestate_post=queryset).count()
        queryset.save()
        return Response("success")
    
def Real_estate_order(request, queryset):
    if request.headers['Sort'] == "recommand" or "":
        queryset = queryset.order_by('-likecount')
    elif request.headers['Sort'] == "-recommand":
        queryset = queryset.order_by('likecount')
    elif request.headers['Sort'] == "price":
        queryset = queryset.order_by('-price')
    elif request.headers['Sort'] == "-price":
        queryset = queryset.order_by('price')
    elif request.headers['Sort'] == "upload_date":
        queryset = queryset.order_by('upload_date')
    else:
        queryset = queryset.order_by('-upload_date')

    return queryset

class LandMark(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        queryset = Real_estate.objects.filter(category__name="랜드마크")

        ordered_queryset = Real_estate_order(request, queryset)

        serializer = RS_Serializer(ordered_queryset, many=True)
        return Response(serializer.data)

class Residential(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        queryset = Real_estate.objects.filter(category__name = "주거용")

        ordered_queryset = Real_estate_order(request, queryset)

        serializer = RS_Serializer(ordered_queryset, many=True)
        return Response(serializer.data)

class Commercial(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        queryset = Real_estate.objects.filter(category__name = "상업용")

        ordered_queryset = Real_estate_order(request, queryset)

        serializer = RS_Serializer(ordered_queryset, many=True)
        return Response(serializer.data)
