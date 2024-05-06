"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from ....modules.routing.proto import (
    routing_pb2 as modules_dot_routing_dot_proto_dot_routing__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/routing/proto/poi.proto",
    package="apollo.routing",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1fmodules/routing/proto/poi.proto\x12\x0eapollo.routing\x1a#modules/routing/proto/routing.proto"\x99\x01\n\x08Landmark\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\x08waypoint\x18\x02 \x03(\x0b2\x1c.apollo.routing.LaneWaypoint\x12\x1c\n\x10parking_space_id\x18\x03 \x01(\tB\x02\x18\x01\x121\n\x0cparking_info\x18\x04 \x01(\x0b2\x1b.apollo.routing.ParkingInfo"1\n\x03POI\x12*\n\x08landmark\x18\x01 \x03(\x0b2\x18.apollo.routing.Landmark',
    dependencies=[modules_dot_routing_dot_proto_dot_routing__pb2.DESCRIPTOR],
)
_LANDMARK = _descriptor.Descriptor(
    name="Landmark",
    full_name="apollo.routing.Landmark",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="apollo.routing.Landmark.name",
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
            name="waypoint",
            full_name="apollo.routing.Landmark.waypoint",
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
            name="parking_space_id",
            full_name="apollo.routing.Landmark.parking_space_id",
            index=2,
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
            serialized_options=b"\x18\x01",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="parking_info",
            full_name="apollo.routing.Landmark.parking_info",
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
    serialized_start=89,
    serialized_end=242,
)
_POI = _descriptor.Descriptor(
    name="POI",
    full_name="apollo.routing.POI",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="landmark",
            full_name="apollo.routing.POI.landmark",
            index=0,
            number=1,
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
    serialized_start=244,
    serialized_end=293,
)
_LANDMARK.fields_by_name[
    "waypoint"
].message_type = modules_dot_routing_dot_proto_dot_routing__pb2._LANEWAYPOINT
_LANDMARK.fields_by_name[
    "parking_info"
].message_type = modules_dot_routing_dot_proto_dot_routing__pb2._PARKINGINFO
_POI.fields_by_name["landmark"].message_type = _LANDMARK
DESCRIPTOR.message_types_by_name["Landmark"] = _LANDMARK
DESCRIPTOR.message_types_by_name["POI"] = _POI
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
Landmark = _reflection.GeneratedProtocolMessageType(
    "Landmark",
    (_message.Message,),
    {"DESCRIPTOR": _LANDMARK, "__module__": "modules.routing.proto.poi_pb2"},
)
_sym_db.RegisterMessage(Landmark)
POI = _reflection.GeneratedProtocolMessageType(
    "POI",
    (_message.Message,),
    {"DESCRIPTOR": _POI, "__module__": "modules.routing.proto.poi_pb2"},
)
_sym_db.RegisterMessage(POI)
_LANDMARK.fields_by_name["parking_space_id"]._options = None
