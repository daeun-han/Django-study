from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from .models import Book #모델 불러오기
from .serializers import BookSerializer #시리얼라이저 불러오기

@api_view(['GET'])
def HelloAPI(request):
    return Response("hello world!")

class HelloAPI(APIView):
    def get(self, request, format=None):
        return Response("hello world")
    
@api_view(['GET', 'POST']) #GET, POST 요청을 처리하게 만들어주는 데코레이터
def booksAPI(request): #/book/
    if request.method == 'GET': #GET 요청(도서 전체 정보)
        books = Book.objects.all() #Book 모델로부터 전체 데이터 가져오기
        serializer = BookSerializer(books, many=True)
        #시리얼라이저에 전체 데이터를 한번에 집어넣기(직렬화, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST': #POST 요청(도서 정보 등록)
        serializer = BookSerializer(data=request.data)
        #POST 요청으로 들어온 데이터를 시리얼라이저에 집어넣기
        if serializer.is_valid(): #유효한 데이터라면
            serializer.save()
            #시리얼라이저의 역직렬화를 통해 save(), 모델시리얼라이저의 기본 create() 함수가 동작
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # 201 메시지를 보내며 성공!
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # 400 잘못된 요청!
        
@api_view(['GET'])
def bookAPI(request, bid):
    book = get_object_or_404(Book, bid=bid) # bid=id인 데이터를 가져오고, 없으면 404 에러
    serializer = BookSerializer(book)        #시리얼라이저에 전체 데이터를 집어넣기(직렬화)
    return Response(serializer.data, status=status.HTTP_200_OK)

class BooksAPI(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookAPI(APIView):
    def get(self, request, bid):
        book = get_object_or_404(Book, bid=bid)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)