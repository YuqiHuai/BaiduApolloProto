"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from .....modules.common.proto import (
    geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2,
)
from .....modules.common.proto import (
    header_pb2 as modules_dot_common_dot_proto_dot_header__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/drivers/gnss/proto/ins.proto",
    package="apollo.drivers.gnss",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n$modules/drivers/gnss/proto/ins.proto\x12\x13apollo.drivers.gnss\x1a!modules/common/proto/header.proto\x1a#modules/common/proto/geometry.proto"V\n\x07InsStat\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x12\n\nins_status\x18\x02 \x01(\r\x12\x10\n\x08pos_type\x18\x03 \x01(\r"\xd6\x04\n\x03Ins\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x18\n\x10measurement_time\x18\x02 \x01(\x01\x12+\n\x04type\x18\x03 \x01(\x0e2\x1d.apollo.drivers.gnss.Ins.Type\x12)\n\x08position\x18\x04 \x01(\x0b2\x17.apollo.common.PointLLH\x12,\n\x0ceuler_angles\x18\x05 \x01(\x0b2\x16.apollo.common.Point3D\x12/\n\x0flinear_velocity\x18\x06 \x01(\x0b2\x16.apollo.common.Point3D\x120\n\x10angular_velocity\x18\x07 \x01(\x0b2\x16.apollo.common.Point3D\x123\n\x13linear_acceleration\x18\x08 \x01(\x0b2\x16.apollo.common.Point3D\x12\x1f\n\x13position_covariance\x18\t \x03(\x02B\x02\x10\x01\x12#\n\x17euler_angles_covariance\x18\n \x03(\x02B\x02\x10\x01\x12&\n\x1alinear_velocity_covariance\x18\x0b \x03(\x02B\x02\x10\x01\x12\'\n\x1bangular_velocity_covariance\x18\x0c \x03(\x02B\x02\x10\x01\x12*\n\x1elinear_acceleration_covariance\x18\r \x03(\x02B\x02\x10\x01"-\n\x04Type\x12\x0b\n\x07INVALID\x10\x00\x12\x0e\n\nCONVERGING\x10\x01\x12\x08\n\x04GOOD\x10\x02',
    dependencies=[
        modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,
        modules_dot_common_dot_proto_dot_geometry__pb2.DESCRIPTOR,
    ],
)
_INS_TYPE = _descriptor.EnumDescriptor(
    name="Type",
    full_name="apollo.drivers.gnss.Ins.Type",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="INVALID",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CONVERGING",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="GOOD",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=775,
    serialized_end=820,
)
_sym_db.RegisterEnumDescriptor(_INS_TYPE)
_INSSTAT = _descriptor.Descriptor(
    name="InsStat",
    full_name="apollo.drivers.gnss.InsStat",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="header",
            full_name="apollo.drivers.gnss.InsStat.header",
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
            name="ins_status",
            full_name="apollo.drivers.gnss.InsStat.ins_status",
            index=1,
            number=2,
            type=13,
            cpp_type=3,
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
            name="pos_type",
            full_name="apollo.drivers.gnss.InsStat.pos_type",
            index=2,
            number=3,
            type=13,
            cpp_type=3,
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
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=133,
    serialized_end=219,
)
_INS = _descriptor.Descriptor(
    name="Ins",
    full_name="apollo.drivers.gnss.Ins",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="header",
            full_name="apollo.drivers.gnss.Ins.header",
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
            name="measurement_time",
            full_name="apollo.drivers.gnss.Ins.measurement_time",
            index=1,
            number=2,
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
            name="type",
            full_name="apollo.drivers.gnss.Ins.type",
            index=2,
            number=3,
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
            name="position",
            full_name="apollo.drivers.gnss.Ins.position",
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
            name="euler_angles",
            full_name="apollo.drivers.gnss.Ins.euler_angles",
            index=4,
            number=5,
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
            name="linear_velocity",
            full_name="apollo.drivers.gnss.Ins.linear_velocity",
            index=5,
            number=6,
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
            name="angular_velocity",
            full_name="apollo.drivers.gnss.Ins.angular_velocity",
            index=6,
            number=7,
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
            name="linear_acceleration",
            full_name="apollo.drivers.gnss.Ins.linear_acceleration",
            index=7,
            number=8,
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
            name="position_covariance",
            full_name="apollo.drivers.gnss.Ins.position_covariance",
            index=8,
            number=9,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\x10\x01",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="euler_angles_covariance",
            full_name="apollo.drivers.gnss.Ins.euler_angles_covariance",
            index=9,
            number=10,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\x10\x01",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="linear_velocity_covariance",
            full_name="apollo.drivers.gnss.Ins.linear_velocity_covariance",
            index=10,
            number=11,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\x10\x01",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="angular_velocity_covariance",
            full_name="apollo.drivers.gnss.Ins.angular_velocity_covariance",
            index=11,
            number=12,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\x10\x01",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="linear_acceleration_covariance",
            full_name="apollo.drivers.gnss.Ins.linear_acceleration_covariance",
            index=12,
            number=13,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\x10\x01",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_INS_TYPE],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=222,
    serialized_end=820,
)
_INSSTAT.fields_by_name[
    "header"
].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_INS.fields_by_name[
    "header"
].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_INS.fields_by_name["type"].enum_type = _INS_TYPE
_INS.fields_by_name[
    "position"
].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINTLLH
_INS.fields_by_name[
    "euler_angles"
].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINT3D
_INS.fields_by_name[
    "linear_velocity"
].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINT3D
_INS.fields_by_name[
    "angular_velocity"
].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINT3D
_INS.fields_by_name[
    "linear_acceleration"
].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINT3D
_INS_TYPE.containing_type = _INS
DESCRIPTOR.message_types_by_name["InsStat"] = _INSSTAT
DESCRIPTOR.message_types_by_name["Ins"] = _INS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
InsStat = _reflection.GeneratedProtocolMessageType(
    "InsStat",
    (_message.Message,),
    {"DESCRIPTOR": _INSSTAT, "__module__": "modules.drivers.gnss.proto.ins_pb2"},
)
_sym_db.RegisterMessage(InsStat)
Ins = _reflection.GeneratedProtocolMessageType(
    "Ins",
    (_message.Message,),
    {"DESCRIPTOR": _INS, "__module__": "modules.drivers.gnss.proto.ins_pb2"},
)
_sym_db.RegisterMessage(Ins)
_INS.fields_by_name["position_covariance"]._options = None
_INS.fields_by_name["euler_angles_covariance"]._options = None
_INS.fields_by_name["linear_velocity_covariance"]._options = None
_INS.fields_by_name["angular_velocity_covariance"]._options = None
_INS.fields_by_name["linear_acceleration_covariance"]._options = None
