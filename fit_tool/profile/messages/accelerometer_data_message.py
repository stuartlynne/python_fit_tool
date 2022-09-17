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


class AccelerometerDataMessage(DataMessage):
    ID = 165
    NAME = 'accelerometer_data'

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
        super().__init__(name=AccelerometerDataMessage.NAME,
                         global_id=AccelerometerDataMessage.ID,
                         local_id=definition_message.local_id if definition_message else local_id,
                         endian=definition_message.endian if definition_message else endian,
                         definition_message=definition_message,
                         developer_fields=developer_fields,
                         fields=[
        TimestampField(
            size=self.__get_field_size(definition_message, TimestampField.ID),
            growable=definition_message is None), 
        AccelerometerDataTimestampMsField(
            size=self.__get_field_size(definition_message, AccelerometerDataTimestampMsField.ID),
            growable=definition_message is None), 
        AccelerometerDataSampleTimeOffsetField(
            size=self.__get_field_size(definition_message, AccelerometerDataSampleTimeOffsetField.ID),
            growable=definition_message is None), 
        AccelerometerDataAccelXField(
            size=self.__get_field_size(definition_message, AccelerometerDataAccelXField.ID),
            growable=definition_message is None), 
        AccelerometerDataAccelYField(
            size=self.__get_field_size(definition_message, AccelerometerDataAccelYField.ID),
            growable=definition_message is None), 
        AccelerometerDataAccelZField(
            size=self.__get_field_size(definition_message, AccelerometerDataAccelZField.ID),
            growable=definition_message is None), 
        AccelerometerDataCalibratedAccelXField(
            size=self.__get_field_size(definition_message, AccelerometerDataCalibratedAccelXField.ID),
            growable=definition_message is None), 
        AccelerometerDataCalibratedAccelYField(
            size=self.__get_field_size(definition_message, AccelerometerDataCalibratedAccelYField.ID),
            growable=definition_message is None), 
        AccelerometerDataCalibratedAccelZField(
            size=self.__get_field_size(definition_message, AccelerometerDataCalibratedAccelZField.ID),
            growable=definition_message is None), 
        AccelerometerDataCompressedCalibratedAccelXField(
            size=self.__get_field_size(definition_message, AccelerometerDataCompressedCalibratedAccelXField.ID),
            growable=definition_message is None), 
        AccelerometerDataCompressedCalibratedAccelYField(
            size=self.__get_field_size(definition_message, AccelerometerDataCompressedCalibratedAccelYField.ID),
            growable=definition_message is None), 
        AccelerometerDataCompressedCalibratedAccelZField(
            size=self.__get_field_size(definition_message, AccelerometerDataCompressedCalibratedAccelZField.ID),
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
    def timestamp_ms(self) -> Optional[int]:
        field = self.get_field(AccelerometerDataTimestampMsField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @timestamp_ms.setter
    def timestamp_ms(self, value: int):
        field = self.get_field(AccelerometerDataTimestampMsField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def sample_time_offset(self) -> Optional[int]:
        field = self.get_field(AccelerometerDataSampleTimeOffsetField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @sample_time_offset.setter
    def sample_time_offset(self, value: int):
        field = self.get_field(AccelerometerDataSampleTimeOffsetField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def accel_x(self) -> Optional[int]:
        field = self.get_field(AccelerometerDataAccelXField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @accel_x.setter
    def accel_x(self, value: int):
        field = self.get_field(AccelerometerDataAccelXField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def accel_y(self) -> Optional[int]:
        field = self.get_field(AccelerometerDataAccelYField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @accel_y.setter
    def accel_y(self, value: int):
        field = self.get_field(AccelerometerDataAccelYField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def accel_z(self) -> Optional[int]:
        field = self.get_field(AccelerometerDataAccelZField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @accel_z.setter
    def accel_z(self, value: int):
        field = self.get_field(AccelerometerDataAccelZField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def calibrated_accel_x(self) -> Optional[float]:
        field = self.get_field(AccelerometerDataCalibratedAccelXField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @calibrated_accel_x.setter
    def calibrated_accel_x(self, value: float):
        field = self.get_field(AccelerometerDataCalibratedAccelXField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def calibrated_accel_y(self) -> Optional[float]:
        field = self.get_field(AccelerometerDataCalibratedAccelYField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @calibrated_accel_y.setter
    def calibrated_accel_y(self, value: float):
        field = self.get_field(AccelerometerDataCalibratedAccelYField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def calibrated_accel_z(self) -> Optional[float]:
        field = self.get_field(AccelerometerDataCalibratedAccelZField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @calibrated_accel_z.setter
    def calibrated_accel_z(self, value: float):
        field = self.get_field(AccelerometerDataCalibratedAccelZField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def compressed_calibrated_accel_x(self) -> Optional[int]:
        field = self.get_field(AccelerometerDataCompressedCalibratedAccelXField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @compressed_calibrated_accel_x.setter
    def compressed_calibrated_accel_x(self, value: int):
        field = self.get_field(AccelerometerDataCompressedCalibratedAccelXField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def compressed_calibrated_accel_y(self) -> Optional[int]:
        field = self.get_field(AccelerometerDataCompressedCalibratedAccelYField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @compressed_calibrated_accel_y.setter
    def compressed_calibrated_accel_y(self, value: int):
        field = self.get_field(AccelerometerDataCompressedCalibratedAccelYField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def compressed_calibrated_accel_z(self) -> Optional[int]:
        field = self.get_field(AccelerometerDataCompressedCalibratedAccelZField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @compressed_calibrated_accel_z.setter
    def compressed_calibrated_accel_z(self, value: int):
        field = self.get_field(AccelerometerDataCompressedCalibratedAccelZField.ID)

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
        offset = -631065600000,
                 scale = 0.001,
                         size = size,
        units = 'ms',
        type_name = 'date_time',
        growable = growable,
                   sub_fields = [
        ]
        )


class AccelerometerDataTimestampMsField(Field):
    ID = 0

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='timestamp_ms',
            field_id=self.ID,
            base_type=BaseType.UINT16,
        offset = 0,
                 scale = 1,
                         size = size,
        units = 'ms',
        type_name = '',
        growable = growable,
                   sub_fields = [
        ]
        )


class AccelerometerDataSampleTimeOffsetField(Field):
    ID = 1

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='sample_time_offset',
            field_id=self.ID,
            base_type=BaseType.UINT16,
        offset = 0,
                 scale = 1,
                         size = size,
        units = 'ms',
        type_name = '',
        growable = growable,
                   sub_fields = [
        ]
        )


class AccelerometerDataAccelXField(Field):
    ID = 2

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='accel_x',
            field_id=self.ID,
            base_type=BaseType.UINT16,
        offset = 0,
                 scale = 1,
                         size = size,
        units = 'counts',
        type_name = '',
        growable = growable,
                   sub_fields = [
        ]
        )


class AccelerometerDataAccelYField(Field):
    ID = 3

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='accel_y',
            field_id=self.ID,
            base_type=BaseType.UINT16,
        offset = 0,
                 scale = 1,
                         size = size,
        units = 'counts',
        type_name = '',
        growable = growable,
                   sub_fields = [
        ]
        )


class AccelerometerDataAccelZField(Field):
    ID = 4

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='accel_z',
            field_id=self.ID,
            base_type=BaseType.UINT16,
        offset = 0,
                 scale = 1,
                         size = size,
        units = 'counts',
        type_name = '',
        growable = growable,
                   sub_fields = [
        ]
        )


class AccelerometerDataCalibratedAccelXField(Field):
    ID = 5

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='calibrated_accel_x',
            field_id=self.ID,
            base_type=BaseType.FLOAT32,
        offset = 0,
                 scale = 1,
                         size = size,
        units = 'g',
        type_name = '',
        growable = growable,
                   sub_fields = [
        ]
        )


class AccelerometerDataCalibratedAccelYField(Field):
    ID = 6

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='calibrated_accel_y',
            field_id=self.ID,
            base_type=BaseType.FLOAT32,
        offset = 0,
                 scale = 1,
                         size = size,
        units = 'g',
        type_name = '',
        growable = growable,
                   sub_fields = [
        ]
        )


class AccelerometerDataCalibratedAccelZField(Field):
    ID = 7

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='calibrated_accel_z',
            field_id=self.ID,
            base_type=BaseType.FLOAT32,
        offset = 0,
                 scale = 1,
                         size = size,
        units = 'g',
        type_name = '',
        growable = growable,
                   sub_fields = [
        ]
        )


class AccelerometerDataCompressedCalibratedAccelXField(Field):
    ID = 8

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='compressed_calibrated_accel_x',
            field_id=self.ID,
            base_type=BaseType.SINT16,
        offset = 0,
                 scale = 1,
                         size = size,
        units = 'mG',
        type_name = '',
        growable = growable,
                   sub_fields = [
        ]
        )


class AccelerometerDataCompressedCalibratedAccelYField(Field):
    ID = 9

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='compressed_calibrated_accel_y',
            field_id=self.ID,
            base_type=BaseType.SINT16,
        offset = 0,
                 scale = 1,
                         size = size,
        units = 'mG',
        type_name = '',
        growable = growable,
                   sub_fields = [
        ]
        )


class AccelerometerDataCompressedCalibratedAccelZField(Field):
    ID = 10

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='compressed_calibrated_accel_z',
            field_id=self.ID,
            base_type=BaseType.SINT16,
        offset = 0,
                 scale = 1,
                         size = size,
        units = 'mG',
        type_name = '',
        growable = growable,
                   sub_fields = [
        ]
        )