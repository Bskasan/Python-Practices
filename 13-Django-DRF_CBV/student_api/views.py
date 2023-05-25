from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Student
from .serializers import StudentSerializer

# Make List 
class StudentListCreate(APIView):
    
    # GET METHOD
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(instance=students, many=True)
        return Response(serializer.data)

    # New Record (POST METHOD)
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # You can use else here as well.