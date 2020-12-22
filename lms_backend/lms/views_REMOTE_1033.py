from django.shortcuts import render
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
import jwt
import base64



# Create your views here.
secret  =  base64.b64decode('LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlHYk1CQUdCeXFHU000OUFnRUdCU3VCQkFBakE0R0dBQVFBdmRrYTFzcTBRd2h0QStieDFBVHVTSUEzT2oxOQpYMk0rVExzZDF3SlBGbTI0U05OUXFUWFBidFFLamhFemhsK2ZDNWExZ2ttRzNpaTJBcWt6MnRaTWUzVUFDb3JSCm1QZXh5blR0cFFSQWFKalhDOGpkRXNDU3UvMlMrblpBMmdBc25uNDBRQWxzaEpBZHMybmRYd1FBSjk5T2tXeTUKcEduRkQ2M042Vy84ODlZQW9acz0KLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0t')

class assignment_upload(APIView):
    permission_classes = [AllowAny]
    def post(self , request , format=None):
        serializer = AssignmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
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


class assignment_answer_upload(APIView):
    permission_classes = [AllowAny]
    def post(self , request , format=None):
        serializer = AssignmentAnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = Assignment()
        instance.user_id = request.auth.payload['Username']
        instance.course_id = serializer.validated_data['course_id']
        instance.file_id= serializer.validated_data['file_id']
        instance.description = serializer.validated_data['description']
        instance.date_of_upload = datetime.datetime.now()
        instance.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)

class assignments_list(APIView):
    def get(self , request , format=None):
        selected_course = request.query_params.get('course_id', None)
        q1 = Assignment_answer.objects.filter( course_id = selected_course)
        #serializer = WorkTimesSerializer(q2 , many=True)
        #return Response(serializer.data)

