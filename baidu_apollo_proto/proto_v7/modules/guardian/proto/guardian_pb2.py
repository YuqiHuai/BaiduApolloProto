"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from ....modules.common.proto import (
    header_pb2 as modules_dot_common_dot_proto_dot_header__pb2,
)
from ....modules.control.proto import (
    control_cmd_pb2 as modules_dot_control_dot_proto_dot_control__cmd__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/guardian/proto/guardian.proto",
    package="apollo.guardian",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b"\n%modules/guardian/proto/guardian.proto\x12\x0fapollo.guardian\x1a!modules/common/proto/header.proto\x1a'modules/control/proto/control_cmd.proto\"q\n\x0fGuardianCommand\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x127\n\x0fcontrol_command\x18\x02 \x01(\x0b2\x1e.apollo.control.ControlCommand",
    dependencies=[
        modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,
        modules_dot_control_dot_proto_dot_control__cmd__pb2.DESCRIPTOR,
    ],
)
_GUARDIANCOMMAND = _descriptor.Descriptor(
    name="GuardianCommand",
    full_name="apollo.guardian.GuardianCommand",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="header",
            full_name="apollo.guardian.GuardianCommand.header",
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
            name="control_command",
            full_name="apollo.guardian.GuardianCommand.control_command",
            index=1,
            number=2,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=134,
    serialized_end=247,
)
_GUARDIANCOMMAND.fields_by_name[
    "header"
].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_GUARDIANCOMMAND.fields_by_name[
    "control_command"
].message_type = modules_dot_control_dot_proto_dot_control__cmd__pb2._CONTROLCOMMAND
DESCRIPTOR.message_types_by_name["GuardianCommand"] = _GUARDIANCOMMAND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
GuardianCommand = _reflection.GeneratedProtocolMessageType(
    "GuardianCommand",
    (_message.Message,),
    {
        "DESCRIPTOR": _GUARDIANCOMMAND,
        "__module__": "modules.guardian.proto.guardian_pb2",
    },
)
_sym_db.RegisterMessage(GuardianCommand)
