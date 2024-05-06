"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from ......modules.drivers.canbus.proto import (
    can_card_parameter_pb2 as modules_dot_drivers_dot_canbus_dot_proto_dot_can__card__parameter__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/drivers/radar/ultrasonic_radar/proto/ultrasonic_radar_conf.proto",
    package="apollo.drivers.ultrasonic_radar",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\nHmodules/drivers/radar/ultrasonic_radar/proto/ultrasonic_radar_conf.proto\x12\x1fapollo.drivers.ultrasonic_radar\x1a5modules/drivers/canbus/proto/can_card_parameter.proto"\xb6\x01\n\x07CanConf\x12C\n\x12can_card_parameter\x18\x01 \x01(\x0b2\'.apollo.drivers.canbus.CANCardParameter\x12 \n\x11enable_debug_mode\x18\x02 \x01(\x08:\x05false\x12"\n\x13enable_receiver_log\x18\x03 \x01(\x08:\x05false\x12 \n\x11enable_sender_log\x18\x04 \x01(\x08:\x05false"g\n\x13UltrasonicRadarConf\x12:\n\x08can_conf\x18\x01 \x01(\x0b2(.apollo.drivers.ultrasonic_radar.CanConf\x12\x14\n\x0centrance_num\x18\x02 \x01(\x05',
    dependencies=[
        modules_dot_drivers_dot_canbus_dot_proto_dot_can__card__parameter__pb2.DESCRIPTOR
    ],
)
_CANCONF = _descriptor.Descriptor(
    name="CanConf",
    full_name="apollo.drivers.ultrasonic_radar.CanConf",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="can_card_parameter",
            full_name="apollo.drivers.ultrasonic_radar.CanConf.can_card_parameter",
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
            name="enable_debug_mode",
            full_name="apollo.drivers.ultrasonic_radar.CanConf.enable_debug_mode",
            index=1,
            number=2,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=True,
            default_value=False,
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
            name="enable_receiver_log",
            full_name="apollo.drivers.ultrasonic_radar.CanConf.enable_receiver_log",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=True,
            default_value=False,
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
            name="enable_sender_log",
            full_name="apollo.drivers.ultrasonic_radar.CanConf.enable_sender_log",
            index=3,
            number=4,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=True,
            default_value=False,
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
    serialized_start=165,
    serialized_end=347,
)
_ULTRASONICRADARCONF = _descriptor.Descriptor(
    name="UltrasonicRadarConf",
    full_name="apollo.drivers.ultrasonic_radar.UltrasonicRadarConf",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="can_conf",
            full_name="apollo.drivers.ultrasonic_radar.UltrasonicRadarConf.can_conf",
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
            name="entrance_num",
            full_name="apollo.drivers.ultrasonic_radar.UltrasonicRadarConf.entrance_num",
            index=1,
            number=2,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=349,
    serialized_end=452,
)
_CANCONF.fields_by_name[
    "can_card_parameter"
].message_type = (
    modules_dot_drivers_dot_canbus_dot_proto_dot_can__card__parameter__pb2._CANCARDPARAMETER
)
_ULTRASONICRADARCONF.fields_by_name["can_conf"].message_type = _CANCONF
DESCRIPTOR.message_types_by_name["CanConf"] = _CANCONF
DESCRIPTOR.message_types_by_name["UltrasonicRadarConf"] = _ULTRASONICRADARCONF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
CanConf = _reflection.GeneratedProtocolMessageType(
    "CanConf",
    (_message.Message,),
    {
        "DESCRIPTOR": _CANCONF,
        "__module__": "modules.drivers.radar.ultrasonic_radar.proto.ultrasonic_radar_conf_pb2",
    },
)
_sym_db.RegisterMessage(CanConf)
UltrasonicRadarConf = _reflection.GeneratedProtocolMessageType(
    "UltrasonicRadarConf",
    (_message.Message,),
    {
        "DESCRIPTOR": _ULTRASONICRADARCONF,
        "__module__": "modules.drivers.radar.ultrasonic_radar.proto.ultrasonic_radar_conf_pb2",
    },
)
_sym_db.RegisterMessage(UltrasonicRadarConf)
