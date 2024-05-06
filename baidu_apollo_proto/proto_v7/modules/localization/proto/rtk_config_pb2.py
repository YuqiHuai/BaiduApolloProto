"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/localization/proto/rtk_config.proto",
    package="apollo.localization.rtk_config",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n+modules/localization/proto/rtk_config.proto\x12\x1eapollo.localization.rtk_config"\xcd\x02\n\x06Config\x12\x1a\n\x12localization_topic\x18\x01 \x01(\t\x12!\n\x19localization_status_topic\x18\x0b \x01(\t\x12\x11\n\timu_topic\x18\x02 \x01(\t\x12\x11\n\tgps_topic\x18\x03 \x01(\t\x12\x18\n\x10gps_status_topic\x18\x0c \x01(\t\x12\x1d\n\x15broadcast_tf_frame_id\x18\x04 \x01(\t\x12#\n\x1bbroadcast_tf_child_frame_id\x18\x05 \x01(\t\x12\x19\n\x11imu_list_max_size\x18\x06 \x01(\x05\x12#\n\x1bgps_imu_time_diff_threshold\x18\x07 \x01(\x01\x12\x14\n\x0cmap_offset_x\x18\x08 \x01(\x01\x12\x14\n\x0cmap_offset_y\x18\t \x01(\x01\x12\x14\n\x0cmap_offset_z\x18\n \x01(\x01',
)
_CONFIG = _descriptor.Descriptor(
    name="Config",
    full_name="apollo.localization.rtk_config.Config",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="localization_topic",
            full_name="apollo.localization.rtk_config.Config.localization_topic",
            index=0,
            number=1,
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
            name="localization_status_topic",
            full_name="apollo.localization.rtk_config.Config.localization_status_topic",
            index=1,
            number=11,
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
            name="imu_topic",
            full_name="apollo.localization.rtk_config.Config.imu_topic",
            index=2,
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
            name="gps_topic",
            full_name="apollo.localization.rtk_config.Config.gps_topic",
            index=3,
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
        _descriptor.FieldDescriptor(
            name="gps_status_topic",
            full_name="apollo.localization.rtk_config.Config.gps_status_topic",
            index=4,
            number=12,
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
            name="broadcast_tf_frame_id",
            full_name="apollo.localization.rtk_config.Config.broadcast_tf_frame_id",
            index=5,
            number=4,
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
            name="broadcast_tf_child_frame_id",
            full_name="apollo.localization.rtk_config.Config.broadcast_tf_child_frame_id",
            index=6,
            number=5,
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
            name="imu_list_max_size",
            full_name="apollo.localization.rtk_config.Config.imu_list_max_size",
            index=7,
            number=6,
            type=5,
            cpp_type=1,
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
            name="gps_imu_time_diff_threshold",
            full_name="apollo.localization.rtk_config.Config.gps_imu_time_diff_threshold",
            index=8,
            number=7,
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
            name="map_offset_x",
            full_name="apollo.localization.rtk_config.Config.map_offset_x",
            index=9,
            number=8,
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
            name="map_offset_y",
            full_name="apollo.localization.rtk_config.Config.map_offset_y",
            index=10,
            number=9,
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
            name="map_offset_z",
            full_name="apollo.localization.rtk_config.Config.map_offset_z",
            index=11,
            number=10,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=80,
    serialized_end=413,
)
DESCRIPTOR.message_types_by_name["Config"] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
Config = _reflection.GeneratedProtocolMessageType(
    "Config",
    (_message.Message,),
    {"DESCRIPTOR": _CONFIG, "__module__": "modules.localization.proto.rtk_config_pb2"},
)
_sym_db.RegisterMessage(Config)
