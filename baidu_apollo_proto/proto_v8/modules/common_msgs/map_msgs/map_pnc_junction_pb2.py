"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from ....modules.common_msgs.map_msgs import (
    map_geometry_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__geometry__pb2,
)
from ....modules.common_msgs.map_msgs import (
    map_id_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__id__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/common_msgs/map_msgs/map_pnc_junction.proto",
    package="apollo.hdmap",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n3modules/common_msgs/map_msgs/map_pnc_junction.proto\x12\x0capollo.hdmap\x1a/modules/common_msgs/map_msgs/map_geometry.proto\x1a)modules/common_msgs/map_msgs/map_id.proto"\x92\x02\n\x07Passage\x12\x1c\n\x02id\x18\x01 \x01(\x0b2\x10.apollo.hdmap.Id\x12#\n\tsignal_id\x18\x02 \x03(\x0b2\x10.apollo.hdmap.Id\x12"\n\x08yield_id\x18\x03 \x03(\x0b2\x10.apollo.hdmap.Id\x12&\n\x0cstop_sign_id\x18\x04 \x03(\x0b2\x10.apollo.hdmap.Id\x12!\n\x07lane_id\x18\x05 \x03(\x0b2\x10.apollo.hdmap.Id\x12(\n\x04type\x18\x06 \x01(\x0e2\x1a.apollo.hdmap.Passage.Type"+\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08ENTRANCE\x10\x01\x12\x08\n\x04EXIT\x10\x02"T\n\x0cPassageGroup\x12\x1c\n\x02id\x18\x01 \x01(\x0b2\x10.apollo.hdmap.Id\x12&\n\x07passage\x18\x02 \x03(\x0b2\x15.apollo.hdmap.Passage"\xac\x01\n\x0bPNCJunction\x12\x1c\n\x02id\x18\x01 \x01(\x0b2\x10.apollo.hdmap.Id\x12&\n\x07polygon\x18\x02 \x01(\x0b2\x15.apollo.hdmap.Polygon\x12$\n\noverlap_id\x18\x03 \x03(\x0b2\x10.apollo.hdmap.Id\x121\n\rpassage_group\x18\x04 \x03(\x0b2\x1a.apollo.hdmap.PassageGroup',
    dependencies=[
        modules_dot_common__msgs_dot_map__msgs_dot_map__geometry__pb2.DESCRIPTOR,
        modules_dot_common__msgs_dot_map__msgs_dot_map__id__pb2.DESCRIPTOR,
    ],
)
_PASSAGE_TYPE = _descriptor.EnumDescriptor(
    name="Type",
    full_name="apollo.hdmap.Passage.Type",
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
            name="ENTRANCE",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="EXIT",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=393,
    serialized_end=436,
)
_sym_db.RegisterEnumDescriptor(_PASSAGE_TYPE)
_PASSAGE = _descriptor.Descriptor(
    name="Passage",
    full_name="apollo.hdmap.Passage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="apollo.hdmap.Passage.id",
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
            name="signal_id",
            full_name="apollo.hdmap.Passage.signal_id",
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
            name="yield_id",
            full_name="apollo.hdmap.Passage.yield_id",
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
            name="stop_sign_id",
            full_name="apollo.hdmap.Passage.stop_sign_id",
            index=3,
            number=4,
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
            name="lane_id",
            full_name="apollo.hdmap.Passage.lane_id",
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
        _descriptor.FieldDescriptor(
            name="type",
            full_name="apollo.hdmap.Passage.type",
            index=5,
            number=6,
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
    enum_types=[_PASSAGE_TYPE],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=162,
    serialized_end=436,
)
_PASSAGEGROUP = _descriptor.Descriptor(
    name="PassageGroup",
    full_name="apollo.hdmap.PassageGroup",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="apollo.hdmap.PassageGroup.id",
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
            name="passage",
            full_name="apollo.hdmap.PassageGroup.passage",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=438,
    serialized_end=522,
)
_PNCJUNCTION = _descriptor.Descriptor(
    name="PNCJunction",
    full_name="apollo.hdmap.PNCJunction",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="apollo.hdmap.PNCJunction.id",
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
            name="polygon",
            full_name="apollo.hdmap.PNCJunction.polygon",
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
            name="overlap_id",
            full_name="apollo.hdmap.PNCJunction.overlap_id",
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
            name="passage_group",
            full_name="apollo.hdmap.PNCJunction.passage_group",
            index=3,
            number=4,
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
    serialized_start=525,
    serialized_end=697,
)
_PASSAGE.fields_by_name[
    "id"
].message_type = modules_dot_common__msgs_dot_map__msgs_dot_map__id__pb2._ID
_PASSAGE.fields_by_name[
    "signal_id"
].message_type = modules_dot_common__msgs_dot_map__msgs_dot_map__id__pb2._ID
_PASSAGE.fields_by_name[
    "yield_id"
].message_type = modules_dot_common__msgs_dot_map__msgs_dot_map__id__pb2._ID
_PASSAGE.fields_by_name[
    "stop_sign_id"
].message_type = modules_dot_common__msgs_dot_map__msgs_dot_map__id__pb2._ID
_PASSAGE.fields_by_name[
    "lane_id"
].message_type = modules_dot_common__msgs_dot_map__msgs_dot_map__id__pb2._ID
_PASSAGE.fields_by_name["type"].enum_type = _PASSAGE_TYPE
_PASSAGE_TYPE.containing_type = _PASSAGE
_PASSAGEGROUP.fields_by_name[
    "id"
].message_type = modules_dot_common__msgs_dot_map__msgs_dot_map__id__pb2._ID
_PASSAGEGROUP.fields_by_name["passage"].message_type = _PASSAGE
_PNCJUNCTION.fields_by_name[
    "id"
].message_type = modules_dot_common__msgs_dot_map__msgs_dot_map__id__pb2._ID
_PNCJUNCTION.fields_by_name[
    "polygon"
].message_type = modules_dot_common__msgs_dot_map__msgs_dot_map__geometry__pb2._POLYGON
_PNCJUNCTION.fields_by_name[
    "overlap_id"
].message_type = modules_dot_common__msgs_dot_map__msgs_dot_map__id__pb2._ID
_PNCJUNCTION.fields_by_name["passage_group"].message_type = _PASSAGEGROUP
DESCRIPTOR.message_types_by_name["Passage"] = _PASSAGE
DESCRIPTOR.message_types_by_name["PassageGroup"] = _PASSAGEGROUP
DESCRIPTOR.message_types_by_name["PNCJunction"] = _PNCJUNCTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
Passage = _reflection.GeneratedProtocolMessageType(
    "Passage",
    (_message.Message,),
    {
        "DESCRIPTOR": _PASSAGE,
        "__module__": "modules.common_msgs.map_msgs.map_pnc_junction_pb2",
    },
)
_sym_db.RegisterMessage(Passage)
PassageGroup = _reflection.GeneratedProtocolMessageType(
    "PassageGroup",
    (_message.Message,),
    {
        "DESCRIPTOR": _PASSAGEGROUP,
        "__module__": "modules.common_msgs.map_msgs.map_pnc_junction_pb2",
    },
)
_sym_db.RegisterMessage(PassageGroup)
PNCJunction = _reflection.GeneratedProtocolMessageType(
    "PNCJunction",
    (_message.Message,),
    {
        "DESCRIPTOR": _PNCJUNCTION,
        "__module__": "modules.common_msgs.map_msgs.map_pnc_junction_pb2",
    },
)
_sym_db.RegisterMessage(PNCJunction)
