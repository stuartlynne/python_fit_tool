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


class FileIdMessage(DataMessage):
    ID = 0
    NAME = 'file_id'

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
        super().__init__(name=FileIdMessage.NAME,
                         global_id=FileIdMessage.ID,
                         local_id=definition_message.local_id if definition_message else local_id,
                         endian=definition_message.endian if definition_message else endian,
                         definition_message=definition_message,
                         developer_fields=developer_fields,
                         fields=[
        FileIdTypeField(
            size=self.__get_field_size(definition_message, FileIdTypeField.ID),
            growable=definition_message is None), 
        FileIdManufacturerField(
            size=self.__get_field_size(definition_message, FileIdManufacturerField.ID),
            growable=definition_message is None), 
        FileIdProductField(
            size=self.__get_field_size(definition_message, FileIdProductField.ID),
            growable=definition_message is None), 
        FileIdSerialNumberField(
            size=self.__get_field_size(definition_message, FileIdSerialNumberField.ID),
            growable=definition_message is None), 
        FileIdTimeCreatedField(
            size=self.__get_field_size(definition_message, FileIdTimeCreatedField.ID),
            growable=definition_message is None), 
        FileIdNumberField(
            size=self.__get_field_size(definition_message, FileIdNumberField.ID),
            growable=definition_message is None), 
        FileIdProductNameField(
            size=self.__get_field_size(definition_message, FileIdProductNameField.ID),
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
    def type(self) -> Optional[FileType]:
        field = self.get_field(FileIdTypeField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @type.setter
    def type(self, value: FileType):
        field = self.get_field(FileIdTypeField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def manufacturer(self) -> Optional[int]:
        field = self.get_field(FileIdManufacturerField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @manufacturer.setter
    def manufacturer(self, value: int):
        field = self.get_field(FileIdManufacturerField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def product(self) -> Optional[int]:
        field = self.get_field(FileIdProductField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @product.setter
    def product(self, value: int):
        field = self.get_field(FileIdProductField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    


    @property
    def favero_product(self) -> Optional[int]:
        field = self.get_field(FileIdProductField.ID)
        type_field = self.get_field(FileIdManufacturerField.ID)

        is_sub_field_valid = type_field and type_field.get_value() in [263]
        if field and field.is_valid() and is_sub_field_valid:
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @favero_product.setter
    def favero_product(self, value: int):
        field = self.get_field(FileIdProductField.ID)
        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)


    @property
    def garmin_product(self) -> Optional[int]:
        field = self.get_field(FileIdProductField.ID)
        type_field = self.get_field(FileIdManufacturerField.ID)

        is_sub_field_valid = type_field and type_field.get_value() in [1, 15, 13, 89]
        if field and field.is_valid() and is_sub_field_valid:
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @garmin_product.setter
    def garmin_product(self, value: int):
        field = self.get_field(FileIdProductField.ID)
        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def serial_number(self) -> Optional[int]:
        field = self.get_field(FileIdSerialNumberField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @serial_number.setter
    def serial_number(self, value: int):
        field = self.get_field(FileIdSerialNumberField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    
# timestamp : milliseconds from January 1st, 1970 at 00:00:00 UTC

    @property
    def time_created(self) -> Optional[int]:
        field = self.get_field(FileIdTimeCreatedField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None


    # timestamp : milliseconds from January 1st, 1970 at 00:00:00 UTC

    @time_created.setter
    def time_created(self, value: int):
        field = self.get_field(FileIdTimeCreatedField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def number(self) -> Optional[int]:
        field = self.get_field(FileIdNumberField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @number.setter
    def number(self, value: int):
        field = self.get_field(FileIdNumberField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def product_name(self) -> Optional[str]:
        field = self.get_field(FileIdProductNameField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @product_name.setter
    def product_name(self, value: str):
        field = self.get_field(FileIdProductNameField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    





class FileIdTypeField(Field):
    ID = 0

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='type',
            field_id=self.ID,
            base_type=BaseType.ENUM,
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        ]
        )


class FileIdManufacturerField(Field):
    ID = 1

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='manufacturer',
            field_id=self.ID,
            base_type=BaseType.UINT16,
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        ]
        )


class FileIdProductField(Field):
    ID = 2

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='product',
            field_id=self.ID,
            base_type=BaseType.UINT16,
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        SubField(
            name='favero_product',
            base_type=BaseType.UINT16,
        scale = 1,
                offset = 0,
        reference_map = {
        FileIdManufacturerField.ID: [263]
        }), 
        SubField(
            name='garmin_product',
            base_type=BaseType.UINT16,
        scale = 1,
                offset = 0,
        reference_map = {
        FileIdManufacturerField.ID: [1, 15, 13, 89]
        })
        ]
        )


class FileIdSerialNumberField(Field):
    ID = 3

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='serial_number',
            field_id=self.ID,
            base_type=BaseType.UINT32Z,
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        ]
        )


class FileIdTimeCreatedField(Field):
    ID = 4

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='time_created',
            field_id=self.ID,
            base_type=BaseType.UINT32,
        offset = -631065600000,
                 scale = 0.001,
                         size = size,
        units = 'ms',
        type_name = 'date_time',
        growable = growable,
                   sub_fields = [
        ]
        )


class FileIdNumberField(Field):
    ID = 5

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='number',
            field_id=self.ID,
            base_type=BaseType.UINT16,
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        ]
        )


class FileIdProductNameField(Field):
    ID = 8

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='product_name',
            field_id=self.ID,
            base_type=BaseType.STRING,
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        ]
        )