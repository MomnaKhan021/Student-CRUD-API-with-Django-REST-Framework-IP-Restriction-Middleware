from django.db import models

class Student(models.Model):  # Use singular name and PascalCase
    SECTION_CHOICES = [
        ('A', 'Section A'),
        ('B', 'Section B'),
        ('C', 'Section C'),
    ]

    name = models.CharField(max_length=100)
    registration_no = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    room_no = models.IntegerField()
    section = models.CharField(max_length=1, choices=SECTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.registration_no})"
