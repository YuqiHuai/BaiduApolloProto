"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/localization/proto/localization_config.proto",
    package="apollo.localization",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n4modules/localization/proto/localization_config.proto\x12\x13apollo.localization"\x94\x01\n\x12LocalizationConfig\x12X\n\x11localization_type\x18\x01 \x01(\x0e28.apollo.localization.LocalizationConfig.LocalizationType:\x03RTK"$\n\x10LocalizationType\x12\x07\n\x03RTK\x10\x00\x12\x07\n\x03MSF\x10\x01',
)
_LOCALIZATIONCONFIG_LOCALIZATIONTYPE = _descriptor.EnumDescriptor(
    name="LocalizationType",
    full_name="apollo.localization.LocalizationConfig.LocalizationType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="RTK",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=190,
    serialized_end=226,
)
_sym_db.RegisterEnumDescriptor(_LOCALIZATIONCONFIG_LOCALIZATIONTYPE)
_LOCALIZATIONCONFIG = _descriptor.Descriptor(
    name="LocalizationConfig",
    full_name="apollo.localization.LocalizationConfig",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="localization_type",
            full_name="apollo.localization.LocalizationConfig.localization_type",
            index=0,
            number=1,
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
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_LOCALIZATIONCONFIG_LOCALIZATIONTYPE],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=78,
    serialized_end=226,
)
_LOCALIZATIONCONFIG.fields_by_name[
    "localization_type"
].enum_type = _LOCALIZATIONCONFIG_LOCALIZATIONTYPE
_LOCALIZATIONCONFIG_LOCALIZATIONTYPE.containing_type = _LOCALIZATIONCONFIG
DESCRIPTOR.message_types_by_name["LocalizationConfig"] = _LOCALIZATIONCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
LocalizationConfig = _reflection.GeneratedProtocolMessageType(
    "LocalizationConfig",
    (_message.Message,),
    {
        "DESCRIPTOR": _LOCALIZATIONCONFIG,
        "__module__": "modules.localization.proto.localization_config_pb2",
    },
)
_sym_db.RegisterMessage(LocalizationConfig)
