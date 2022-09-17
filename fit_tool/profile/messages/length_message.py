# Autogenerated. Do not modify.
#
# Profile: 21.60
from typing import Optional

from fit_tool.base_type import BaseType
from fit_tool.data_message import DataMessage
from fit_tool.definition_message import DefinitionMessage
from fit_tool.developer_field import DeveloperField
from fit_tool.endian import Endian
from fit_tool.field import Field
from fit_tool.sub_field import SubField
from fit_tool.profile.profile_type import *


class LengthMessage(DataMessage):
    ID = 101
    NAME = 'length'

    @staticmethod
    def __get_field_size(definition_message: DefinitionMessage, field_id: int) -> int:
        size = 0
        if definition_message:
            field_definition = definition_message.get_field_definition(field_id)
            if field_definition:
                size = field_definition.size

        return size

    def __init__(self, definition_message=None, developer_fields=None, local_id: int = 0,
                 endian: Endian = Endian.LITTLE):
        super().__init__(name=LengthMessage.NAME,
                         global_id=LengthMessage.ID,
                         local_id=definition_message.local_id if definition_message else local_id,
                         endian=definition_message.endian if definition_message else endian,
                         definition_message=definition_message,
                         developer_fields=developer_fields,
                         fields=[
                             MessageIndexField(
                                 size=self.__get_field_size(definition_message, MessageIndexField.ID),
                                 growable=definition_message is None),
                             TimestampField(
                                 size=self.__get_field_size(definition_message, TimestampField.ID),
                                 growable=definition_message is None),
                             LengthEventField(
                                 size=self.__get_field_size(definition_message, LengthEventField.ID),
                                 growable=definition_message is None),
                             LengthEventTypeField(
                                 size=self.__get_field_size(definition_message, LengthEventTypeField.ID),
                                 growable=definition_message is None),
                             LengthStartTimeField(
                                 size=self.__get_field_size(definition_message, LengthStartTimeField.ID),
                                 growable=definition_message is None),
                             LengthTotalElapsedTimeField(
                                 size=self.__get_field_size(definition_message, LengthTotalElapsedTimeField.ID),
                                 growable=definition_message is None),
                             LengthTotalTimerTimeField(
                                 size=self.__get_field_size(definition_message, LengthTotalTimerTimeField.ID),
                                 growable=definition_message is None),
                             LengthTotalStrokesField(
                                 size=self.__get_field_size(definition_message, LengthTotalStrokesField.ID),
                                 growable=definition_message is None),
                             LengthAvgSpeedField(
                                 size=self.__get_field_size(definition_message, LengthAvgSpeedField.ID),
                                 growable=definition_message is None),
                             LengthSwimStrokeField(
                                 size=self.__get_field_size(definition_message, LengthSwimStrokeField.ID),
                                 growable=definition_message is None),
                             LengthAvgSwimmingCadenceField(
                                 size=self.__get_field_size(definition_message, LengthAvgSwimmingCadenceField.ID),
                                 growable=definition_message is None),
                             LengthEventGroupField(
                                 size=self.__get_field_size(definition_message, LengthEventGroupField.ID),
                                 growable=definition_message is None),
                             LengthTotalCaloriesField(
                                 size=self.__get_field_size(definition_message, LengthTotalCaloriesField.ID),
                                 growable=definition_message is None),
                             LengthLengthTypeField(
                                 size=self.__get_field_size(definition_message, LengthLengthTypeField.ID),
                                 growable=definition_message is None),
                             LengthPlayerScoreField(
                                 size=self.__get_field_size(definition_message, LengthPlayerScoreField.ID),
                                 growable=definition_message is None),
                             LengthOpponentScoreField(
                                 size=self.__get_field_size(definition_message, LengthOpponentScoreField.ID),
                                 growable=definition_message is None),
                             LengthStrokeCountField(
                                 size=self.__get_field_size(definition_message, LengthStrokeCountField.ID),
                                 growable=definition_message is None),
                             LengthZoneCountField(
                                 size=self.__get_field_size(definition_message, LengthZoneCountField.ID),
                                 growable=definition_message is None)
                         ])

        self.growable = self.definition_message is None

    @classmethod
    def from_bytes(cls, definition_message: DefinitionMessage, developer_fields: list[DeveloperField],
                   bytes_buffer: bytes, offset: int = 0):
        message = cls(definition_message=definition_message, developer_fields=developer_fields)
        message.read_from_bytes(bytes_buffer, offset)
        return message

    @property
    def message_index(self) -> Optional[int]:
        field = self.get_field(MessageIndexField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @message_index.setter
    def message_index(self, value: int):
        field = self.get_field(MessageIndexField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    # timestamp : milliseconds from January 1st, 1970 at 00:00:00 UTC

    @property
    def timestamp(self) -> Optional[int]:
        field = self.get_field(TimestampField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    # timestamp : milliseconds from January 1st, 1970 at 00:00:00 UTC

    @timestamp.setter
    def timestamp(self, value: int):
        field = self.get_field(TimestampField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def event(self) -> Optional[Event]:
        field = self.get_field(LengthEventField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @event.setter
    def event(self, value: Event):
        field = self.get_field(LengthEventField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def event_type(self) -> Optional[EventType]:
        field = self.get_field(LengthEventTypeField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @event_type.setter
    def event_type(self, value: EventType):
        field = self.get_field(LengthEventTypeField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    # timestamp : milliseconds from January 1st, 1970 at 00:00:00 UTC

    @property
    def start_time(self) -> Optional[int]:
        field = self.get_field(LengthStartTimeField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    # timestamp : milliseconds from January 1st, 1970 at 00:00:00 UTC

    @start_time.setter
    def start_time(self, value: int):
        field = self.get_field(LengthStartTimeField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def total_elapsed_time(self) -> Optional[float]:
        field = self.get_field(LengthTotalElapsedTimeField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @total_elapsed_time.setter
    def total_elapsed_time(self, value: float):
        field = self.get_field(LengthTotalElapsedTimeField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def total_timer_time(self) -> Optional[float]:
        field = self.get_field(LengthTotalTimerTimeField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @total_timer_time.setter
    def total_timer_time(self, value: float):
        field = self.get_field(LengthTotalTimerTimeField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def total_strokes(self) -> Optional[int]:
        field = self.get_field(LengthTotalStrokesField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @total_strokes.setter
    def total_strokes(self, value: int):
        field = self.get_field(LengthTotalStrokesField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def avg_speed(self) -> Optional[float]:
        field = self.get_field(LengthAvgSpeedField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @avg_speed.setter
    def avg_speed(self, value: float):
        field = self.get_field(LengthAvgSpeedField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def swim_stroke(self) -> Optional[SwimStroke]:
        field = self.get_field(LengthSwimStrokeField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @swim_stroke.setter
    def swim_stroke(self, value: SwimStroke):
        field = self.get_field(LengthSwimStrokeField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def avg_swimming_cadence(self) -> Optional[int]:
        field = self.get_field(LengthAvgSwimmingCadenceField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @avg_swimming_cadence.setter
    def avg_swimming_cadence(self, value: int):
        field = self.get_field(LengthAvgSwimmingCadenceField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def event_group(self) -> Optional[int]:
        field = self.get_field(LengthEventGroupField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @event_group.setter
    def event_group(self, value: int):
        field = self.get_field(LengthEventGroupField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def total_calories(self) -> Optional[int]:
        field = self.get_field(LengthTotalCaloriesField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @total_calories.setter
    def total_calories(self, value: int):
        field = self.get_field(LengthTotalCaloriesField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def length_type(self) -> Optional[LengthType]:
        field = self.get_field(LengthLengthTypeField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @length_type.setter
    def length_type(self, value: LengthType):
        field = self.get_field(LengthLengthTypeField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def player_score(self) -> Optional[int]:
        field = self.get_field(LengthPlayerScoreField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @player_score.setter
    def player_score(self, value: int):
        field = self.get_field(LengthPlayerScoreField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def opponent_score(self) -> Optional[int]:
        field = self.get_field(LengthOpponentScoreField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @opponent_score.setter
    def opponent_score(self, value: int):
        field = self.get_field(LengthOpponentScoreField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def stroke_count(self) -> Optional[int]:
        field = self.get_field(LengthStrokeCountField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @stroke_count.setter
    def stroke_count(self, value: int):
        field = self.get_field(LengthStrokeCountField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def zone_count(self) -> Optional[int]:
        field = self.get_field(LengthZoneCountField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @zone_count.setter
    def zone_count(self, value: int):
        field = self.get_field(LengthZoneCountField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)


class MessageIndexField(Field):
    ID = 254

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='message_index',
            field_id=self.ID,
            base_type=BaseType.UINT16,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class TimestampField(Field):
    ID = 253

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='timestamp',
            field_id=self.ID,
            base_type=BaseType.UINT32,
            offset=-631065600000,
            scale=0.001,
            size=size,
            units='ms',
            type_name='date_time',
            growable=growable,
            sub_fields=[
            ]
        )


class LengthEventField(Field):
    ID = 0

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='event',
            field_id=self.ID,
            base_type=BaseType.ENUM,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class LengthEventTypeField(Field):
    ID = 1

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='event_type',
            field_id=self.ID,
            base_type=BaseType.ENUM,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class LengthStartTimeField(Field):
    ID = 2

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='start_time',
            field_id=self.ID,
            base_type=BaseType.UINT32,
            offset=-631065600000,
            scale=0.001,
            size=size,
            units='ms',
            type_name='date_time',
            growable=growable,
            sub_fields=[
            ]
        )


class LengthTotalElapsedTimeField(Field):
    ID = 3

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='total_elapsed_time',
            field_id=self.ID,
            base_type=BaseType.UINT32,
            offset=0,
            scale=1000,
            size=size,
            units='s',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )


class LengthTotalTimerTimeField(Field):
    ID = 4

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='total_timer_time',
            field_id=self.ID,
            base_type=BaseType.UINT32,
            offset=0,
            scale=1000,
            size=size,
            units='s',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )


class LengthTotalStrokesField(Field):
    ID = 5

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='total_strokes',
            field_id=self.ID,
            base_type=BaseType.UINT16,
            offset=0,
            scale=1,
            size=size,
            units='strokes',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )


class LengthAvgSpeedField(Field):
    ID = 6

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='avg_speed',
            field_id=self.ID,
            base_type=BaseType.UINT16,
            offset=0,
            scale=1000,
            size=size,
            units='m/s',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )


class LengthSwimStrokeField(Field):
    ID = 7

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='swim_stroke',
            field_id=self.ID,
            base_type=BaseType.ENUM,
            offset=0,
            scale=1,
            size=size,
            units='swim_stroke',
            type_name='swim_stroke',
            growable=growable,
            sub_fields=[
            ]
        )


class LengthAvgSwimmingCadenceField(Field):
    ID = 9

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='avg_swimming_cadence',
            field_id=self.ID,
            base_type=BaseType.UINT8,
            offset=0,
            scale=1,
            size=size,
            units='strokes/min',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )


class LengthEventGroupField(Field):
    ID = 10

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='event_group',
            field_id=self.ID,
            base_type=BaseType.UINT8,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class LengthTotalCaloriesField(Field):
    ID = 11

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='total_calories',
            field_id=self.ID,
            base_type=BaseType.UINT16,
            offset=0,
            scale=1,
            size=size,
            units='kcal',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )


class LengthLengthTypeField(Field):
    ID = 12

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='length_type',
            field_id=self.ID,
            base_type=BaseType.ENUM,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class LengthPlayerScoreField(Field):
    ID = 18

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='player_score',
            field_id=self.ID,
            base_type=BaseType.UINT16,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class LengthOpponentScoreField(Field):
    ID = 19

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='opponent_score',
            field_id=self.ID,
            base_type=BaseType.UINT16,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class LengthStrokeCountField(Field):
    ID = 20

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='stroke_count',
            field_id=self.ID,
            base_type=BaseType.UINT16,
            offset=0,
            scale=1,
            size=size,
            units='counts',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )


class LengthZoneCountField(Field):
    ID = 21

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='zone_count',
            field_id=self.ID,
            base_type=BaseType.UINT16,
            offset=0,
            scale=1,
            size=size,
            units='counts',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )
