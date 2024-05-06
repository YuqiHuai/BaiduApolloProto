"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/map/tools/map_datachecker/proto/collection_error_code.proto",
    package="apollo.hdmap",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b"\nCmodules/map/tools/map_datachecker/proto/collection_error_code.proto\x12\x0capollo.hdmap*\xab\x05\n\tErrorCode\x12\x0b\n\x07SUCCESS\x10\x00\x12\t\n\x05ERROR\x10\x01\x12\x11\n\rERROR_REQUEST\x10\x02\x12\x1d\n\x19ERROR_SERVICE_NO_RESPONSE\x10\x03\x12\x18\n\x14ERROR_REPEATED_START\x10\x04\x12\x1c\n\x18ERROR_CHECK_BEFORE_START\x10\x05\x12\x15\n\x11ERROR_GPSBIN_LACK\x10e\x12\x18\n\x14ERROR_DISKINFO_ERROR\x10f\x12\x16\n\x12ERROR_DISK_UNMOUNT\x10g\x12\x14\n\x10ERROR_SPEED_LACK\x10i\x12\x19\n\x15WARNING_ODOMETER_LACK\x10j\x12\x19\n\x15ERROR_RTKSTATUS_EMPTY\x10k\x12\x1e\n\x19ERROR_MAPGRPC_NOT_CONNECT\x10\xc9\x01\x12\x19\n\x14WARNING_NOT_STRAIGHT\x10\xd4\x01\x12\x1e\n\x19WARNING_PROGRESS_ROLLBACK\x10\xd5\x01\x12\x1a\n\x15ERROR_NOT_EIGHT_ROUTE\x10\xdd\x01\x12$\n\x1fERROR_CHANNEL_VERIFY_TOPIC_LACK\x10\xe7\x01\x12(\n#ERROR_CHANNEL_VERIFY_RATES_ABNORMAL\x10\xe8\x01\x12\x1e\n\x19ERROR_VERIFY_NO_RECORDERS\x10\xe9\x01\x12\x1c\n\x17ERROR_LOOPS_NOT_REACHED\x10\xea\x01\x12\x1c\n\x17ERROR_VERIFY_NO_GNSSPOS\x10\xeb\x01\x12\x15\n\x10ERROR_NOT_STATIC\x10\xf1\x01\x12\x1b\n\x16ERROR_GNSS_SIGNAL_FAIL\x10\xf2\x01\x12\x17\n\x12SUCCESS_TASK_EMPTY\x10\xad\x02\x12\x17\n\x12SUCCESS_TASK_STOCK\x10\xae\x02",
)
_ERRORCODE = _descriptor.EnumDescriptor(
    name="ErrorCode",
    full_name="apollo.hdmap.ErrorCode",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="SUCCESS",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_REQUEST",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_SERVICE_NO_RESPONSE",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_REPEATED_START",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_CHECK_BEFORE_START",
            index=5,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_GPSBIN_LACK",
            index=6,
            number=101,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_DISKINFO_ERROR",
            index=7,
            number=102,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_DISK_UNMOUNT",
            index=8,
            number=103,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_SPEED_LACK",
            index=9,
            number=105,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="WARNING_ODOMETER_LACK",
            index=10,
            number=106,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_RTKSTATUS_EMPTY",
            index=11,
            number=107,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_MAPGRPC_NOT_CONNECT",
            index=12,
            number=201,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="WARNING_NOT_STRAIGHT",
            index=13,
            number=212,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="WARNING_PROGRESS_ROLLBACK",
            index=14,
            number=213,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_NOT_EIGHT_ROUTE",
            index=15,
            number=221,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_CHANNEL_VERIFY_TOPIC_LACK",
            index=16,
            number=231,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_CHANNEL_VERIFY_RATES_ABNORMAL",
            index=17,
            number=232,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_VERIFY_NO_RECORDERS",
            index=18,
            number=233,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_LOOPS_NOT_REACHED",
            index=19,
            number=234,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_VERIFY_NO_GNSSPOS",
            index=20,
            number=235,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_NOT_STATIC",
            index=21,
            number=241,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_GNSS_SIGNAL_FAIL",
            index=22,
            number=242,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="SUCCESS_TASK_EMPTY",
            index=23,
            number=301,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="SUCCESS_TASK_STOCK",
            index=24,
            number=302,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=86,
    serialized_end=769,
)
_sym_db.RegisterEnumDescriptor(_ERRORCODE)
ErrorCode = enum_type_wrapper.EnumTypeWrapper(_ERRORCODE)
SUCCESS = 0
ERROR = 1
ERROR_REQUEST = 2
ERROR_SERVICE_NO_RESPONSE = 3
ERROR_REPEATED_START = 4
ERROR_CHECK_BEFORE_START = 5
ERROR_GPSBIN_LACK = 101
ERROR_DISKINFO_ERROR = 102
ERROR_DISK_UNMOUNT = 103
ERROR_SPEED_LACK = 105
WARNING_ODOMETER_LACK = 106
ERROR_RTKSTATUS_EMPTY = 107
ERROR_MAPGRPC_NOT_CONNECT = 201
WARNING_NOT_STRAIGHT = 212
WARNING_PROGRESS_ROLLBACK = 213
ERROR_NOT_EIGHT_ROUTE = 221
ERROR_CHANNEL_VERIFY_TOPIC_LACK = 231
ERROR_CHANNEL_VERIFY_RATES_ABNORMAL = 232
ERROR_VERIFY_NO_RECORDERS = 233
ERROR_LOOPS_NOT_REACHED = 234
ERROR_VERIFY_NO_GNSSPOS = 235
ERROR_NOT_STATIC = 241
ERROR_GNSS_SIGNAL_FAIL = 242
SUCCESS_TASK_EMPTY = 301
SUCCESS_TASK_STOCK = 302
DESCRIPTOR.enum_types_by_name["ErrorCode"] = _ERRORCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
