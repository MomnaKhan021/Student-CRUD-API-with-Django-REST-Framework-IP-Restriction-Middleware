from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'registration_no', 'email', 'room_no', 'section', 'created_at', 'updated_at')
    search_fields = ('name', 'registration_no', 'email')
