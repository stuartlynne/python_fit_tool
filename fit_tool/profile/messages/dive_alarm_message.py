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


class DiveAlarmMessage(DataMessage):
    ID = 262
    NAME = 'dive_alarm'

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
        super().__init__(name=DiveAlarmMessage.NAME,
                         global_id=DiveAlarmMessage.ID,
                         local_id=definition_message.local_id if definition_message else local_id,
                         endian=definition_message.endian if definition_message else endian,
                         definition_message=definition_message,
                         developer_fields=developer_fields,
                         fields=[
                             MessageIndexField(
                                 size=self.__get_field_size(definition_message, MessageIndexField.ID),
                                 growable=definition_message is None),
                             DiveAlarmDepthField(
                                 size=self.__get_field_size(definition_message, DiveAlarmDepthField.ID),
                                 growable=definition_message is None),
                             DiveAlarmTimeField(
                                 size=self.__get_field_size(definition_message, DiveAlarmTimeField.ID),
                                 growable=definition_message is None),
                             DiveAlarmEnabledField(
                                 size=self.__get_field_size(definition_message, DiveAlarmEnabledField.ID),
                                 growable=definition_message is None),
                             DiveAlarmAlarmTypeField(
                                 size=self.__get_field_size(definition_message, DiveAlarmAlarmTypeField.ID),
                                 growable=definition_message is None),
                             DiveAlarmSoundField(
                                 size=self.__get_field_size(definition_message, DiveAlarmSoundField.ID),
                                 growable=definition_message is None),
                             DiveAlarmDiveTypesField(
                                 size=self.__get_field_size(definition_message, DiveAlarmDiveTypesField.ID),
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

    @property
    def depth(self) -> Optional[float]:
        field = self.get_field(DiveAlarmDepthField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @depth.setter
    def depth(self, value: float):
        field = self.get_field(DiveAlarmDepthField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def time(self) -> Optional[int]:
        field = self.get_field(DiveAlarmTimeField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @time.setter
    def time(self, value: int):
        field = self.get_field(DiveAlarmTimeField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def enabled(self) -> Optional[bool]:
        field = self.get_field(DiveAlarmEnabledField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @enabled.setter
    def enabled(self, value: bool):
        field = self.get_field(DiveAlarmEnabledField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def alarm_type(self) -> Optional[DiveAlarmType]:
        field = self.get_field(DiveAlarmAlarmTypeField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @alarm_type.setter
    def alarm_type(self, value: DiveAlarmType):
        field = self.get_field(DiveAlarmAlarmTypeField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def sound(self) -> Optional[Tone]:
        field = self.get_field(DiveAlarmSoundField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @sound.setter
    def sound(self, value: Tone):
        field = self.get_field(DiveAlarmSoundField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def dive_types(self) -> Optional[SubSport]:
        field = self.get_field(DiveAlarmDiveTypesField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @dive_types.setter
    def dive_types(self, value: SubSport):
        field = self.get_field(DiveAlarmDiveTypesField.ID)

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


class DiveAlarmDepthField(Field):
    ID = 0

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='depth',
            field_id=self.ID,
            base_type=BaseType.UINT32,
            offset=0,
            scale=1000,
            size=size,
            units='m',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )


class DiveAlarmTimeField(Field):
    ID = 1

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='time',
            field_id=self.ID,
            base_type=BaseType.SINT32,
            offset=0,
            scale=1,
            size=size,
            units='s',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )


class DiveAlarmEnabledField(Field):
    ID = 2

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='enabled',
            field_id=self.ID,
            base_type=BaseType.UINT8,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class DiveAlarmAlarmTypeField(Field):
    ID = 3

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='alarm_type',
            field_id=self.ID,
            base_type=BaseType.ENUM,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class DiveAlarmSoundField(Field):
    ID = 4

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='sound',
            field_id=self.ID,
            base_type=BaseType.ENUM,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class DiveAlarmDiveTypesField(Field):
    ID = 5

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='dive_types',
            field_id=self.ID,
            base_type=BaseType.ENUM,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )
