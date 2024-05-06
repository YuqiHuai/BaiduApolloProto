"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/common_msgs/prediction_msgs/prediction_point.proto",
    package="apollo.prediction",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n:modules/common_msgs/prediction_msgs/prediction_point.proto\x12\x11apollo.prediction"E\n\x13PredictionPathPoint\x12\t\n\x01x\x18\x01 \x02(\x01\x12\t\n\x01y\x18\x02 \x02(\x01\x12\x18\n\x10velocity_heading\x18\x03 \x01(\x01"j\n\x19PredictionTrajectoryPoint\x12:\n\npath_point\x18\x01 \x02(\x0b2&.apollo.prediction.PredictionPathPoint\x12\x11\n\ttimestamp\x18\x02 \x02(\x01',
)
_PREDICTIONPATHPOINT = _descriptor.Descriptor(
    name="PredictionPathPoint",
    full_name="apollo.prediction.PredictionPathPoint",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="x",
            full_name="apollo.prediction.PredictionPathPoint.x",
            index=0,
            number=1,
            type=1,
            cpp_type=5,
            label=2,
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
            name="y",
            full_name="apollo.prediction.PredictionPathPoint.y",
            index=1,
            number=2,
            type=1,
            cpp_type=5,
            label=2,
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
            name="velocity_heading",
            full_name="apollo.prediction.PredictionPathPoint.velocity_heading",
            index=2,
            number=3,
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
    serialized_start=81,
    serialized_end=150,
)
_PREDICTIONTRAJECTORYPOINT = _descriptor.Descriptor(
    name="PredictionTrajectoryPoint",
    full_name="apollo.prediction.PredictionTrajectoryPoint",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="path_point",
            full_name="apollo.prediction.PredictionTrajectoryPoint.path_point",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=2,
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
            name="timestamp",
            full_name="apollo.prediction.PredictionTrajectoryPoint.timestamp",
            index=1,
            number=2,
            type=1,
            cpp_type=5,
            label=2,
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
    serialized_start=152,
    serialized_end=258,
)
_PREDICTIONTRAJECTORYPOINT.fields_by_name[
    "path_point"
].message_type = _PREDICTIONPATHPOINT
DESCRIPTOR.message_types_by_name["PredictionPathPoint"] = _PREDICTIONPATHPOINT
DESCRIPTOR.message_types_by_name[
    "PredictionTrajectoryPoint"
] = _PREDICTIONTRAJECTORYPOINT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
PredictionPathPoint = _reflection.GeneratedProtocolMessageType(
    "PredictionPathPoint",
    (_message.Message,),
    {
        "DESCRIPTOR": _PREDICTIONPATHPOINT,
        "__module__": "modules.common_msgs.prediction_msgs.prediction_point_pb2",
    },
)
_sym_db.RegisterMessage(PredictionPathPoint)
PredictionTrajectoryPoint = _reflection.GeneratedProtocolMessageType(
    "PredictionTrajectoryPoint",
    (_message.Message,),
    {
        "DESCRIPTOR": _PREDICTIONTRAJECTORYPOINT,
        "__module__": "modules.common_msgs.prediction_msgs.prediction_point_pb2",
    },
)
_sym_db.RegisterMessage(PredictionTrajectoryPoint)
