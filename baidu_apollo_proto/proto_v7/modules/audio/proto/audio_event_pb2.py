"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from ....modules.audio.proto import (
    audio_common_pb2 as modules_dot_audio_dot_proto_dot_audio__common__pb2,
)
from ....modules.common.proto import (
    header_pb2 as modules_dot_common_dot_proto_dot_header__pb2,
)
from ....modules.localization.proto import (
    pose_pb2 as modules_dot_localization_dot_proto_dot_pose__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/audio/proto/audio_event.proto",
    package="apollo.audio",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b"\n%modules/audio/proto/audio_event.proto\x12\x0capollo.audio\x1a&modules/audio/proto/audio_common.proto\x1a!modules/common/proto/header.proto\x1a%modules/localization/proto/pose.proto\"\xbe\x02\n\nAudioEvent\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\n\n\x02id\x18\x02 \x01(\x05\x12:\n\rmoving_result\x18\x03 \x01(\x0e2\x1a.apollo.audio.MovingResult:\x07UNKNOWN\x129\n\naudio_type\x18\x04 \x01(\x0e2\x17.apollo.audio.AudioType:\x0cUNKNOWN_TYPE\x12\x13\n\x0bsiren_is_on\x18\x05 \x01(\x08\x12H\n\x0faudio_direction\x18\x06 \x01(\x0e2\x1c.apollo.audio.AudioDirection:\x11UNKNOWN_DIRECTION\x12'\n\x04pose\x18\x07 \x01(\x0b2\x19.apollo.localization.Pose",
    dependencies=[
        modules_dot_audio_dot_proto_dot_audio__common__pb2.DESCRIPTOR,
        modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,
        modules_dot_localization_dot_proto_dot_pose__pb2.DESCRIPTOR,
    ],
)
_AUDIOEVENT = _descriptor.Descriptor(
    name="AudioEvent",
    full_name="apollo.audio.AudioEvent",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="header",
            full_name="apollo.audio.AudioEvent.header",
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
            name="id",
            full_name="apollo.audio.AudioEvent.id",
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
        _descriptor.FieldDescriptor(
            name="moving_result",
            full_name="apollo.audio.AudioEvent.moving_result",
            index=2,
            number=3,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=True,
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
            name="audio_type",
            full_name="apollo.audio.AudioEvent.audio_type",
            index=3,
            number=4,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=True,
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
            name="siren_is_on",
            full_name="apollo.audio.AudioEvent.siren_is_on",
            index=4,
            number=5,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
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
            name="audio_direction",
            full_name="apollo.audio.AudioEvent.audio_direction",
            index=5,
            number=6,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=True,
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
            name="pose",
            full_name="apollo.audio.AudioEvent.pose",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=170,
    serialized_end=488,
)
_AUDIOEVENT.fields_by_name[
    "header"
].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_AUDIOEVENT.fields_by_name[
    "moving_result"
].enum_type = modules_dot_audio_dot_proto_dot_audio__common__pb2._MOVINGRESULT
_AUDIOEVENT.fields_by_name[
    "audio_type"
].enum_type = modules_dot_audio_dot_proto_dot_audio__common__pb2._AUDIOTYPE
_AUDIOEVENT.fields_by_name[
    "audio_direction"
].enum_type = modules_dot_audio_dot_proto_dot_audio__common__pb2._AUDIODIRECTION
_AUDIOEVENT.fields_by_name[
    "pose"
].message_type = modules_dot_localization_dot_proto_dot_pose__pb2._POSE
DESCRIPTOR.message_types_by_name["AudioEvent"] = _AUDIOEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
AudioEvent = _reflection.GeneratedProtocolMessageType(
    "AudioEvent",
    (_message.Message,),
    {"DESCRIPTOR": _AUDIOEVENT, "__module__": "modules.audio.proto.audio_event_pb2"},
)
_sym_db.RegisterMessage(AudioEvent)
