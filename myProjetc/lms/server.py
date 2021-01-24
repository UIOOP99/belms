import math
import sys
from lms.models import Assignment
from lms.serializer import RoleReqProtoSerializer, RoleResProtoSerializer, HwReqProtoSerializer, HwResProtoSerializer, \
    ValidReqProtoSerializer, ValidResProtoSerializer

sys.path.append("..")
from protos import hw_file_pb2_grpc
from django_grpc_framework import generics
import grpc
from concurrent import futures


#class HomeworkControllerServicer(generics.ModelService):


class HomeworkControllerServicer(hw_file_pb2_grpc.HomeworkControllerServicer):

    def HomeworkID(self, request, context):
        url_list = []
        url = "www.google.com"
        for index in range(len(request)):
            url_list.append(url)
        return url_list

    def Validation(self, request, context):
        return True

    def Userrole(self, request, context):
        if int(math.log10(context))+1 == 1:
            return "PROFESSOR"
        else:
            return "STUDENT"

    serializer_class = RoleResProtoSerializer


"""def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hw_file_pb2_grpc.add_HomeworkControllerServicer_to_server(HomeworkControllerServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
"""