from rest_framework import serializers 
from .models import Book,User 
from .models import Department
class BookSerializer(serializers.Serializer):
    class Meta:
        model = Book
        fields = '__all__'

from rest_framework import serializers 
class UserSerializer(serializers.Serializer):
    class Meta:
        model = User 
        fields = '__all__'

from rest_framework import serializers
class DepartmentSerilizer(serializers.Serializer):
    class Meta:
        model = Department 
        fields = '__all__'

from rest_framework import serializers
from .models import Manager 
class ManagerSerializer(serializers.Serializer):
    class Meta:
        model = Manager
        fields = '__all__'


