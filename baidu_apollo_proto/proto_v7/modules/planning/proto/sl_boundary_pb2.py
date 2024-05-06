"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from ....modules.common.proto import (
    pnc_point_pb2 as modules_dot_common_dot_proto_dot_pnc__point__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/planning/proto/sl_boundary.proto",
    package="apollo.planning",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n(modules/planning/proto/sl_boundary.proto\x12\x0fapollo.planning\x1a$modules/common/proto/pnc_point.proto"|\n\nSLBoundary\x12\x0f\n\x07start_s\x18\x01 \x01(\x01\x12\r\n\x05end_s\x18\x02 \x01(\x01\x12\x0f\n\x07start_l\x18\x03 \x01(\x01\x12\r\n\x05end_l\x18\x04 \x01(\x01\x12.\n\x0eboundary_point\x18\x05 \x03(\x0b2\x16.apollo.common.SLPoint',
    dependencies=[modules_dot_common_dot_proto_dot_pnc__point__pb2.DESCRIPTOR],
)
_SLBOUNDARY = _descriptor.Descriptor(
    name="SLBoundary",
    full_name="apollo.planning.SLBoundary",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="start_s",
            full_name="apollo.planning.SLBoundary.start_s",
            index=0,
            number=1,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="end_s",
            full_name="apollo.planning.SLBoundary.end_s",
            index=1,
            number=2,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="start_l",
            full_name="apollo.planning.SLBoundary.start_l",
            index=2,
            number=3,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="end_l",
            full_name="apollo.planning.SLBoundary.end_l",
            index=3,
            number=4,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="boundary_point",
            full_name="apollo.planning.SLBoundary.boundary_point",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=99,
    serialized_end=223,
)
_SLBOUNDARY.fields_by_name[
    "boundary_point"
].message_type = modules_dot_common_dot_proto_dot_pnc__point__pb2._SLPOINT
DESCRIPTOR.message_types_by_name["SLBoundary"] = _SLBOUNDARY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
SLBoundary = _reflection.GeneratedProtocolMessageType(
    "SLBoundary",
    (_message.Message,),
    {"DESCRIPTOR": _SLBOUNDARY, "__module__": "modules.planning.proto.sl_boundary_pb2"},
)
_sym_db.RegisterMessage(SLBoundary)
