from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response 
from .serializers import EmployeeSerializer
from .models import Employee,Department


class EmployeeList(APIView):
    def get(self,request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        data = request.data 
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response('data saved successfully into employee table',status=201)
        return Response(serializer.errors,status=400)
        

# Create your views here.
