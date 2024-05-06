"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from ....modules.common.proto import (
    drive_state_pb2 as modules_dot_common_dot_proto_dot_drive__state__pb2,
)
from ....modules.common.proto import (
    header_pb2 as modules_dot_common_dot_proto_dot_header__pb2,
)
from ....modules.control.proto import (
    input_debug_pb2 as modules_dot_control_dot_proto_dot_input__debug__pb2,
)
from ....modules.control.proto import (
    local_view_pb2 as modules_dot_control_dot_proto_dot_local__view__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/control/proto/preprocessor.proto",
    package="apollo.control",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b"\n(modules/control/proto/preprocessor.proto\x12\x0eapollo.control\x1a!modules/common/proto/header.proto\x1a&modules/common/proto/drive_state.proto\x1a'modules/control/proto/input_debug.proto\x1a&modules/control/proto/local_view.proto\"\x96\x02\n\x0cPreprocessor\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12-\n\nlocal_view\x18\x02 \x01(\x0b2\x19.apollo.control.LocalView\x122\n\rengage_advice\x18\x04 \x01(\x0b2\x1b.apollo.common.EngageAdvice\x12/\n\x0binput_debug\x18\x05 \x01(\x0b2\x1a.apollo.control.InputDebug\x12\x1f\n\x10received_pad_msg\x18\x06 \x01(\x08:\x05false\x12\x14\n\x05estop\x18\x07 \x01(\x08:\x05false\x12\x14\n\x0cestop_reason\x18\x08 \x01(\t",
    dependencies=[
        modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,
        modules_dot_common_dot_proto_dot_drive__state__pb2.DESCRIPTOR,
        modules_dot_control_dot_proto_dot_input__debug__pb2.DESCRIPTOR,
        modules_dot_control_dot_proto_dot_local__view__pb2.DESCRIPTOR,
    ],
)
_PREPROCESSOR = _descriptor.Descriptor(
    name="Preprocessor",
    full_name="apollo.control.Preprocessor",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="header",
            full_name="apollo.control.Preprocessor.header",
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
            name="local_view",
            full_name="apollo.control.Preprocessor.local_view",
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
        _descriptor.FieldDescriptor(
            name="engage_advice",
            full_name="apollo.control.Preprocessor.engage_advice",
            index=2,
            number=4,
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
            name="input_debug",
            full_name="apollo.control.Preprocessor.input_debug",
            index=3,
            number=5,
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
            name="received_pad_msg",
            full_name="apollo.control.Preprocessor.received_pad_msg",
            index=4,
            number=6,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=True,
            default_value=False,
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
            name="estop",
            full_name="apollo.control.Preprocessor.estop",
            index=5,
            number=7,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=True,
            default_value=False,
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
            name="estop_reason",
            full_name="apollo.control.Preprocessor.estop_reason",
            index=6,
            number=8,
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
    serialized_start=217,
    serialized_end=495,
)
_PREPROCESSOR.fields_by_name[
    "header"
].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_PREPROCESSOR.fields_by_name[
    "local_view"
].message_type = modules_dot_control_dot_proto_dot_local__view__pb2._LOCALVIEW
_PREPROCESSOR.fields_by_name[
    "engage_advice"
].message_type = modules_dot_common_dot_proto_dot_drive__state__pb2._ENGAGEADVICE
_PREPROCESSOR.fields_by_name[
    "input_debug"
].message_type = modules_dot_control_dot_proto_dot_input__debug__pb2._INPUTDEBUG
DESCRIPTOR.message_types_by_name["Preprocessor"] = _PREPROCESSOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
Preprocessor = _reflection.GeneratedProtocolMessageType(
    "Preprocessor",
    (_message.Message,),
    {
        "DESCRIPTOR": _PREPROCESSOR,
        "__module__": "modules.control.proto.preprocessor_pb2",
    },
)
_sym_db.RegisterMessage(Preprocessor)
