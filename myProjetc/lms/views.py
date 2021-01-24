"""import os

from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializer import AssignmentSerializer, AssignmentAnswerSerializer, MessageSerializer
from .models import Assignment, Assignment_answer, Message
import datetime
from rest_framework import status
from rest_framework.permissions import BasePermission, AllowAny, SAFE_METHODS
import jwt
import base64


from . import client


# Create your views here.
secret = base64.b64decode('LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlHYk1CQUdCeXFHU000OUFnRUdCU3VCQkFBakE0R0dBQVFBdmRrYTFzcTBRd2h0QStieDFBVHVTSUEzT2oxOQpYMk0rVExzZDF3SlBGbTI0U05OUXFUWFBidFFLamhFemhsK2ZDNWExZ2ttRzNpaTJBcWt6MnRaTWUzVUFDb3JSCm1QZXh5blR0cFFSQWFKalhDOGpkRXNDU3UvMlMrblpBMmdBc25uNDBRQWxzaEpBZHMybmRYd1FBSjk5T2tXeTUKcEduRkQ2M042Vy84ODlZQW9acz0KLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0t')


class assignment_upload(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = AssignmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = request.headers.get('jwt')
        decoded_token = jwt.decode(token, secret, algorithm='ES512')
        userID = decoded_token['user_id']
        courseID  = serializer.validated_data['course_id']

        print("*******************************1 view")
        role = client.run_user(userID)
        if role == "PROFESSOR":
            valid_course = client.run_course(userID, courseID)
            if valid_course:
                instance = Assignment()
                #token = request.headers.get('jwt')
                #decoded_token = jwt.decode(token, secret, algorithm='ES512')
                instance.user_id = userID
                instance.course_id = courseID
                instance.file_id = serializer.validated_data['file_id']
                instance.description = serializer.validated_data['description']
                instance.start_date = datetime.datetime.now()
                instance.deadline = serializer.validated_data['deadline']
                instance.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class assignment_answer_upload(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = AssignmentAnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = request.headers.get('jwt')
        decoded_token = jwt.decode(token, secret, algorithm='ES512')
        userID = decoded_token['user_id']
        courseID  = serializer.validated_data['course_id']

        role = client.run_user(userID)
        if role == "STUDENT":
            valid_course = client.run_course(userID, courseID)
            if valid_course:
                instance = Assignment_answer()
                instance.user_id = userID
                instance.course_id = courseID
                instance.file_id = serializer.validated_data['file_id']
                instance.homework_number_id = serializer.validated_data['homework_number_id']
                instance.description = serializer.validated_data['description']
                instance.date_of_upload = datetime.datetime.now()
                instance.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class assignments_homeworklist(APIView):
    def get(self, request, format=None):
        selected_course = request.query_params.get('course_id', None)
        q1 = Assignment.objects.filter(course_id=selected_course)
        serializer = AssignmentSerializer(q1, many=True)
        return Response(serializer.data)


class assignment_download(APIView):
    permission_classes = [AllowAny]
    result = []

    def post(self, request, format=None):
        serializer = AssignmentAnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = request.headers.get('jwt')
        decoded_token = jwt.decode(token, secret, algorithm='ES512')
        userID = decoded_token['user_id']
        course_id = serializer.validated_data['course_id']
        hw_num_id = serializer.validated_data['homework_number_id']

        role = client.run_user(userID)
        if role == "PROFESSOR":
            valid_course = client.run_course(userID, course_id)
            if valid_course:
                selected_course = request.query_params.get(course_id, None)
                selected_homework = request.query_params.get(hw_num_id, None)
                q1 = Assignment_answer.objects.get(course_id=selected_course,
                                                   homework_number_id=selected_homework).values("File_id")
                student_id = Assignment_answer.objects.get(course_id=selected_course,
                                                           homework_number_id=selected_homework).values("user_id")
                answer_urls = client.run_file(q1)
                for i in range(len(answer_urls)):
                    self.result.append(student_id[i])
                    self.result.append(answer_urls[i])
            else:
                return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def get(self,requestf, format=None):
        serializer = AssignmentAnswerSerializer(self.result, many=True)
        return Response(serializer.data)


class write_message(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = request.headers.get('jwt')
        decoded_token = jwt.decode(token, secret, algorithm='ES512')
        userID = decoded_token['user_id']
        courseID  = serializer.validated_data['course_id']
        valid_course = client.run_course(userID, courseID)
        if valid_course:
            instance = Message()
            instance.user_id = userID
            instance.course_id = courseID
            instance.msg = serializer.validated_data['message']
            instance.date_of_send = datetime.datetime.now()
            instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


class see_message(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = request.headers.get('jwt')
        decoded_token = jwt.decode(token, secret, algorithm='ES512')
        userID = decoded_token['user_id']
        courseID = serializer.validated_data['course_id']
        valid_course = client.run_course(userID, courseID)
        if valid_course:
            selected_course = request.query_params.get(courseID, None)
            q1 = Assignment_answer.objects.get(course_id=selected_course).values("user_id", "msg", "date_of_send")
            serializer = MessageSerializer(q1, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
"""
# -------------------------------- removing grpc ---------------------------------------------
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializer import AssignmentSerializer, AssignmentAnswerSerializer, MessageSerializer,\
    AnswerDownloadReqSerializer, AnswerDownloadResSerializer, SeeMessageSerializer
