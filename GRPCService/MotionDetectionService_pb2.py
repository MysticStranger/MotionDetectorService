# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MotionDetectionService.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='MotionDetectionService.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1cMotionDetectionService.proto\"<\n\x16MotionDetectionRequest\x12\r\n\x05\x66iles\x18\x01 \x03(\x0c\x12\x13\n\x0b\x66ile_format\x18\x02 \x01(\t\"c\n\x17MotionDetectionResponse\x12\x10\n\x08\x61nalyzed\x18\x01 \x01(\x08\x12%\n\x06\x66rames\x18\x02 \x03(\x0b\x32\x15.MotionDetectionFrame\x12\x0f\n\x07message\x18\x03 \x01(\t\"<\n\x14MotionDetectionFrame\x12$\n\ndetections\x18\x01 \x03(\x0b\x32\x10.MotionDetection\"I\n\x0fMotionDetection\x12\x0c\n\x04xmin\x18\x01 \x01(\x02\x12\x0c\n\x04ymin\x18\x02 \x01(\x02\x12\x0c\n\x04xmax\x18\x03 \x01(\x02\x12\x0c\n\x04ymax\x18\x04 \x01(\x02\x32X\n\x16MotionDetectionService\x12>\n\x07\x41nalyze\x12\x17.MotionDetectionRequest\x1a\x18.MotionDetectionResponse\"\x00\x62\x06proto3'
)




_MOTIONDETECTIONREQUEST = _descriptor.Descriptor(
  name='MotionDetectionRequest',
  full_name='MotionDetectionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='files', full_name='MotionDetectionRequest.files', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_format', full_name='MotionDetectionRequest.file_format', index=1,
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
  serialized_start=32,
  serialized_end=92,
)


_MOTIONDETECTIONRESPONSE = _descriptor.Descriptor(
  name='MotionDetectionResponse',
  full_name='MotionDetectionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='analyzed', full_name='MotionDetectionResponse.analyzed', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frames', full_name='MotionDetectionResponse.frames', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='MotionDetectionResponse.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=94,
  serialized_end=193,
)


_MOTIONDETECTIONFRAME = _descriptor.Descriptor(
  name='MotionDetectionFrame',
  full_name='MotionDetectionFrame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='detections', full_name='MotionDetectionFrame.detections', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=195,
  serialized_end=255,
)


_MOTIONDETECTION = _descriptor.Descriptor(
  name='MotionDetection',
  full_name='MotionDetection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='xmin', full_name='MotionDetection.xmin', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ymin', full_name='MotionDetection.ymin', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='xmax', full_name='MotionDetection.xmax', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ymax', full_name='MotionDetection.ymax', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=257,
  serialized_end=330,
)

_MOTIONDETECTIONRESPONSE.fields_by_name['frames'].message_type = _MOTIONDETECTIONFRAME
_MOTIONDETECTIONFRAME.fields_by_name['detections'].message_type = _MOTIONDETECTION
DESCRIPTOR.message_types_by_name['MotionDetectionRequest'] = _MOTIONDETECTIONREQUEST
DESCRIPTOR.message_types_by_name['MotionDetectionResponse'] = _MOTIONDETECTIONRESPONSE
DESCRIPTOR.message_types_by_name['MotionDetectionFrame'] = _MOTIONDETECTIONFRAME
DESCRIPTOR.message_types_by_name['MotionDetection'] = _MOTIONDETECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MotionDetectionRequest = _reflection.GeneratedProtocolMessageType('MotionDetectionRequest', (_message.Message,), {
  'DESCRIPTOR' : _MOTIONDETECTIONREQUEST,
  '__module__' : 'MotionDetectionService_pb2'
  # @@protoc_insertion_point(class_scope:MotionDetectionRequest)
  })
_sym_db.RegisterMessage(MotionDetectionRequest)

MotionDetectionResponse = _reflection.GeneratedProtocolMessageType('MotionDetectionResponse', (_message.Message,), {
  'DESCRIPTOR' : _MOTIONDETECTIONRESPONSE,
  '__module__' : 'MotionDetectionService_pb2'
  # @@protoc_insertion_point(class_scope:MotionDetectionResponse)
  })
_sym_db.RegisterMessage(MotionDetectionResponse)

MotionDetectionFrame = _reflection.GeneratedProtocolMessageType('MotionDetectionFrame', (_message.Message,), {
  'DESCRIPTOR' : _MOTIONDETECTIONFRAME,
  '__module__' : 'MotionDetectionService_pb2'
  # @@protoc_insertion_point(class_scope:MotionDetectionFrame)
  })
_sym_db.RegisterMessage(MotionDetectionFrame)

MotionDetection = _reflection.GeneratedProtocolMessageType('MotionDetection', (_message.Message,), {
  'DESCRIPTOR' : _MOTIONDETECTION,
  '__module__' : 'MotionDetectionService_pb2'
  # @@protoc_insertion_point(class_scope:MotionDetection)
  })
_sym_db.RegisterMessage(MotionDetection)



_MOTIONDETECTIONSERVICE = _descriptor.ServiceDescriptor(
  name='MotionDetectionService',
  full_name='MotionDetectionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=332,
  serialized_end=420,
  methods=[
  _descriptor.MethodDescriptor(
    name='Analyze',
    full_name='MotionDetectionService.Analyze',
    index=0,
    containing_service=None,
    input_type=_MOTIONDETECTIONREQUEST,
    output_type=_MOTIONDETECTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MOTIONDETECTIONSERVICE)

DESCRIPTOR.services_by_name['MotionDetectionService'] = _MOTIONDETECTIONSERVICE

# @@protoc_insertion_point(module_scope)
