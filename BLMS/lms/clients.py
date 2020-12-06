from concurrent import futures
import grpc

from BLMS.lms_proto import course_pb2, course_pb2_grpc


def run(user_id):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = course_pb2_grpc.CourseControllerStub(channel)
        response = stub.Login(course_pb2.CourseRequest(userID=user_id))
    channel.close()
    return response
