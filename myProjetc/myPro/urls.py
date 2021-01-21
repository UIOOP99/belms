import grpc
from concurrent import futures
from protos import hw_file_pb2_grpc, hw_file_pb2

from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

from protos import hw_file_pb2_grpc
from lms.server import HomeworkControllerServicer


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/token', obtain_jwt_token),
    path('lms/', include('lms.urls')),

]


def grpc_handlers(server):
    #server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hw_file_pb2_grpc.add_HomeworkControllerServicer_to_server(HomeworkControllerServicer(), server)

"""def grpc_handlers(server):
    hw_file_pb2_grpc.add_HomeworkControllerServicer_to_server(HomeworkControllerServicer.Userrole(), server)
    hw_file_pb2_grpc.add_HomeworkControllerServicer_to_server(HomeworkControllerServicer.Validation(), server)
    hw_file_pb2_grpc.add_HomeworkControllerServicer_to_server(HomeworkControllerServicer.HomeworkID(), server)
"""
