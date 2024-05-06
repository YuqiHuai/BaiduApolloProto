"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/planning/proto/planning_semantic_map_config.proto",
    package="apollo.planning",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n9modules/planning/proto/planning_semantic_map_config.proto\x12\x0fapollo.planning"\xc8\x02\n\x19PlanningSemanticMapConfig\x12\x12\n\nresolution\x18\x01 \x01(\x01\x12\x0e\n\x06height\x18d \x01(\x05\x12\r\n\x05width\x18e \x01(\x05\x12\x11\n\tego_idx_x\x18f \x01(\x05\x12\x11\n\tego_idx_y\x18g \x01(\x05\x12\x1a\n\x12max_rand_delta_phi\x18h \x01(\x01\x12\x1e\n\x16max_ego_future_horizon\x18i \x01(\x01\x12\x1c\n\x14max_ego_past_horizon\x18j \x01(\x01\x12\x1e\n\x16max_obs_future_horizon\x18k \x01(\x01\x12\x1c\n\x14max_obs_past_horizon\x18l \x01(\x01\x12\x19\n\x10base_map_padding\x18\xc8\x01 \x01(\x05\x12\x1f\n\x16city_driving_max_speed\x18\xc9\x01 \x01(\x01',
)
_PLANNINGSEMANTICMAPCONFIG = _descriptor.Descriptor(
    name="PlanningSemanticMapConfig",
    full_name="apollo.planning.PlanningSemanticMapConfig",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="resolution",
            full_name="apollo.planning.PlanningSemanticMapConfig.resolution",
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
            name="height",
            full_name="apollo.planning.PlanningSemanticMapConfig.height",
            index=1,
            number=100,
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
            name="width",
            full_name="apollo.planning.PlanningSemanticMapConfig.width",
            index=2,
            number=101,
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
            name="ego_idx_x",
            full_name="apollo.planning.PlanningSemanticMapConfig.ego_idx_x",
            index=3,
            number=102,
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
            name="ego_idx_y",
            full_name="apollo.planning.PlanningSemanticMapConfig.ego_idx_y",
            index=4,
            number=103,
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
            name="max_rand_delta_phi",
            full_name="apollo.planning.PlanningSemanticMapConfig.max_rand_delta_phi",
            index=5,
            number=104,
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
            name="max_ego_future_horizon",
            full_name="apollo.planning.PlanningSemanticMapConfig.max_ego_future_horizon",
            index=6,
            number=105,
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
            name="max_ego_past_horizon",
            full_name="apollo.planning.PlanningSemanticMapConfig.max_ego_past_horizon",
            index=7,
            number=106,
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
            name="max_obs_future_horizon",
            full_name="apollo.planning.PlanningSemanticMapConfig.max_obs_future_horizon",
            index=8,
            number=107,
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
            name="max_obs_past_horizon",
            full_name="apollo.planning.PlanningSemanticMapConfig.max_obs_past_horizon",
            index=9,
            number=108,
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
            name="base_map_padding",
            full_name="apollo.planning.PlanningSemanticMapConfig.base_map_padding",
            index=10,
            number=200,
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
            name="city_driving_max_speed",
            full_name="apollo.planning.PlanningSemanticMapConfig.city_driving_max_speed",
            index=11,
            number=201,
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
    serialized_start=79,
    serialized_end=407,
)
DESCRIPTOR.message_types_by_name[
    "PlanningSemanticMapConfig"
] = _PLANNINGSEMANTICMAPCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
PlanningSemanticMapConfig = _reflection.GeneratedProtocolMessageType(
    "PlanningSemanticMapConfig",
    (_message.Message,),
    {
        "DESCRIPTOR": _PLANNINGSEMANTICMAPCONFIG,
        "__module__": "modules.planning.proto.planning_semantic_map_config_pb2",
    },
)
_sym_db.RegisterMessage(PlanningSemanticMapConfig)
