import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import course_pb2 as lms__proto_dot_course__pb2


class CourseControllerStub(object):

    def __init__(self, channel):
        self.Login = channel.unary_stream(
                '/lms_proto.CourseController/Login',
                request_serializer=lms__proto_dot_course__pb2.CourseRequest.SerializeToString,
                response_deserializer=lms__proto_dot_course__pb2.CourseReply.FromString,
                )
        """self.Create = channel.unary_unary(
                '/lms_proto.CourseController/Create',
                request_serializer=lms__proto_dot_course__pb2.Course.SerializeToString,
                response_deserializer=lms__proto_dot_course__pb2.Course.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/lms_proto.CourseController/Retrieve',
                request_serializer=lms__proto_dot_course__pb2.CourseRetrieveRequest.SerializeToString,
                response_deserializer=lms__proto_dot_course__pb2.Course.FromString,
                )
        self.Update = channel.unary_unary(
                '/lms_proto.CourseController/Update',
                request_serializer=lms__proto_dot_course__pb2.Course.SerializeToString,
                response_deserializer=lms__proto_dot_course__pb2.Course.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/lms_proto.CourseController/Destroy',
                request_serializer=lms__proto_dot_course__pb2.Course.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )"""


class CourseControllerServicer(object):

    def Login(self, request, context):
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    """def Create(self, request, context):
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')"""


def add_CourseControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Login': grpc.unary_stream_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=lms__proto_dot_course__pb2.CourseRequest.FromString,
                    response_serializer=lms__proto_dot_course__pb2.CourseReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'lms_proto.CourseController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


"""
inside the dictionary
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=lms__proto_dot_course__pb2.Course.FromString,
                    response_serializer=lms__proto_dot_course__pb2.Course.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=lms__proto_dot_course__pb2.CourseRetrieveRequest.FromString,
                    response_serializer=lms__proto_dot_course__pb2.Course.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=lms__proto_dot_course__pb2.Course.FromString,
                    response_serializer=lms__proto_dot_course__pb2.Course.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=lms__proto_dot_course__pb2.Course.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),"""


# This class is part of an EXPERIMENTAL API.
class CourseController(object):

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/lms_proto.CourseController/Login',
            lms__proto_dot_course__pb2.CourseRequest.SerializeToString,
            lms__proto_dot_course__pb2.Course.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    """@staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/lms_proto.CourseController/Create',
            lms__proto_dot_course__pb2.Course.SerializeToString,
            lms__proto_dot_course__pb2.Course.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/lms_proto.CourseController/Retrieve',
            lms__proto_dot_course__pb2.CourseRetrieveRequest.SerializeToString,
            lms__proto_dot_course__pb2.Course.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/lms_proto.CourseController/Update',
            lms__proto_dot_course__pb2.Course.SerializeToString,
            lms__proto_dot_course__pb2.Course.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Destroy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/lms_proto.CourseController/Destroy',
            lms__proto_dot_course__pb2.Course.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)"""

