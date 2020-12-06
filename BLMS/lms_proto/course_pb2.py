from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
  name='lms_proto/course.proto',
  package='lms_proto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16lms_proto/course.proto\x12\tlms_proto\x1a\x1bgoogle/protobuf/empty.proto\"1\n\x06\x43CourseReply\x12\x11\n\tcourse_id\x18\x01 \x01(\t\x12\x14\n\x0c\x63course_title\x18\x02 \x01(\t\"\x13\n\x11\x43CourseListRequest\"*\n\x15\x43CourseRetrieveRequest\x12\x11\n\tcourse_id\x18\x01 \x01(\t2\xae\x02\n\x10\x43CourseController\x12;\n\x04Login\x12\x1c.lms_proto.CourseRequest\x1a\x11.lms_proto.CourseReply\"\x00\x30\x01\x12\x30\n\x06\x43reate\x12\x11.lms_proto.Course\x1a\x11.lms_proto.Course\"\x00\x12\x41\n\x08Retrieve\x12 .lms_proto.CourseRetrieveRequest\x1a\x11.lms_proto.Course\"\x00\x12\x30\n\x06Update\x12\x11.lms_proto.Course\x1a\x11.lms_proto.Course\"\x00\x12\x36\n\x07\x44\x65stroy\x12\x11.lms_proto.Course\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,
                ])


_COURSEREPLY = _descriptor.Descriptor(
  name='CourseReply',
  full_name='lms_proto.CourseReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='course_id', full_name='lms_proto.CourseReply.course_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='course_title', full_name='lms_proto.CourseReply.course_title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=115,
)


_COURSEREQUEST = _descriptor.Descriptor(
  name='CourseRequest',
  full_name='lms_proto.CourseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=136,
)


"""_COURSEREPLY = _descriptor.Descriptor(
  name='CourseReply',
  full_name='lms_proto.CourseReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='course_id', full_name='lms_proto.CourseReply.course_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=180,
)"""

DESCRIPTOR.message_types_by_name['CourseReply'] = _COURSEREPLY
DESCRIPTOR.message_types_by_name['CourseRequest'] = _COURSEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Course = _reflection.GeneratedProtocolMessageType('CourseReply', (_message.Message,), {
  'DESCRIPTOR': _COURSEREPLY,
  '__module__': 'lms_proto.course_pb2'
  # @@protoc_insertion_point(class_scope:lms_proto.Course)
  })
_sym_db.RegisterMessage(Course)

CourseRequest = _reflection.GeneratedProtocolMessageType('CourseRequest', (_message.Message,), {
  'DESCRIPTOR': _COURSEREQUEST,
  '__module__': 'lms_proto.course_pb2'
  # @@protoc_insertion_point(class_scope:lms_proto.CourseListRequest)
  })
_sym_db.RegisterMessage(CourseRequest)

"""CourseRetrieveRequest = _reflection.GeneratedProtocolMessageType('CourseRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR': _COURSERETRIEVEREQUEST,
  '__module__': 'lms_proto.course_pb2'
  # @@protoc_insertion_point(class_scope:lms_proto.CourseRetrieveRequest)
  })
_sym_db.RegisterMessage(CourseRetrieveRequest)"""


_COURSECONTROLLER = _descriptor.ServiceDescriptor(
  name='CourseController',
  full_name='lms_proto.CourseController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=183,
  serialized_end=485,
  methods=[
  _descriptor.MethodDescriptor(
    name='Login',
    full_name='lms_proto.CourseController.Login',
    index=0,
    containing_service=None,
    input_type=_COURSEREQUEST,
    output_type=_COURSEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  """_descriptor.MethodDescriptor(
    name='Create',
    full_name='lms_proto.CourseController.Create',
    index=1,
    containing_service=None,
    input_type=_COURSE,
    output_type=_COURSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='lms_proto.CourseController.Retrieve',
    index=2,
    containing_service=None,
    input_type=_COURSERETRIEVEREQUEST,
    output_type=_COURSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='lms_proto.CourseController.Update',
    index=3,
    containing_service=None,
    input_type=_COURSE,
    output_type=_COURSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Destroy',
    full_name='lms_proto.CourseController.Destroy',
    index=4,
    containing_service=None,
    input_type=_COURSE,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  )""",
])
_sym_db.RegisterServiceDescriptor(_COURSECONTROLLER)

DESCRIPTOR.services_by_name['CourseController'] = _COURSECONTROLLER

# @@protoc_insertion_point(module_scope)
