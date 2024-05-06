"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

_sym_db = _symbol_database.Default()
from ....modules.common.proto import (
    header_pb2 as modules_dot_common_dot_proto_dot_header__pb2,
)
from ....modules.map.proto import (
    map_parking_space_pb2 as modules_dot_map_dot_proto_dot_map__parking__space__pb2,
)
from ....modules.routing.proto import (
    routing_pb2 as modules_dot_routing_dot_proto_dot_routing__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/task_manager/proto/task_manager.proto",
    package="apollo.task_manager",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n-modules/task_manager/proto/task_manager.proto\x12\x13apollo.task_manager\x1a!modules/common/proto/header.proto\x1a#modules/routing/proto/routing.proto\x1a)modules/map/proto/map_parking_space.proto"^\n\x10CycleRoutingTask\x12\x11\n\tcycle_num\x18\x01 \x01(\x05\x127\n\x0frouting_request\x18\x02 \x01(\x0b2\x1e.apollo.routing.RoutingRequest"a\n\x12ParkingRoutingTask\x12\x12\n\nlane_width\x18\x01 \x01(\x01\x127\n\x0frouting_request\x18\x02 \x01(\x0b2\x1e.apollo.routing.RoutingRequest"\x8d\x01\n\x12DeadEndRoutingTask\x12:\n\x12routing_request_in\x18\x02 \x01(\x0b2\x1e.apollo.routing.RoutingRequest\x12;\n\x13routing_request_out\x18\x03 \x01(\x0b2\x1e.apollo.routing.RoutingRequest"\xda\x02\n\x04Task\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x11\n\ttask_name\x18\x02 \x01(\t\x120\n\ttask_type\x18\x03 \x01(\x0e2\x1d.apollo.task_manager.TaskType\x12C\n\x12cycle_routing_task\x18\x04 \x01(\x0b2%.apollo.task_manager.CycleRoutingTaskH\x00\x12G\n\x14parking_routing_task\x18\x05 \x01(\x0b2\'.apollo.task_manager.ParkingRoutingTaskH\x00\x12H\n\x15dead_end_routing_task\x18\x06 \x01(\x0b2\'.apollo.task_manager.DeadEndRoutingTaskH\x00B\x0e\n\x0crouting_task*H\n\x08TaskType\x12\x11\n\rCYCLE_ROUTING\x10\x00\x12\x13\n\x0fPARKING_ROUTING\x10\x01\x12\x14\n\x10DEAD_END_ROUTING\x10\x03*d\n\x0cJunctionType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07IN_ROAD\x10\x01\x12\x0e\n\nCROSS_ROAD\x10\x02\x12\r\n\tFORK_ROAD\x10\x03\x12\r\n\tMAIN_SIDE\x10\x04\x12\x0c\n\x08DEAD_END\x10\x05',
    dependencies=[
        modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,
        modules_dot_routing_dot_proto_dot_routing__pb2.DESCRIPTOR,
        modules_dot_map_dot_proto_dot_map__parking__space__pb2.DESCRIPTOR,
    ],
)
_TASKTYPE = _descriptor.EnumDescriptor(
    name="TaskType",
    full_name="apollo.task_manager.TaskType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="CYCLE_ROUTING",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PARKING_ROUTING",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="DEAD_END_ROUTING",
            index=2,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=873,
    serialized_end=945,
)
_sym_db.RegisterEnumDescriptor(_TASKTYPE)
TaskType = enum_type_wrapper.EnumTypeWrapper(_TASKTYPE)
_JUNCTIONTYPE = _descriptor.EnumDescriptor(
    name="JunctionType",
    full_name="apollo.task_manager.JunctionType",
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
            name="IN_ROAD",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CROSS_ROAD",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="FORK_ROAD",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MAIN_SIDE",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="DEAD_END",
            index=5,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=947,
    serialized_end=1047,
)
_sym_db.RegisterEnumDescriptor(_JUNCTIONTYPE)
JunctionType = enum_type_wrapper.EnumTypeWrapper(_JUNCTIONTYPE)
CYCLE_ROUTING = 0
PARKING_ROUTING = 1
DEAD_END_ROUTING = 3
UNKNOWN = 0
IN_ROAD = 1
CROSS_ROAD = 2
FORK_ROAD = 3
MAIN_SIDE = 4
DEAD_END = 5
_CYCLEROUTINGTASK = _descriptor.Descriptor(
    name="CycleRoutingTask",
    full_name="apollo.task_manager.CycleRoutingTask",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="cycle_num",
            full_name="apollo.task_manager.CycleRoutingTask.cycle_num",
            index=0,
            number=1,
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
        _descriptor.FieldDescriptor(
            name="routing_request",
            full_name="apollo.task_manager.CycleRoutingTask.routing_request",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=185,
    serialized_end=279,
)
_PARKINGROUTINGTASK = _descriptor.Descriptor(
    name="ParkingRoutingTask",
    full_name="apollo.task_manager.ParkingRoutingTask",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="lane_width",
            full_name="apollo.task_manager.ParkingRoutingTask.lane_width",
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
            name="routing_request",
            full_name="apollo.task_manager.ParkingRoutingTask.routing_request",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=281,
    serialized_end=378,
)
_DEADENDROUTINGTASK = _descriptor.Descriptor(
    name="DeadEndRoutingTask",
    full_name="apollo.task_manager.DeadEndRoutingTask",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="routing_request_in",
            full_name="apollo.task_manager.DeadEndRoutingTask.routing_request_in",
            index=0,
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
            name="routing_request_out",
            full_name="apollo.task_manager.DeadEndRoutingTask.routing_request_out",
            index=1,
            number=3,
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
    serialized_start=381,
    serialized_end=522,
)
_TASK = _descriptor.Descriptor(
    name="Task",
    full_name="apollo.task_manager.Task",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="header",
            full_name="apollo.task_manager.Task.header",
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
            name="task_name",
            full_name="apollo.task_manager.Task.task_name",
            index=1,
            number=2,
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
            name="task_type",
            full_name="apollo.task_manager.Task.task_type",
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
            name="cycle_routing_task",
            full_name="apollo.task_manager.Task.cycle_routing_task",
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
            name="parking_routing_task",
            full_name="apollo.task_manager.Task.parking_routing_task",
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
            name="dead_end_routing_task",
            full_name="apollo.task_manager.Task.dead_end_routing_task",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="routing_task",
            full_name="apollo.task_manager.Task.routing_task",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        )
    ],
    serialized_start=525,
    serialized_end=871,
)
_CYCLEROUTINGTASK.fields_by_name[
    "routing_request"
].message_type = modules_dot_routing_dot_proto_dot_routing__pb2._ROUTINGREQUEST
_PARKINGROUTINGTASK.fields_by_name[
    "routing_request"
].message_type = modules_dot_routing_dot_proto_dot_routing__pb2._ROUTINGREQUEST
_DEADENDROUTINGTASK.fields_by_name[
    "routing_request_in"
].message_type = modules_dot_routing_dot_proto_dot_routing__pb2._ROUTINGREQUEST
_DEADENDROUTINGTASK.fields_by_name[
    "routing_request_out"
].message_type = modules_dot_routing_dot_proto_dot_routing__pb2._ROUTINGREQUEST
_TASK.fields_by_name[
    "header"
].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_TASK.fields_by_name["task_type"].enum_type = _TASKTYPE
_TASK.fields_by_name["cycle_routing_task"].message_type = _CYCLEROUTINGTASK
_TASK.fields_by_name["parking_routing_task"].message_type = _PARKINGROUTINGTASK
_TASK.fields_by_name["dead_end_routing_task"].message_type = _DEADENDROUTINGTASK
_TASK.oneofs_by_name["routing_task"].fields.append(
    _TASK.fields_by_name["cycle_routing_task"]
)
_TASK.fields_by_name["cycle_routing_task"].containing_oneof = _TASK.oneofs_by_name[
    "routing_task"
]
_TASK.oneofs_by_name["routing_task"].fields.append(
    _TASK.fields_by_name["parking_routing_task"]
)
_TASK.fields_by_name["parking_routing_task"].containing_oneof = _TASK.oneofs_by_name[
    "routing_task"
]
_TASK.oneofs_by_name["routing_task"].fields.append(
    _TASK.fields_by_name["dead_end_routing_task"]
)
_TASK.fields_by_name["dead_end_routing_task"].containing_oneof = _TASK.oneofs_by_name[
    "routing_task"
]
DESCRIPTOR.message_types_by_name["CycleRoutingTask"] = _CYCLEROUTINGTASK
DESCRIPTOR.message_types_by_name["ParkingRoutingTask"] = _PARKINGROUTINGTASK
DESCRIPTOR.message_types_by_name["DeadEndRoutingTask"] = _DEADENDROUTINGTASK
DESCRIPTOR.message_types_by_name["Task"] = _TASK
DESCRIPTOR.enum_types_by_name["TaskType"] = _TASKTYPE
DESCRIPTOR.enum_types_by_name["JunctionType"] = _JUNCTIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
CycleRoutingTask = _reflection.GeneratedProtocolMessageType(
    "CycleRoutingTask",
    (_message.Message,),
    {
        "DESCRIPTOR": _CYCLEROUTINGTASK,
        "__module__": "modules.task_manager.proto.task_manager_pb2",
    },
)
_sym_db.RegisterMessage(CycleRoutingTask)
ParkingRoutingTask = _reflection.GeneratedProtocolMessageType(
    "ParkingRoutingTask",
    (_message.Message,),
    {
        "DESCRIPTOR": _PARKINGROUTINGTASK,
        "__module__": "modules.task_manager.proto.task_manager_pb2",
    },
)
_sym_db.RegisterMessage(ParkingRoutingTask)
DeadEndRoutingTask = _reflection.GeneratedProtocolMessageType(
    "DeadEndRoutingTask",
    (_message.Message,),
    {
        "DESCRIPTOR": _DEADENDROUTINGTASK,
        "__module__": "modules.task_manager.proto.task_manager_pb2",
    },
)
_sym_db.RegisterMessage(DeadEndRoutingTask)
Task = _reflection.GeneratedProtocolMessageType(
    "Task",
    (_message.Message,),
    {"DESCRIPTOR": _TASK, "__module__": "modules.task_manager.proto.task_manager_pb2"},
)
_sym_db.RegisterMessage(Task)
