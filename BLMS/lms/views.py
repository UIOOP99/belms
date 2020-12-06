from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import MessageSerializer, HomeworkSerializer, CustomUserProtoSerializer, CourseProtoSerializer
from .models import Message, Homework, CustomUser
from BLMS.lms import clients


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


class HomeworkViewSet(viewsets.ModelViewSet):
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()
    ordering_fields = '__all__'


@api_view(['GET', 'POST'])
class LoginView(APIView):
    def login(self, request):
        courses = []
        if request.method == 'POST':
            serializer = CustomUserProtoSerializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            id = serializer.validated_data['user_id']
            global courses
            courses = clients.run(id)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        elif request.method == 'GET':
            serializer = CourseProtoSerializer(courses, many=True)
            return Response(serializer.data)


class MessageView(APIView):
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        store = Message.objects.get(author=serializer.validated_data['author'],
                                    course=serializer.validated_data['course'],
                                    content=serializer.validated_data['content'])
        store.save()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
class HomeworkView(APIView):
    def hw(self, request):
        if request.method == 'POST':
            serializer = HomeworkSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            # GRPC to file system