from rest_framework import generics

from .models import Section, Student
from .serializers import SectionSerializer, StudentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class StudentList(generics.ListCreateAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.all()
        Section = self.request.query_params.get('section')
        if Section is not None:
            queryset = queryset.filter(studentSection=Section)
        return queryset
    
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    
class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]


class SectionList(generics.ListCreateAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    

class SectionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]