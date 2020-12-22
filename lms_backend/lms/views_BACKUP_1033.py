from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import AssignmentSerializer, AssignmentAnswerSerializer
from .models import Assignment, Assignment_answer
import datetime
from rest_framework import status
from rest_framework.permissions import BasePermission, AllowAny, SAFE_METHODS
import jwt
import base64

from belms.lms_backend.lms import client


<<<<<<< HEAD
=======
# Create your views here.
secret  =  base64.b64decode('LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlHYk1CQUdCeXFHU000OUFnRUdCU3VCQkFBakE0R0dBQVFBdmRrYTFzcTBRd2h0QStieDFBVHVTSUEzT2oxOQpYMk0rVExzZDF3SlBGbTI0U05OUXFUWFBidFFLamhFemhsK2ZDNWExZ2ttRzNpaTJBcWt6MnRaTWUzVUFDb3JSCm1QZXh5blR0cFFSQWFKalhDOGpkRXNDU3UvMlMrblpBMmdBc25uNDBRQWxzaEpBZHMybmRYd1FBSjk5T2tXeTUKcEduRkQ2M042Vy84ODlZQW9acz0KLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0t')

>>>>>>> negin
class assignment_upload(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = AssignmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
<<<<<<< HEAD
        userID = request.auth.payload['Username']
        courseID = serializer.validated_data['course_id']

        role = client.run_user(userID)
        if role == "PROFESSOR":
            valid_course = client.run_course(userID, courseID)
            if valid_course:
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
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
=======
        instance = Assignment()
        token = request.headers.get('jwt')
        decoded_token = jwt.decode(token, secret, algorithm='ES512')
        instance.user_id = decoded_token['user_id']
        instance.course_id = serializer.validated_data['course_id']
        instance.file_id= serializer.validated_data['file_id']
        instance.description = serializer.validated_data['description']
        instance.start_date = datetime.datetime.now()
        instance.deadline = serializer.validated_data['deadline']
        instance.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)
>>>>>>> negin


class assignment_answer_upload(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = AssignmentAnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        userID = request.auth.payload['Username']
        courseID = serializer.validated_data['course_id']

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
        result = []
        if request.method == 'POST':
            selected_course = request.query_params.get('course_id', None)
            selected_homework = request.query_params.get('homework_number_id', None)
            q1 = Assignment_answer.objects.get(course_id=selected_course,
                                               homework_number_id=selected_homework).values("File_id")
            student_id = Assignment_answer.objects.get(course_id=selected_course,
                                                       homework_number_id=selected_homework).values("user_id")
            answer_urls = client.run_file(q1)
            for i in range(len(answer_urls)):
                result.append(student_id[i])
                result.append(answer_urls[i])
        elif request.method == 'GET':
            serializer = AssignmentAnswerSerializer(result, many=True)
            return Response(serializer.data)
