from rest_framework import serializers
from django_grpc_framework import proto_serializers
from lms_proto import course_pb2

from .models import Message
from .models import Course

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields='__all__'

class CourseProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Course
        proto_class = course_pb2.Course
        fields = ['course_id', 'course_title']




