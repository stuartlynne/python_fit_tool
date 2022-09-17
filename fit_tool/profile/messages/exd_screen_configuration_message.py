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


class ExdScreenConfigurationMessage(DataMessage):
    ID = 200
    NAME = 'exd_screen_configuration'

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
        super().__init__(name=ExdScreenConfigurationMessage.NAME,
                         global_id=ExdScreenConfigurationMessage.ID,
                         local_id=definition_message.local_id if definition_message else local_id,
                         endian=definition_message.endian if definition_message else endian,
                         definition_message=definition_message,
                         developer_fields=developer_fields,
                         fields=[
        ExdScreenConfigurationScreenIndexField(
            size=self.__get_field_size(definition_message, ExdScreenConfigurationScreenIndexField.ID),
            growable=definition_message is None), 
        ExdScreenConfigurationFieldCountField(
            size=self.__get_field_size(definition_message, ExdScreenConfigurationFieldCountField.ID),
            growable=definition_message is None), 
        ExdScreenConfigurationLayoutField(
            size=self.__get_field_size(definition_message, ExdScreenConfigurationLayoutField.ID),
            growable=definition_message is None), 
        ExdScreenConfigurationScreenEnabledField(
            size=self.__get_field_size(definition_message, ExdScreenConfigurationScreenEnabledField.ID),
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
    def screen_index(self) -> Optional[int]:
        field = self.get_field(ExdScreenConfigurationScreenIndexField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @screen_index.setter
    def screen_index(self, value: int):
        field = self.get_field(ExdScreenConfigurationScreenIndexField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def field_count(self) -> Optional[int]:
        field = self.get_field(ExdScreenConfigurationFieldCountField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @field_count.setter
    def field_count(self, value: int):
        field = self.get_field(ExdScreenConfigurationFieldCountField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def layout(self) -> Optional[ExdLayout]:
        field = self.get_field(ExdScreenConfigurationLayoutField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @layout.setter
    def layout(self, value: ExdLayout):
        field = self.get_field(ExdScreenConfigurationLayoutField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def screen_enabled(self) -> Optional[bool]:
        field = self.get_field(ExdScreenConfigurationScreenEnabledField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @screen_enabled.setter
    def screen_enabled(self, value: bool):
        field = self.get_field(ExdScreenConfigurationScreenEnabledField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    





class ExdScreenConfigurationScreenIndexField(Field):
    ID = 0

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='screen_index',
            field_id=self.ID,
            base_type=BaseType.UINT8,
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        ]
        )


class ExdScreenConfigurationFieldCountField(Field):
    ID = 1

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='field_count',
            field_id=self.ID,
            base_type=BaseType.UINT8,
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        ]
        )


class ExdScreenConfigurationLayoutField(Field):
    ID = 2

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='layout',
            field_id=self.ID,
            base_type=BaseType.ENUM,
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        ]
        )


class ExdScreenConfigurationScreenEnabledField(Field):
    ID = 3

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='screen_enabled',
            field_id=self.ID,
            base_type=BaseType.UINT8,
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        ]
        )