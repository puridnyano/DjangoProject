from rest_framework import serializers
from .models import Section, Student

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('__all__')
        #fields = ['id', 'SectionName']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('__all__')
        #fields = ['id', 'StudentName', 'Email', 'RollNumber' 'section']