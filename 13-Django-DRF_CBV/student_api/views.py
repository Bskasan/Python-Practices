from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework import mixins

from django.shortcuts import get_object_or_404

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

class StudentDetailUpdateDelete(APIView):

    # One Record Detail
    def get(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(instance=student)
        return Response(serializer.data)

    # Update
    def put(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete one record
    def delete(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        student.delete()
        return Response({"message" : "Deleted"}, status=status.HTTP_204_NO_CONTENT)
    

# ----------------------------------------------------------------
# One Class For All Methods

class StudentGPPD(APIView):

    def get(self, request, pk=0):
        if pk:
        # Tek kayıt görüntüle:
            student = get_object_or_404(Student, id=pk)
            serializer = StudentSerializer(instance=student)
            return Response(serializer.data)
        else:
        # Kayıtları listele:
            students = Student.objects.all()
            serializer = StudentSerializer(instance=students, many=True)
            return Response(serializer.data)
    
    # Yeni Kayıt (POST Method)
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Tek kayıt güncelle:
    def put(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # Tek kayıt sil:
    def delete(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        student.delete()
        return Response({ "message": "Deleted" }, status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------------------
# GenericAPIView
# https://www.django-rest-framework.org/api-guide/generic-views/#genericapiview
# Mixins
# https://www.django-rest-framework.org/api-guide/generic-views/#mixins
# ----------------------------------------------------------------


class StudentGenericListCreate(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Make list
    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)
    
    # New Record
    def post(self, request, *args, **kwargs):
        return self.create(self, request, *args, **kwargs)
    

# ----------------------------------------------------------------
# ListCreateAPIView
# RetrieveUpdateDestroyAPIView
# https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes
# ----------------------------------------------------------------
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Kayıt Listeleme ve Yeni Kayıt Ekleme:
class StudentListCreateAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Tek kayıt görüntüle/güncelle/sil:
class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # lookup_field = "id" # Default: "pk"

# ----------------------------------------------------------------
# ModelViewSet:
# https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
# ----------------------------------------------------------------
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

# Tüm İşlemler:
class StudentMVS(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(methods=["GET"], detail=False)
    def count(self, request):
        return Response({
            "count": Student.objects.count()
        })