from .models import Assignment, Assignment_answer, Message
import datetime
from rest_framework import status
from rest_framework.permissions import BasePermission, AllowAny, SAFE_METHODS
import jwt
import base64
from . import client


secret = base64.b64decode('LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlHYk1CQUdCeXFHU000OUFnRUdCU3VCQkFBakE0R0dBQVFBdmRrYTFzcTBRd2h0QStieDFBVHVTSUEzT2oxOQpYMk0rVExzZDF3SlBGbTI0U05OUXFUWFBidFFLamhFemhsK2ZDNWExZ2ttRzNpaTJBcWt6MnRaTWUzVUFDb3JSCm1QZXh5blR0cFFSQWFKalhDOGpkRXNDU3UvMlMrblpBMmdBc25uNDBRQWxzaEpBZHMybmRYd1FBSjk5T2tXeTUKcEduRkQ2M042Vy84ODlZQW9acz0KLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0t')


class assignment_upload(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = AssignmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = request.headers.get('jwt')
        decoded_token = jwt.decode(token, secret, algorithm='ES512')
        userID = decoded_token['user_id']
        courseID  = serializer.validated_data['course_id']

        instance = Assignment()
        instance.user_id = userID
        instance.course_id = courseID
        instance.file_id = serializer.validated_data['file_id']
        instance.description = serializer.validated_data['description']
        instance.start_date = datetime.datetime.now()
        instance.deadline = serializer.validated_data['deadline']
        instance.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class assignment_answer_upload(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = AssignmentAnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = request.headers.get('jwt')
        decoded_token = jwt.decode(token, secret, algorithm='ES512')
        userID = decoded_token['user_id']
        courseID  = serializer.validated_data['course_id']

        instance = Assignment_answer()
        instance.user_id = userID
        instance.course_id = courseID
        instance.file_id = serializer.validated_data['file_id']
        instance.homework_number_id = serializer.validated_data['homework_number_id']
        instance.description = serializer.validated_data['description']
        instance.date_of_upload = datetime.datetime.now()
        instance.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# http://127.0.0.1:8000/lms/assignment_list/?course_id=123
class assignments_homeworklist(APIView):
    def get(self, request, format=None):
        selected_course = request.query_params.get('course_id', None)
        q1 = Assignment_answer.objects.filter(course_id=selected_course)
        serializer = AssignmentAnswerSerializer(q1, many=True)
        return Response(serializer.data)


class assignment_download(APIView):
    permission_classes = [AllowAny]
    result = []

    def post(self, request, format=None):
        serializer = AnswerDownloadReqSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = request.headers.get('jwt')
        decoded_token = jwt.decode(token, secret, algorithm='ES512')
        userID = decoded_token['user_id']
        courseID = serializer.validated_data['course_id']
        hw_num_id = serializer.validated_data['homework_number_id']
        q1 = Assignment_answer.objects.filter(course_id=courseID, homework_number_id=hw_num_id)
        fileID = q1.values("user_id", "file_id")
        serializer2 = AnswerDownloadResSerializer(fileID, many=True)
        return Response(serializer2.data)


class write_message(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = request.headers.get('jwt')
        decoded_token = jwt.decode(token, secret, algorithm='ES512')
        userID = decoded_token['user_id']
        courseID  = serializer.validated_data['course_id']
        instance = Message()
        instance.user_id = userID
        instance.course_id = courseID
        instance.msg = serializer.validated_data['msg']
        instance.date_of_send = datetime.datetime.now()
        instance.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class see_message(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = request.headers.get('jwt')
        decoded_token = jwt.decode(token, secret, algorithm='ES512')
        #userID = decoded_token['user_id']
        courseID = serializer.validated_data['course_id']
        q1 = Message.objects.filter(course_id=courseID)
        q2 = q1.values("user_id", "msg", "date_of_send")
        serializer = SeeMessageSerializer(q2, many=True)
        return Response(serializer.data)

