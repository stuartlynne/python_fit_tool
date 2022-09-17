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


class AntTxMessage(DataMessage):
    ID = 81
    NAME = 'ant_tx'

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
        super().__init__(name=AntTxMessage.NAME,
                         global_id=AntTxMessage.ID,
                         local_id=definition_message.local_id if definition_message else local_id,
                         endian=definition_message.endian if definition_message else endian,
                         definition_message=definition_message,
                         developer_fields=developer_fields,
                         fields=[
                             TimestampField(
                                 size=self.__get_field_size(definition_message, TimestampField.ID),
                                 growable=definition_message is None),
                             AntTxFractionalTimestampField(
                                 size=self.__get_field_size(definition_message, AntTxFractionalTimestampField.ID),
                                 growable=definition_message is None),
                             AntTxMesgIdField(
                                 size=self.__get_field_size(definition_message, AntTxMesgIdField.ID),
                                 growable=definition_message is None),
                             AntTxMesgDataField(
                                 size=self.__get_field_size(definition_message, AntTxMesgDataField.ID),
                                 growable=definition_message is None),
                             AntTxChannelNumberField(
                                 size=self.__get_field_size(definition_message, AntTxChannelNumberField.ID),
                                 growable=definition_message is None),
                             AntTxDataField(
                                 size=self.__get_field_size(definition_message, AntTxDataField.ID),
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
        field = self.get_field(AntTxFractionalTimestampField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @fractional_timestamp.setter
    def fractional_timestamp(self, value: float):
        field = self.get_field(AntTxFractionalTimestampField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def mesg_id(self) -> Optional[int]:
        field = self.get_field(AntTxMesgIdField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @mesg_id.setter
    def mesg_id(self, value: int):
        field = self.get_field(AntTxMesgIdField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def mesg_data(self) -> Optional[int]:
        field = self.get_field(AntTxMesgDataField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @mesg_data.setter
    def mesg_data(self, value: int):
        field = self.get_field(AntTxMesgDataField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def channel_number(self) -> Optional[int]:
        field = self.get_field(AntTxChannelNumberField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @channel_number.setter
    def channel_number(self, value: int):
        field = self.get_field(AntTxChannelNumberField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def data(self) -> Optional[int]:
        field = self.get_field(AntTxDataField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @data.setter
    def data(self, value: int):
        field = self.get_field(AntTxDataField.ID)

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


class AntTxFractionalTimestampField(Field):
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


class AntTxMesgIdField(Field):
    ID = 1

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='mesg_id',
            field_id=self.ID,
            base_type=BaseType.BYTE,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class AntTxMesgDataField(Field):
    ID = 2

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='mesg_data',
            field_id=self.ID,
            base_type=BaseType.BYTE,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class AntTxChannelNumberField(Field):
    ID = 3

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='channel_number',
            field_id=self.ID,
            base_type=BaseType.UINT8,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class AntTxDataField(Field):
    ID = 4

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='data',
            field_id=self.ID,
            base_type=BaseType.BYTE,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )
