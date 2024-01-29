from django.db import models

class Section(models.Model):
    SectionName = models.CharField(max_length=255)

    def __str__(self):
        return self.SectionName

class Student(models.Model):
    StudentName = models.CharField(max_length=255)
    Email = models.EmailField(max_length=100)
    RollNumber = models.IntegerField()
    Section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.StudentName