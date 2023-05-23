from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def home(request):
    return Response(
        # To change object to JSON.
        {
            'message': 'Hello World'
        }
    )
        
# -------------------------------------------------------------------
'''
    HTTP Request Types:
        GET -> Public verilerdir. Listeleme/Görüntüleme işlemlerinde kullanılır.
        POST -> Private verilerdir. Kayıt oluşturma işlemlerinde kullanılır. (ID'ye ihtiyaç duymaz.)
        * PUT -> Kayıt güncelleme işlemlerinde kullanılır. (Veri bir bütün olarak güncellenir.) (ID'ye ihtiyaç duyar.)
        * PATCH -> Kayıt güncelleme işlemlerinde kullanılır. (Verinin sadece ilgili kısmı güncellenir.) (ID'ye ihtiyaç duyar.)
        * DELETE -> Kayıt silme işlemlerinde kullanılır. (ID'ye ihtiyaç duyar.)
'''
# -------------------------------------------------------------------       

# All records in the StudentSerializers
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET']) # Default : GET
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)