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


class MemoGlobMessage(DataMessage):
    ID = 145
    NAME = 'memo_glob'

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
        super().__init__(name=MemoGlobMessage.NAME,
                         global_id=MemoGlobMessage.ID,
                         local_id=definition_message.local_id if definition_message else local_id,
                         endian=definition_message.endian if definition_message else endian,
                         definition_message=definition_message,
                         developer_fields=developer_fields,
                         fields=[
        MemoGlobPartIndexField(
            size=self.__get_field_size(definition_message, MemoGlobPartIndexField.ID),
            growable=definition_message is None), 
        MemoGlobMemoField(
            size=self.__get_field_size(definition_message, MemoGlobMemoField.ID),
            growable=definition_message is None), 
        MemoGlobMessageNumberField(
            size=self.__get_field_size(definition_message, MemoGlobMessageNumberField.ID),
            growable=definition_message is None), 
        MemoGlobMessageIndexField(
            size=self.__get_field_size(definition_message, MemoGlobMessageIndexField.ID),
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
    def part_index(self) -> Optional[int]:
        field = self.get_field(MemoGlobPartIndexField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @part_index.setter
    def part_index(self, value: int):
        field = self.get_field(MemoGlobPartIndexField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def memo(self) -> Optional[int]:
        field = self.get_field(MemoGlobMemoField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @memo.setter
    def memo(self, value: int):
        field = self.get_field(MemoGlobMemoField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def message_number(self) -> Optional[int]:
        field = self.get_field(MemoGlobMessageNumberField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @message_number.setter
    def message_number(self, value: int):
        field = self.get_field(MemoGlobMessageNumberField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def message_index(self) -> Optional[int]:
        field = self.get_field(MemoGlobMessageIndexField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @message_index.setter
    def message_index(self, value: int):
        field = self.get_field(MemoGlobMessageIndexField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    





class MemoGlobPartIndexField(Field):
    ID = 250

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='part_index',
            field_id=self.ID,
            base_type=BaseType.UINT32,
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        ]
        )


class MemoGlobMemoField(Field):
    ID = 0

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='memo',
            field_id=self.ID,
            base_type=BaseType.BYTE,
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        ]
        )


class MemoGlobMessageNumberField(Field):
    ID = 1

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='message_number',
            field_id=self.ID,
            base_type=BaseType.UINT16,
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        ]
        )


class MemoGlobMessageIndexField(Field):
    ID = 2

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='message_index',
            field_id=self.ID,
            base_type=BaseType.UINT16,
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        ]
        )