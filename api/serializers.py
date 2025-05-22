from rest_framework import serializers
from students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    student_code = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'student_id', 'name', 'branch', 'student_code']

    def get_student_code(self, obj):
        return f"{obj.id}{obj.name}{obj.branch}"
