from ..protos import hw_file_pb2_grpc


class HomeworkControllerServicer(hw_file_pb2_grpc.HomeworkControllerServicer):
    def HomeworkID(self, request, context):
        url_list = []
        url = "www.google.com"
        for index in range(len(request)):
            url_list.append(url)
        return url

    def Validation(self, request, context):
        return True

    def Userrole(self, request, context):
        """if int(math.log10(context))+1 == 1:
            return "PROFESSOR"
        else:
            return "STUDENT"
            """
        return "PROFESSOR"


