"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from ....modules.common_msgs.basic_msgs import (
    header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/common_msgs/control_msgs/input_debug.proto",
    package="apollo.control",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n2modules/common_msgs/control_msgs/input_debug.proto\x12\x0eapollo.control\x1a+modules/common_msgs/basic_msgs/header.proto"\xe0\x01\n\nInputDebug\x122\n\x13localization_header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12,\n\rcanbus_header\x18\x02 \x01(\x0b2\x15.apollo.common.Header\x120\n\x11trajectory_header\x18\x03 \x01(\x0b2\x15.apollo.common.Header\x12>\n\x1flatest_replan_trajectory_header\x18\x04 \x01(\x0b2\x15.apollo.common.Header',
    dependencies=[modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2.DESCRIPTOR],
)
_INPUTDEBUG = _descriptor.Descriptor(
    name="InputDebug",
    full_name="apollo.control.InputDebug",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="localization_header",
            full_name="apollo.control.InputDebug.localization_header",
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
            name="canbus_header",
            full_name="apollo.control.InputDebug.canbus_header",
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
            name="trajectory_header",
            full_name="apollo.control.InputDebug.trajectory_header",
            index=2,
            number=3,
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
            name="latest_replan_trajectory_header",
            full_name="apollo.control.InputDebug.latest_replan_trajectory_header",
            index=3,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=116,
    serialized_end=340,
)
_INPUTDEBUG.fields_by_name[
    "localization_header"
].message_type = modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2._HEADER
_INPUTDEBUG.fields_by_name[
    "canbus_header"
].message_type = modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2._HEADER
_INPUTDEBUG.fields_by_name[
    "trajectory_header"
].message_type = modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2._HEADER
_INPUTDEBUG.fields_by_name[
    "latest_replan_trajectory_header"
].message_type = modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2._HEADER
DESCRIPTOR.message_types_by_name["InputDebug"] = _INPUTDEBUG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
InputDebug = _reflection.GeneratedProtocolMessageType(
    "InputDebug",
    (_message.Message,),
    {
        "DESCRIPTOR": _INPUTDEBUG,
        "__module__": "modules.common_msgs.control_msgs.input_debug_pb2",
    },
)
_sym_db.RegisterMessage(InputDebug)