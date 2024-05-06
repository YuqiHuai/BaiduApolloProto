"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/common/vehicle_model/proto/vehicle_model_config.proto",
    package="apollo.common",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n=modules/common/vehicle_model/proto/vehicle_model_config.proto\x12\rapollo.common"\xab\x03\n\x12VehicleModelConfig\x12?\n\nmodel_type\x18\x01 \x01(\x0e2+.apollo.common.VehicleModelConfig.ModelType\x12Z\n\x1arc_kinematic_bicycle_model\x18\x02 \x01(\x0b26.apollo.common.RearCenteredKinematicBicycleModelConfig\x12W\n\x1acomc_dynamic_bicycle_model\x18\x03 \x01(\x0b23.apollo.common.ComCenteredDynamicBicycleModelConfig\x120\n\tmlp_model\x18\x04 \x01(\x0b2\x1d.apollo.common.MlpModelConfig"m\n\tModelType\x12)\n%REAR_CENTERED_KINEMATIC_BICYCLE_MODEL\x10\x00\x12&\n"COM_CENTERED_DYNAMIC_BICYCLE_MODEL\x10\x01\x12\r\n\tMLP_MODEL\x10\x02"5\n\'RearCenteredKinematicBicycleModelConfig\x12\n\n\x02dt\x18\x01 \x01(\x01"2\n$ComCenteredDynamicBicycleModelConfig\x12\n\n\x02dt\x18\x01 \x01(\x01"\x1c\n\x0eMlpModelConfig\x12\n\n\x02dt\x18\x01 \x01(\x01',
)
_VEHICLEMODELCONFIG_MODELTYPE = _descriptor.EnumDescriptor(
    name="ModelType",
    full_name="apollo.common.VehicleModelConfig.ModelType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="REAR_CENTERED_KINEMATIC_BICYCLE_MODEL",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="COM_CENTERED_DYNAMIC_BICYCLE_MODEL",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MLP_MODEL",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=399,
    serialized_end=508,
)
_sym_db.RegisterEnumDescriptor(_VEHICLEMODELCONFIG_MODELTYPE)
_VEHICLEMODELCONFIG = _descriptor.Descriptor(
    name="VehicleModelConfig",
    full_name="apollo.common.VehicleModelConfig",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="model_type",
            full_name="apollo.common.VehicleModelConfig.model_type",
            index=0,
            number=1,
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
            name="rc_kinematic_bicycle_model",
            full_name="apollo.common.VehicleModelConfig.rc_kinematic_bicycle_model",
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
            name="comc_dynamic_bicycle_model",
            full_name="apollo.common.VehicleModelConfig.comc_dynamic_bicycle_model",
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
            name="mlp_model",
            full_name="apollo.common.VehicleModelConfig.mlp_model",
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
    enum_types=[_VEHICLEMODELCONFIG_MODELTYPE],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=81,
    serialized_end=508,
)
_REARCENTEREDKINEMATICBICYCLEMODELCONFIG = _descriptor.Descriptor(
    name="RearCenteredKinematicBicycleModelConfig",
    full_name="apollo.common.RearCenteredKinematicBicycleModelConfig",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="dt",
            full_name="apollo.common.RearCenteredKinematicBicycleModelConfig.dt",
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
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=510,
    serialized_end=563,
)
_COMCENTEREDDYNAMICBICYCLEMODELCONFIG = _descriptor.Descriptor(
    name="ComCenteredDynamicBicycleModelConfig",
    full_name="apollo.common.ComCenteredDynamicBicycleModelConfig",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="dt",
            full_name="apollo.common.ComCenteredDynamicBicycleModelConfig.dt",
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
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=565,
    serialized_end=615,
)
_MLPMODELCONFIG = _descriptor.Descriptor(
    name="MlpModelConfig",
    full_name="apollo.common.MlpModelConfig",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="dt",
            full_name="apollo.common.MlpModelConfig.dt",
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
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=617,
    serialized_end=645,
)
_VEHICLEMODELCONFIG.fields_by_name[
    "model_type"
].enum_type = _VEHICLEMODELCONFIG_MODELTYPE
_VEHICLEMODELCONFIG.fields_by_name[
    "rc_kinematic_bicycle_model"
].message_type = _REARCENTEREDKINEMATICBICYCLEMODELCONFIG
_VEHICLEMODELCONFIG.fields_by_name[
    "comc_dynamic_bicycle_model"
].message_type = _COMCENTEREDDYNAMICBICYCLEMODELCONFIG
_VEHICLEMODELCONFIG.fields_by_name["mlp_model"].message_type = _MLPMODELCONFIG
_VEHICLEMODELCONFIG_MODELTYPE.containing_type = _VEHICLEMODELCONFIG
DESCRIPTOR.message_types_by_name["VehicleModelConfig"] = _VEHICLEMODELCONFIG
DESCRIPTOR.message_types_by_name[
    "RearCenteredKinematicBicycleModelConfig"
] = _REARCENTEREDKINEMATICBICYCLEMODELCONFIG
DESCRIPTOR.message_types_by_name[
    "ComCenteredDynamicBicycleModelConfig"
] = _COMCENTEREDDYNAMICBICYCLEMODELCONFIG
DESCRIPTOR.message_types_by_name["MlpModelConfig"] = _MLPMODELCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
VehicleModelConfig = _reflection.GeneratedProtocolMessageType(
    "VehicleModelConfig",
    (_message.Message,),
    {
        "DESCRIPTOR": _VEHICLEMODELCONFIG,
        "__module__": "modules.common.vehicle_model.proto.vehicle_model_config_pb2",
    },
)
_sym_db.RegisterMessage(VehicleModelConfig)
RearCenteredKinematicBicycleModelConfig = _reflection.GeneratedProtocolMessageType(
    "RearCenteredKinematicBicycleModelConfig",
    (_message.Message,),
    {
        "DESCRIPTOR": _REARCENTEREDKINEMATICBICYCLEMODELCONFIG,
        "__module__": "modules.common.vehicle_model.proto.vehicle_model_config_pb2",
    },
)
_sym_db.RegisterMessage(RearCenteredKinematicBicycleModelConfig)
ComCenteredDynamicBicycleModelConfig = _reflection.GeneratedProtocolMessageType(
    "ComCenteredDynamicBicycleModelConfig",
    (_message.Message,),
    {
        "DESCRIPTOR": _COMCENTEREDDYNAMICBICYCLEMODELCONFIG,
        "__module__": "modules.common.vehicle_model.proto.vehicle_model_config_pb2",
    },
)
_sym_db.RegisterMessage(ComCenteredDynamicBicycleModelConfig)
MlpModelConfig = _reflection.GeneratedProtocolMessageType(
    "MlpModelConfig",
    (_message.Message,),
    {
        "DESCRIPTOR": _MLPMODELCONFIG,
        "__module__": "modules.common.vehicle_model.proto.vehicle_model_config_pb2",
    },
)
_sym_db.RegisterMessage(MlpModelConfig)
