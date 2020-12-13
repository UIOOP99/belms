from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import AssignmentSerializer, AssignmentAnswerSerializer
from .models import Assignment, Assignment_answer
import datetime
from rest_framework import  status
from rest_framework.permissions import BasePermission, AllowAny, SAFE_METHODS

from belms.lms_backend.lms import client


class assignment_upload(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = AssignmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        userID = request.auth.payload['Username']
        courseID = serializer.validated_data['course_id']

        is_valid = client.run_course(userID, courseID)
        if is_valid[0] and is_valid[1]:
            instance = Assignment()
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


class assignment_answer_upload(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = AssignmentAnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        userID = request.auth.payload['Username']
        courseID = serializer.validated_data['course_id']

        is_valid = client.run_course(userID, courseID)
        if is_valid[0] and is_valid[1]:
            instance = Assignment_answer()
            instance.user_id = request.auth.payload['Username']
            instance.course_id = serializer.validated_data['course_id']
            instance.file_id = serializer.validated_data['file_id']
            instance.homework_number_id = serializer.validated_data['homework_number_id']
            instance.description = serializer.validated_data['description']
            instance.date_of_upload = datetime.datetime.now()
            instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


"""class assignments_list(APIView):
    def get(self , request , format=None):
        selected_course = request.query_params.get('course_id', None)
        q1 = Assignment_answer.objects.filter( course_id = selected_course)
        #serializer = WorkTimesSerializer(q2 , many=True)
        #return Response(serializer.data)"""


class assignments_homeworklist(APIView):
    def get(self, request, format=None):
        selected_course = request.query_params.get('course_id', None)
        q1 = Assignment.objects.filter(course_id=selected_course)
        serializer = AssignmentSerializer(q1, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
class assignment_download(APIView):
    def download_hw(self, request):
        answer_urls = []
        if request.method == 'POST':
            selected_course = request.query_params.get('course_id', None)
            selected_homework = request.query_params.get('homework_number_id', None)
            q1 = Assignment_answer.objects.get(course_id=selected_course,
                                               homework_number_id=selected_homework,
                                               id=3)
            student_id = Assignment_answer.objects.get(course_id=selected_course,
                                                       homework_number_id=selected_homework,
                                                       id=1)
            for index in q1:
                answer_urls.append(client.run_file(q1[index]))
                answer_urls.append(student_id[index])
        elif request.method == 'GET':
            serializer = AssignmentAnswerSerializer(answer_urls, many=True)
            return Response(serializer.data)
