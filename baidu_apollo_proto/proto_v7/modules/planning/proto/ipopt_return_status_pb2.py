"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/planning/proto/ipopt_return_status.proto",
    package="apollo.planning",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b"\n0modules/planning/proto/ipopt_return_status.proto\x12\x0fapollo.planning*\xeb\x04\n\x11IpoptReturnStatus\x12\x13\n\x0fSOLVE_SUCCEEDED\x10\x00\x12\x1e\n\x1aSOLVED_TO_ACCEPTABLE_LEVEL\x10\x01\x12\x1f\n\x1bINFEASIBLE_PROBLEM_DETECTED\x10\x02\x12&\n\"SEARCH_DIRECTION_BECOMES_TOO_SMALL\x10\x03\x12\x15\n\x11DIVERGIN_ITERATES\x10\x04\x12\x17\n\x13USER_REQUESTED_STOP\x10\x05\x12\x18\n\x14FEASIBLE_POINT_FOUND\x10\x06\x12(\n\x1bMAXIMUM_ITERATIONS_EXCEEDED\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1f\n\x12RESTORATION_FAILED\x10\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12&\n\x19ERROR_IN_STEP_COMPUTATION\x10\xfd\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12*\n\x1dNOT_ENOUGH_DEGREES_OF_FREEDOM\x10\xf6\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12'\n\x1aINVALID_PROGRAM_DEFINITION\x10\xf5\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1b\n\x0eINVALID_OPTION\x10\xf4\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12$\n\x17INVALID_NUMBER_DETECTED\x10\xf3\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12$\n\x17UNRECOVERABLE_EXCEPTION\x10\x9c\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12&\n\x19NONIPOPT_EXCEPTION_THROWN\x10\x9b\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12 \n\x13INSUFFICIENT_MEMORY\x10\x9a\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x13\n\x0eINTERNAL_ERROR\x10\xc7\x01",
)
_IPOPTRETURNSTATUS = _descriptor.EnumDescriptor(
    name="IpoptReturnStatus",
    full_name="apollo.planning.IpoptReturnStatus",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="SOLVE_SUCCEEDED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="SOLVED_TO_ACCEPTABLE_LEVEL",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="INFEASIBLE_PROBLEM_DETECTED",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="SEARCH_DIRECTION_BECOMES_TOO_SMALL",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="DIVERGIN_ITERATES",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="USER_REQUESTED_STOP",
            index=5,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="FEASIBLE_POINT_FOUND",
            index=6,
            number=6,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MAXIMUM_ITERATIONS_EXCEEDED",
            index=7,
            number=-1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="RESTORATION_FAILED",
            index=8,
            number=-2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR_IN_STEP_COMPUTATION",
            index=9,
            number=-3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="NOT_ENOUGH_DEGREES_OF_FREEDOM",
            index=10,
            number=-10,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="INVALID_PROGRAM_DEFINITION",
            index=11,
            number=-11,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="INVALID_OPTION",
            index=12,
            number=-12,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="INVALID_NUMBER_DETECTED",
            index=13,
            number=-13,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="UNRECOVERABLE_EXCEPTION",
            index=14,
            number=-100,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="NONIPOPT_EXCEPTION_THROWN",
            index=15,
            number=-101,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="INSUFFICIENT_MEMORY",
            index=16,
            number=-102,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="INTERNAL_ERROR",
            index=17,
            number=199,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=70,
    serialized_end=689,
)
_sym_db.RegisterEnumDescriptor(_IPOPTRETURNSTATUS)
IpoptReturnStatus = enum_type_wrapper.EnumTypeWrapper(_IPOPTRETURNSTATUS)
SOLVE_SUCCEEDED = 0
SOLVED_TO_ACCEPTABLE_LEVEL = 1
INFEASIBLE_PROBLEM_DETECTED = 2
SEARCH_DIRECTION_BECOMES_TOO_SMALL = 3
DIVERGIN_ITERATES = 4
USER_REQUESTED_STOP = 5
FEASIBLE_POINT_FOUND = 6
MAXIMUM_ITERATIONS_EXCEEDED = -1
RESTORATION_FAILED = -2
ERROR_IN_STEP_COMPUTATION = -3
NOT_ENOUGH_DEGREES_OF_FREEDOM = -10
INVALID_PROGRAM_DEFINITION = -11
INVALID_OPTION = -12
INVALID_NUMBER_DETECTED = -13
UNRECOVERABLE_EXCEPTION = -100
NONIPOPT_EXCEPTION_THROWN = -101
INSUFFICIENT_MEMORY = -102
INTERNAL_ERROR = 199
DESCRIPTOR.enum_types_by_name["IpoptReturnStatus"] = _IPOPTRETURNSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
