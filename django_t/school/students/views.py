# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
# Create your views here.
class StudentList(APIView):
    def get(self,request):
        student = Student.objects.all()
        serializer = StudentSerializer(student,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)

