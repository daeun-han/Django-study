from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category, Real_estate, MyUser, Like, Message
from .serializer import CateSerializer, RS_Serializer, Message_Serializer

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
    
class RecentMessage(APIView):

    def get(self, request, format=None):
        user = request.headers['Username']
        queryset_receiver = Message.objects.filter(receiver__email=user, recent_msg=True)
        queryset_sender = Message.objects.filter(sender__email=user, recent_msg=True)
        queryset_total = queryset_receiver | queryset_sender
        serializer = Message_Serializer(queryset_total, many=True)
        return Response(serializer.data)