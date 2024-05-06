"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

_sym_db = _symbol_database.Default()
from ......modules.common.proto import (
    header_pb2 as modules_dot_common_dot_proto_dot_header__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/data/tools/smart_recorder/proto/smart_recorder_status.proto",
    package="apollo.data",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\nCmodules/data/tools/smart_recorder/proto/smart_recorder_status.proto\x12\x0bapollo.data\x1a!modules/common/proto/header.proto"\x89\x01\n\x13SmartRecorderStatus\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x124\n\x0frecording_state\x18\x02 \x01(\x0e2\x1b.apollo.data.RecordingState\x12\x15\n\rstate_message\x18\x03 \x01(\t*=\n\x0eRecordingState\x12\x0b\n\x07STOPPED\x10\x00\x12\r\n\tRECORDING\x10\x01\x12\x0f\n\x0bTERMINATING\x10\x02',
    dependencies=[modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR],
)
_RECORDINGSTATE = _descriptor.EnumDescriptor(
    name="RecordingState",
    full_name="apollo.data.RecordingState",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="STOPPED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="RECORDING",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TERMINATING",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=259,
    serialized_end=320,
)
_sym_db.RegisterEnumDescriptor(_RECORDINGSTATE)
RecordingState = enum_type_wrapper.EnumTypeWrapper(_RECORDINGSTATE)
STOPPED = 0
RECORDING = 1
TERMINATING = 2
_SMARTRECORDERSTATUS = _descriptor.Descriptor(
    name="SmartRecorderStatus",
    full_name="apollo.data.SmartRecorderStatus",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="header",
            full_name="apollo.data.SmartRecorderStatus.header",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="recording_state",
            full_name="apollo.data.SmartRecorderStatus.recording_state",
            index=1,
            number=2,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
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
            name="state_message",
            full_name="apollo.data.SmartRecorderStatus.state_message",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
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
    serialized_start=120,
    serialized_end=257,
)
_SMARTRECORDERSTATUS.fields_by_name[
    "header"
].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_SMARTRECORDERSTATUS.fields_by_name["recording_state"].enum_type = _RECORDINGSTATE
DESCRIPTOR.message_types_by_name["SmartRecorderStatus"] = _SMARTRECORDERSTATUS
DESCRIPTOR.enum_types_by_name["RecordingState"] = _RECORDINGSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
SmartRecorderStatus = _reflection.GeneratedProtocolMessageType(
    "SmartRecorderStatus",
    (_message.Message,),
    {
        "DESCRIPTOR": _SMARTRECORDERSTATUS,
        "__module__": "modules.data.tools.smart_recorder.proto.smart_recorder_status_pb2",
    },
)
_sym_db.RegisterMessage(SmartRecorderStatus)
