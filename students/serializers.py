from rest_framework import serializers
from .models import Student  # Corrected model name

class StudentSerializer(serializers.ModelSerializer):  # Corrected serializer name
    class Meta:
        model = Student
        fields = ['id', 'name', 'registration_no', 'email', 'room_no', 'section', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']  # Ensure these fields are read-only

    def validate_registration_no(self, value):
        """Ensure the registration number is unique."""
        if Student.objects.filter(registration_no=value).exists():  # Use the corrected model name
            raise serializers.ValidationError("A student with this registration number already exists.")
        return value

    def validate_email(self, value):
        """Ensure the email is unique."""
        if Student.objects.filter(email=value).exists():  # Use the corrected model name
            raise serializers.ValidationError("A student with this email already exists.")
        return value

    def validate_room_no(self, value):
        """Ensure the room number is a positive integer."""
        if value <= 0:
            raise serializers.ValidationError("Room number must be a positive integer.")
        return value

    def validate_section(self, value):
        """Ensure the section is one of the allowed choices."""
        if value not in ['A', 'B', 'C']:
            raise serializers.ValidationError("Section must be 'A', 'B', or 'C'.")
        return value

    def validate(self, data):
        """Perform additional validations if needed."""
        return data
