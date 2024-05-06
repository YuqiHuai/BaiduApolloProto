"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/drivers/tools/image_decompress/proto/config.proto",
    package="apollo.image_decompress",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n9modules/drivers/tools/image_decompress/proto/config.proto\x12\x17apollo.image_decompress"\x1e\n\x06Config\x12\x14\n\x0cchannel_name\x18\x01 \x01(\t',
)
_CONFIG = _descriptor.Descriptor(
    name="Config",
    full_name="apollo.image_decompress.Config",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="channel_name",
            full_name="apollo.image_decompress.Config.channel_name",
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
    serialized_start=86,
    serialized_end=116,
)
DESCRIPTOR.message_types_by_name["Config"] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
Config = _reflection.GeneratedProtocolMessageType(
    "Config",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONFIG,
        "__module__": "modules.drivers.tools.image_decompress.proto.config_pb2",
    },
)
_sym_db.RegisterMessage(Config)
