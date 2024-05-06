"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from ....modules.map.proto import (
    map_geometry_pb2 as modules_dot_map_dot_proto_dot_map__geometry__pb2,
)
from ....modules.map.proto import (
    map_id_pb2 as modules_dot_map_dot_proto_dot_map__id__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/map/proto/map_stop_sign.proto",
    package="apollo.hdmap",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n%modules/map/proto/map_stop_sign.proto\x12\x0capollo.hdmap\x1a\x1emodules/map/proto/map_id.proto\x1a$modules/map/proto/map_geometry.proto"\x82\x02\n\x08StopSign\x12\x1c\n\x02id\x18\x01 \x01(\x0b2\x10.apollo.hdmap.Id\x12&\n\tstop_line\x18\x02 \x03(\x0b2\x13.apollo.hdmap.Curve\x12$\n\noverlap_id\x18\x03 \x03(\x0b2\x10.apollo.hdmap.Id\x12-\n\x04type\x18\x04 \x01(\x0e2\x1f.apollo.hdmap.StopSign.StopType"[\n\x08StopType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07ONE_WAY\x10\x01\x12\x0b\n\x07TWO_WAY\x10\x02\x12\r\n\tTHREE_WAY\x10\x03\x12\x0c\n\x08FOUR_WAY\x10\x04\x12\x0b\n\x07ALL_WAY\x10\x05',
    dependencies=[
        modules_dot_map_dot_proto_dot_map__id__pb2.DESCRIPTOR,
        modules_dot_map_dot_proto_dot_map__geometry__pb2.DESCRIPTOR,
    ],
)
_STOPSIGN_STOPTYPE = _descriptor.EnumDescriptor(
    name="StopType",
    full_name="apollo.hdmap.StopSign.StopType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="UNKNOWN",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ONE_WAY",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TWO_WAY",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="THREE_WAY",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="FOUR_WAY",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ALL_WAY",
            index=5,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=293,
    serialized_end=384,
)
_sym_db.RegisterEnumDescriptor(_STOPSIGN_STOPTYPE)
_STOPSIGN = _descriptor.Descriptor(
    name="StopSign",
    full_name="apollo.hdmap.StopSign",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="apollo.hdmap.StopSign.id",
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
            name="stop_line",
            full_name="apollo.hdmap.StopSign.stop_line",
            index=1,
            number=2,
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
        _descriptor.FieldDescriptor(
            name="overlap_id",
            full_name="apollo.hdmap.StopSign.overlap_id",
            index=2,
            number=3,
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
        _descriptor.FieldDescriptor(
            name="type",
            full_name="apollo.hdmap.StopSign.type",
            index=3,
            number=4,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_STOPSIGN_STOPTYPE],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=126,
    serialized_end=384,
)
_STOPSIGN.fields_by_name[
    "id"
].message_type = modules_dot_map_dot_proto_dot_map__id__pb2._ID
_STOPSIGN.fields_by_name[
    "stop_line"
].message_type = modules_dot_map_dot_proto_dot_map__geometry__pb2._CURVE
_STOPSIGN.fields_by_name[
    "overlap_id"
].message_type = modules_dot_map_dot_proto_dot_map__id__pb2._ID
_STOPSIGN.fields_by_name["type"].enum_type = _STOPSIGN_STOPTYPE
_STOPSIGN_STOPTYPE.containing_type = _STOPSIGN
DESCRIPTOR.message_types_by_name["StopSign"] = _STOPSIGN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
StopSign = _reflection.GeneratedProtocolMessageType(
    "StopSign",
    (_message.Message,),
    {"DESCRIPTOR": _STOPSIGN, "__module__": "modules.map.proto.map_stop_sign_pb2"},
)
_sym_db.RegisterMessage(StopSign)
