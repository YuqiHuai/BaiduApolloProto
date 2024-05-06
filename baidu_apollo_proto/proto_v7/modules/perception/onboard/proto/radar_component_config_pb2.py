"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/perception/onboard/proto/radar_component_config.proto",
    package="apollo.perception.onboard",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n=modules/perception/onboard/proto/radar_component_config.proto\x12\x19apollo.perception.onboard"\x82\x02\n\x14RadarComponentConfig\x12\x12\n\nradar_name\x18\x01 \x01(\t\x12\x19\n\x11tf_child_frame_id\x18\x02 \x01(\t\x12\x1e\n\x16radar_forward_distance\x18\x03 \x01(\x01\x12!\n\x19radar_preprocessor_method\x18\x04 \x01(\t\x12\x1f\n\x17radar_perception_method\x18\x05 \x01(\t\x12\x1b\n\x13radar_pipeline_name\x18\x06 \x01(\t\x12\x1d\n\x15odometry_channel_name\x18\x07 \x01(\t\x12\x1b\n\x13output_channel_name\x18\x08 \x01(\t',
)
_RADARCOMPONENTCONFIG = _descriptor.Descriptor(
    name="RadarComponentConfig",
    full_name="apollo.perception.onboard.RadarComponentConfig",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="radar_name",
            full_name="apollo.perception.onboard.RadarComponentConfig.radar_name",
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
            name="tf_child_frame_id",
            full_name="apollo.perception.onboard.RadarComponentConfig.tf_child_frame_id",
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
            name="radar_forward_distance",
            full_name="apollo.perception.onboard.RadarComponentConfig.radar_forward_distance",
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
            name="radar_preprocessor_method",
            full_name="apollo.perception.onboard.RadarComponentConfig.radar_preprocessor_method",
            index=3,
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
            name="radar_perception_method",
            full_name="apollo.perception.onboard.RadarComponentConfig.radar_perception_method",
            index=4,
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
            name="radar_pipeline_name",
            full_name="apollo.perception.onboard.RadarComponentConfig.radar_pipeline_name",
            index=5,
            number=6,
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
            name="odometry_channel_name",
            full_name="apollo.perception.onboard.RadarComponentConfig.odometry_channel_name",
            index=6,
            number=7,
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
            name="output_channel_name",
            full_name="apollo.perception.onboard.RadarComponentConfig.output_channel_name",
            index=7,
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
    serialized_start=93,
    serialized_end=351,
)
DESCRIPTOR.message_types_by_name["RadarComponentConfig"] = _RADARCOMPONENTCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
RadarComponentConfig = _reflection.GeneratedProtocolMessageType(
    "RadarComponentConfig",
    (_message.Message,),
    {
        "DESCRIPTOR": _RADARCOMPONENTCONFIG,
        "__module__": "modules.perception.onboard.proto.radar_component_config_pb2",
    },
)
_sym_db.RegisterMessage(RadarComponentConfig)
