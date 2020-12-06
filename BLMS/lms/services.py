from concurrent import futures
import grpc
from google.protobuf import empty_pb2
from django_grpc_framework.services import Service
from django.contrib.auth.models import User
from django_grpc_framework import generics
from .serializers import CustomUserProtoSerializer

from BLMS.lms_proto import course_pb2, course_pb2_grpc


"""class CourseService(Service):
    def List(self, request, context):
        courses = Course.objects.all()
        serializer = CourseProtoSerializer(posts, many=True)
        for msg in serializer.message:
            yield msg

    def Create(self, request, context):
        serializer = CourseProtoSerializer(message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            self.context.abort(grpc.StatusCode.NOT_FOUND, 'Post:%s not found!' % pk)

    def Retrieve(self, request, context):
        course = self.get_object(request.id)
        serializer = CourseProtoSerializer(course)
        return serializer.message

    def Update(self, request, context):
        course = self.get_object(request.id)
        serializer = CourseProtoSerializer(post, message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def Destroy(self, request, context):
        course = self.get_object(request.id)
        course.delete()
        return empty_pb2.Empty()"""


class CourseController(course_pb2_grpc.CourseControllerServicer):
    def Login(self, request, context):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        course_pb2_grpc.add_CourseControllerServicer_to_server(CourseController(), server)
        server.add_insecure_port('[::]:50051')
        server.start()
        server.wait_for_termination()
        return course_pb2.CourserReply()

