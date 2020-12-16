from concurrent import futures
import grpc

from belms.lms_backend.protos import hw_file_pb2, hw_file_pb2_grpc


def run_file(hwID):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hw_file_pb2_grpc.HomeworkControllerStub(channel)
        answer_file = stub.HomeworkID(hw_file_pb2.FileRequest(hw_id=hwID))
        return answer_file.hw_url


def run_course(userID, courseID):
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = hw_file_pb2_grpc.HomeworkControllerStub(channel)
        validation = stub.Validation(hw_file_pb2.CourseRequest(user_id=userID, course_id=courseID))
        return validation.valid_user, validation.valid_course


def run_user(userID):
    with grpc.insecure_channel('localhost:50053') as channel:
        stub = hw_file_pb2_grpc.HomeworkControllerStub(channel)
        user_role = stub.Userrole(hw_file_pb2.UserRequest(user_id=userID))
        return user_role.role


