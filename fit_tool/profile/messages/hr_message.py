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


class HrMessage(DataMessage):
    ID = 132
    NAME = 'hr'

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
        super().__init__(name=HrMessage.NAME,
                         global_id=HrMessage.ID,
                         local_id=definition_message.local_id if definition_message else local_id,
                         endian=definition_message.endian if definition_message else endian,
                         definition_message=definition_message,
                         developer_fields=developer_fields,
                         fields=[
                             TimestampField(
                                 size=self.__get_field_size(definition_message, TimestampField.ID),
                                 growable=definition_message is None),
                             HrFractionalTimestampField(
                                 size=self.__get_field_size(definition_message, HrFractionalTimestampField.ID),
                                 growable=definition_message is None),
                             HrTime256Field(
                                 size=self.__get_field_size(definition_message, HrTime256Field.ID),
                                 growable=definition_message is None),
                             HrFilteredBpmField(
                                 size=self.__get_field_size(definition_message, HrFilteredBpmField.ID),
                                 growable=definition_message is None),
                             HrEventTimestampField(
                                 size=self.__get_field_size(definition_message, HrEventTimestampField.ID),
                                 growable=definition_message is None),
                             HrEventTimestamp12Field(
                                 size=self.__get_field_size(definition_message, HrEventTimestamp12Field.ID),
                                 growable=definition_message is None)
                         ])

        self.growable = self.definition_message is None

    @classmethod
    def from_bytes(cls, definition_message: DefinitionMessage, developer_fields: list[DeveloperField],
                   bytes_buffer: bytes, offset: int = 0):
        message = cls(definition_message=definition_message, developer_fields=developer_fields)
        message.read_from_bytes(bytes_buffer, offset)
        return message

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
    def fractional_timestamp(self) -> Optional[float]:
        field = self.get_field(HrFractionalTimestampField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @fractional_timestamp.setter
    def fractional_timestamp(self, value: float):
        field = self.get_field(HrFractionalTimestampField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def time256(self) -> Optional[float]:
        field = self.get_field(HrTime256Field.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @time256.setter
    def time256(self, value: float):
        field = self.get_field(HrTime256Field.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def filtered_bpm(self) -> Optional[int]:
        field = self.get_field(HrFilteredBpmField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @filtered_bpm.setter
    def filtered_bpm(self, value: int):
        field = self.get_field(HrFilteredBpmField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def event_timestamp(self) -> Optional[float]:
        field = self.get_field(HrEventTimestampField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @event_timestamp.setter
    def event_timestamp(self, value: float):
        field = self.get_field(HrEventTimestampField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def event_timestamp_12(self) -> Optional[int]:
        field = self.get_field(HrEventTimestamp12Field.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @event_timestamp_12.setter
    def event_timestamp_12(self, value: int):
        field = self.get_field(HrEventTimestamp12Field.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)


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


class HrFractionalTimestampField(Field):
    ID = 0

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='fractional_timestamp',
            field_id=self.ID,
            base_type=BaseType.UINT16,
            offset=0,
            scale=32768,
            size=size,
            units='s',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )


class HrTime256Field(Field):
    ID = 1

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='time256',
            field_id=self.ID,
            base_type=BaseType.UINT8,
            offset=0,
            scale=256,
            size=size,
            units='s',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )


class HrFilteredBpmField(Field):
    ID = 6

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='filtered_bpm',
            field_id=self.ID,
            base_type=BaseType.UINT8,
            offset=0,
            scale=1,
            size=size,
            units='bpm',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )


class HrEventTimestampField(Field):
    ID = 9

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='event_timestamp',
            field_id=self.ID,
            base_type=BaseType.UINT32,
            offset=0,
            scale=1024,
            size=size,
            units='s',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )


class HrEventTimestamp12Field(Field):
    ID = 10

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='event_timestamp_12',
            field_id=self.ID,
            base_type=BaseType.BYTE,
            offset=0,
            scale=1,
            size=size,
            units='s',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )
