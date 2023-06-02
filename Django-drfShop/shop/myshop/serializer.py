from rest_framework import serializers
from myshop.models import Category, Real_estate, MyUser

class CateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class RS_Serializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url= True)      #추가
    class Meta:
        model = Real_estate
        fields = ('id','name','detail','image','price','category','likecount') #수정
