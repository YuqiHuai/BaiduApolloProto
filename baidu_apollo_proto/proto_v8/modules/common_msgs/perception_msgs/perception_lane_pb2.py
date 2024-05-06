"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from ....modules.common_msgs.basic_msgs import (
    header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2,
)
from ....modules.common_msgs.perception_msgs import (
    perception_camera_pb2 as modules_dot_common__msgs_dot_perception__msgs_dot_perception__camera__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/common_msgs/perception_msgs/perception_lane.proto",
    package="apollo.perception",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n9modules/common_msgs/perception_msgs/perception_lane.proto\x12\x11apollo.perception\x1a+modules/common_msgs/basic_msgs/header.proto\x1a;modules/common_msgs/perception_msgs/perception_camera.proto"\xa3\x02\n\x0fPerceptionLanes\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x14\n\x0csource_topic\x18\x02 \x01(\t\x12I\n\nerror_code\x18\x03 \x01(\x0e2).apollo.perception.camera.CameraErrorCode:\nERROR_NONE\x12E\n\x11camera_calibrator\x18\x04 \x01(\x0b2*.apollo.perception.camera.CameraCalibrator\x12A\n\x0fcamera_laneline\x18\x05 \x03(\x0b2(.apollo.perception.camera.CameraLaneLine',
    dependencies=[
        modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2.DESCRIPTOR,
        modules_dot_common__msgs_dot_perception__msgs_dot_perception__camera__pb2.DESCRIPTOR,
    ],
)
_PERCEPTIONLANES = _descriptor.Descriptor(
    name="PerceptionLanes",
    full_name="apollo.perception.PerceptionLanes",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="header",
            full_name="apollo.perception.PerceptionLanes.header",
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
            name="source_topic",
            full_name="apollo.perception.PerceptionLanes.source_topic",
            index=1,
            number=2,
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
        _descriptor.FieldDescriptor(
            name="error_code",
            full_name="apollo.perception.PerceptionLanes.error_code",
            index=2,
            number=3,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=True,
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
            name="camera_calibrator",
            full_name="apollo.perception.PerceptionLanes.camera_calibrator",
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
        _descriptor.FieldDescriptor(
            name="camera_laneline",
            full_name="apollo.perception.PerceptionLanes.camera_laneline",
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
    serialized_start=187,
    serialized_end=478,
)
_PERCEPTIONLANES.fields_by_name[
    "header"
].message_type = modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2._HEADER
_PERCEPTIONLANES.fields_by_name[
    "error_code"
].enum_type = (
    modules_dot_common__msgs_dot_perception__msgs_dot_perception__camera__pb2._CAMERAERRORCODE
)
_PERCEPTIONLANES.fields_by_name[
    "camera_calibrator"
].message_type = (
    modules_dot_common__msgs_dot_perception__msgs_dot_perception__camera__pb2._CAMERACALIBRATOR
)
_PERCEPTIONLANES.fields_by_name[
    "camera_laneline"
].message_type = (
    modules_dot_common__msgs_dot_perception__msgs_dot_perception__camera__pb2._CAMERALANELINE
)
DESCRIPTOR.message_types_by_name["PerceptionLanes"] = _PERCEPTIONLANES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
PerceptionLanes = _reflection.GeneratedProtocolMessageType(
    "PerceptionLanes",
    (_message.Message,),
    {
        "DESCRIPTOR": _PERCEPTIONLANES,
        "__module__": "modules.common_msgs.perception_msgs.perception_lane_pb2",
    },
)
_sym_db.RegisterMessage(PerceptionLanes)
