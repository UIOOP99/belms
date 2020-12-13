from rest_framework import serializers
from .models import Assignment, Assignment_answer


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['course_id', 'file_id', 'description', 'deadline']


class AssignmentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment_answer
        fields = ['course_id', 'file_id', 'description']



