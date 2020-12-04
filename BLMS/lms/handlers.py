from .services import CourseService
from lms_proto import course_pb2_grpc


def grpc_handlers(server):
    course_pb2_grpc.add_CourseControllerServicer_to_server(CourseService.as_servicer(), server)