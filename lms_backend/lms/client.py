from concurrent import futures
import grpc

from belms.lms_backend.protos import hw_file_pb2, hw_file_pb2_grpc


def run_file(hwID):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hw_file_pb2_grpc.HomeworkControllerStub(channel)
        answer_file = stub.HomeworkID(hw_file_pb2.FileRequest(hw_id=hwID))
        return answer_file


def run_course(userID, courseID):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hw_file_pb2_grpc.HomeworkControllerStub(channel)
        validation = stub.Validation(hw_file_pb2.CourseRequest(user_id=userID, course_id=courseID))
        return validation

