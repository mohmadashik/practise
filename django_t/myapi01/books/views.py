from rest_framework import APIview

from rest_framework.response import Response

from rest_framework import status 
from .models import Book

from .serializers import BookSerializer

class BookList(APIview):
    def get(self,request):
        book = Book.objects.all()
        serializer = BookSerializer(book,many=True)
        return Response(serializer.data)
