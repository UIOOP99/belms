from rest_framework import serializers
from django_grpc_framework import proto_serializers

from protos.hw_file_pb2 import UserRequest, UserReply, FileRequest, FileReply, CourseRequest, CourseReply
from .models import Assignment, Assignment_answer, Message
from protos import hw_file_pb2


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['course_id', 'file_id', 'description', 'deadline']


class AssignmentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment_answer
        fields = ['course_id', 'file_id', 'description', 'homework_number_id']


class AnswerDownloadReqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment_answer
        fields = ['course_id', 'homework_number_id']


class AnswerDownloadResSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment_answer
        fields = ['user_id', 'file_id']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['course_id', 'msg']


class SeeMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['user_id', 'msg', 'date_of_send']

# ----------------------------------------- proto serializers -----------------------------------------------


class RoleReqProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = UserRequest
        proto_class = hw_file_pb2.UserRequest
        fields = ['user_id']


class RoleResProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = UserReply
        proto_class = hw_file_pb2.UserReply
        fields = ['role']


class ValidReqProtoSerializer(proto_serializers.ModelProtoSerializer):
    userID = serializers.IntegerField()
    courseID = serializers.CharField()

    class Meta:
        proto_class = hw_file_pb2.CourseRequest


class ValidResProtoSerializer(proto_serializers.ModelProtoSerializer):
    validation = serializers.BooleanField()

    class Meta:
        proto_class = hw_file_pb2.CourseReply


class HwReqProtoSerializer(proto_serializers.ModelProtoSerializer):
    hwID = serializers.CharField()

    class Meta:
        proto_class = hw_file_pb2.FileRequest


class HwResProtoSerializer(proto_serializers.ModelProtoSerializer):
    hwURL = serializers.CharField()

    class Meta:
        proto_class = hw_file_pb2.FileReply
