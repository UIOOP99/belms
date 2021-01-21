from rest_framework import serializers
from django_grpc_framework import proto_serializers
from .models import Assignment, Assignment_answer, Message
from protos import hw_file_pb2


class AssignmentSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Assignment
        proto_class = hw_file_pb2.UserRequest
        proto_class2 = hw_file_pb2.CourseRequest
        fields = ['course_id', 'file_id', 'description', 'deadline']


class AssignmentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment_answer
        fields = ['course_id', 'file_id', 'description']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['course_id', 'msg']
