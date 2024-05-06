"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/control/proto/gain_scheduler_conf.proto",
    package="apollo.control",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n/modules/control/proto/gain_scheduler_conf.proto\x12\x0eapollo.control"E\n\rGainScheduler\x124\n\tscheduler\x18\x01 \x03(\x0b2!.apollo.control.GainSchedulerInfo"1\n\x11GainSchedulerInfo\x12\r\n\x05speed\x18\x01 \x01(\x01\x12\r\n\x05ratio\x18\x02 \x01(\x01',
)
_GAINSCHEDULER = _descriptor.Descriptor(
    name="GainScheduler",
    full_name="apollo.control.GainScheduler",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="scheduler",
            full_name="apollo.control.GainScheduler.scheduler",
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
    serialized_start=67,
    serialized_end=136,
)
_GAINSCHEDULERINFO = _descriptor.Descriptor(
    name="GainSchedulerInfo",
    full_name="apollo.control.GainSchedulerInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="speed",
            full_name="apollo.control.GainSchedulerInfo.speed",
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
            name="ratio",
            full_name="apollo.control.GainSchedulerInfo.ratio",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=138,
    serialized_end=187,
)
_GAINSCHEDULER.fields_by_name["scheduler"].message_type = _GAINSCHEDULERINFO
DESCRIPTOR.message_types_by_name["GainScheduler"] = _GAINSCHEDULER
DESCRIPTOR.message_types_by_name["GainSchedulerInfo"] = _GAINSCHEDULERINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
GainScheduler = _reflection.GeneratedProtocolMessageType(
    "GainScheduler",
    (_message.Message,),
    {
        "DESCRIPTOR": _GAINSCHEDULER,
        "__module__": "modules.control.proto.gain_scheduler_conf_pb2",
    },
)
_sym_db.RegisterMessage(GainScheduler)
GainSchedulerInfo = _reflection.GeneratedProtocolMessageType(
    "GainSchedulerInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _GAINSCHEDULERINFO,
        "__module__": "modules.control.proto.gain_scheduler_conf_pb2",
    },
)
_sym_db.RegisterMessage(GainSchedulerInfo)