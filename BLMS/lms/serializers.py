from grpc import protos
from rest_framework import serializers
from django_grpc_framework import proto_serializers
from BLMS.lms_proto import course_pb2, course_pb2_grpc

from .models import Message, Homework, CustomUser
from .models import Course


class CustomUserProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = CustomUser
        proto_class = course_pb2.CourseRequest
        fields = ['userID']


class CourseProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Course
        proto_class = course_pb2.CourseReply
        fields = ['course_id', 'course_title']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'



