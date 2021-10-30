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
from fit_tool.profile.profile_type import *
from fit_tool.sub_field import SubField


class WatchfaceSettingsMessage(DataMessage):
    ID = 159
    NAME = 'watchface_settings'

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
        super().__init__(name=WatchfaceSettingsMessage.NAME,
                         global_id=WatchfaceSettingsMessage.ID,
                         local_id=definition_message.local_id if definition_message else local_id,
                         endian=definition_message.endian if definition_message else endian,
                         definition_message=definition_message,
                         developer_fields=developer_fields,
                         fields=[
                             MessageIndexField(
                                 size=self.__get_field_size(definition_message, MessageIndexField.ID),
                                 growable=definition_message is None),
                             WatchfaceSettingsModeField(
                                 size=self.__get_field_size(definition_message, WatchfaceSettingsModeField.ID),
                                 growable=definition_message is None),
                             WatchfaceSettingsLayoutField(
                                 size=self.__get_field_size(definition_message, WatchfaceSettingsLayoutField.ID),
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
    def mode(self) -> Optional[WatchfaceMode]:
        field = self.get_field(WatchfaceSettingsModeField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @mode.setter
    def mode(self, value: WatchfaceMode):
        field = self.get_field(WatchfaceSettingsModeField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def layout(self) -> Optional[int]:
        field = self.get_field(WatchfaceSettingsLayoutField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @layout.setter
    def layout(self, value: int):
        field = self.get_field(WatchfaceSettingsLayoutField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def digital_layout(self) -> Optional[DigitalWatchfaceLayout]:
        field = self.get_field(WatchfaceSettingsLayoutField.ID)
        type_field = self.get_field(WatchfaceSettingsModeField.ID)

        is_sub_field_valid = type_field and type_field.get_value() in [0]
        if field and field.is_valid() and is_sub_field_valid:
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @digital_layout.setter
    def digital_layout(self, value: DigitalWatchfaceLayout):
        field = self.get_field(WatchfaceSettingsLayoutField.ID)
        if field:
            if value:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)
            else:
                field.clear()

    @property
    def analog_layout(self) -> Optional[AnalogWatchfaceLayout]:
        field = self.get_field(WatchfaceSettingsLayoutField.ID)
        type_field = self.get_field(WatchfaceSettingsModeField.ID)

        is_sub_field_valid = type_field and type_field.get_value() in [1]
        if field and field.is_valid() and is_sub_field_valid:
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @analog_layout.setter
    def analog_layout(self, value: AnalogWatchfaceLayout):
        field = self.get_field(WatchfaceSettingsLayoutField.ID)
        if field:
            if value:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)
            else:
                field.clear()


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


class WatchfaceSettingsModeField(Field):
    ID = 0

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='mode',
            field_id=self.ID,
            base_type=BaseType.ENUM,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class WatchfaceSettingsLayoutField(Field):
    ID = 1

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='layout',
            field_id=self.ID,
            base_type=BaseType.BYTE,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
                SubField(
                    name='digital_layout',
                    base_type=BaseType.ENUM,
                    scale=1,
                    offset=0,
                    reference_map={
                        WatchfaceSettingsModeField.ID: [0]
                    }),
                SubField(
                    name='analog_layout',
                    base_type=BaseType.ENUM,
                    scale=1,
                    offset=0,
                    reference_map={
                        WatchfaceSettingsModeField.ID: [1]
                    })
            ]
        )
