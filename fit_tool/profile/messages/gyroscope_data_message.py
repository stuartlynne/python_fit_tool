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


class GyroscopeDataMessage(DataMessage):
    ID = 164
    NAME = 'gyroscope_data'

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
        super().__init__(name=GyroscopeDataMessage.NAME,
                         global_id=GyroscopeDataMessage.ID,
                         local_id=definition_message.local_id if definition_message else local_id,
                         endian=definition_message.endian if definition_message else endian,
                         definition_message=definition_message,
                         developer_fields=developer_fields,
                         fields=[
                             TimestampField(
                                 size=self.__get_field_size(definition_message, TimestampField.ID),
                                 growable=definition_message is None),
                             GyroscopeDataTimestampMsField(
                                 size=self.__get_field_size(definition_message, GyroscopeDataTimestampMsField.ID),
                                 growable=definition_message is None),
                             GyroscopeDataSampleTimeOffsetField(
                                 size=self.__get_field_size(definition_message, GyroscopeDataSampleTimeOffsetField.ID),
                                 growable=definition_message is None),
                             GyroscopeDataGyroXField(
                                 size=self.__get_field_size(definition_message, GyroscopeDataGyroXField.ID),
                                 growable=definition_message is None),
                             GyroscopeDataGyroYField(
                                 size=self.__get_field_size(definition_message, GyroscopeDataGyroYField.ID),
                                 growable=definition_message is None),
                             GyroscopeDataGyroZField(
                                 size=self.__get_field_size(definition_message, GyroscopeDataGyroZField.ID),
                                 growable=definition_message is None),
                             GyroscopeDataCalibratedGyroXField(
                                 size=self.__get_field_size(definition_message, GyroscopeDataCalibratedGyroXField.ID),
                                 growable=definition_message is None),
                             GyroscopeDataCalibratedGyroYField(
                                 size=self.__get_field_size(definition_message, GyroscopeDataCalibratedGyroYField.ID),
                                 growable=definition_message is None),
                             GyroscopeDataCalibratedGyroZField(
                                 size=self.__get_field_size(definition_message, GyroscopeDataCalibratedGyroZField.ID),
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
        field = self.get_field(GyroscopeDataTimestampMsField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @timestamp_ms.setter
    def timestamp_ms(self, value: int):
        field = self.get_field(GyroscopeDataTimestampMsField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def sample_time_offset(self) -> Optional[int]:
        field = self.get_field(GyroscopeDataSampleTimeOffsetField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @sample_time_offset.setter
    def sample_time_offset(self, value: int):
        field = self.get_field(GyroscopeDataSampleTimeOffsetField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def gyro_x(self) -> Optional[int]:
        field = self.get_field(GyroscopeDataGyroXField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @gyro_x.setter
    def gyro_x(self, value: int):
        field = self.get_field(GyroscopeDataGyroXField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def gyro_y(self) -> Optional[int]:
        field = self.get_field(GyroscopeDataGyroYField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @gyro_y.setter
    def gyro_y(self, value: int):
        field = self.get_field(GyroscopeDataGyroYField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def gyro_z(self) -> Optional[int]:
        field = self.get_field(GyroscopeDataGyroZField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @gyro_z.setter
    def gyro_z(self, value: int):
        field = self.get_field(GyroscopeDataGyroZField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def calibrated_gyro_x(self) -> Optional[float]:
        field = self.get_field(GyroscopeDataCalibratedGyroXField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @calibrated_gyro_x.setter
    def calibrated_gyro_x(self, value: float):
        field = self.get_field(GyroscopeDataCalibratedGyroXField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def calibrated_gyro_y(self) -> Optional[float]:
        field = self.get_field(GyroscopeDataCalibratedGyroYField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @calibrated_gyro_y.setter
    def calibrated_gyro_y(self, value: float):
        field = self.get_field(GyroscopeDataCalibratedGyroYField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def calibrated_gyro_z(self) -> Optional[float]:
        field = self.get_field(GyroscopeDataCalibratedGyroZField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @calibrated_gyro_z.setter
    def calibrated_gyro_z(self, value: float):
        field = self.get_field(GyroscopeDataCalibratedGyroZField.ID)

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


class GyroscopeDataTimestampMsField(Field):
    ID = 0

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='timestamp_ms',
            field_id=self.ID,
            base_type=BaseType.UINT16,
            offset=0,
            scale=1,
            size=size,
            units='ms',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )


class GyroscopeDataSampleTimeOffsetField(Field):
    ID = 1

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='sample_time_offset',
            field_id=self.ID,
            base_type=BaseType.UINT16,
            offset=0,
            scale=1,
            size=size,
            units='ms',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )


class GyroscopeDataGyroXField(Field):
    ID = 2

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='gyro_x',
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


class GyroscopeDataGyroYField(Field):
    ID = 3

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='gyro_y',
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


class GyroscopeDataGyroZField(Field):
    ID = 4

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='gyro_z',
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


class GyroscopeDataCalibratedGyroXField(Field):
    ID = 5

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='calibrated_gyro_x',
            field_id=self.ID,
            base_type=BaseType.FLOAT32,
            offset=0,
            scale=1,
            size=size,
            units='deg/s',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )


class GyroscopeDataCalibratedGyroYField(Field):
    ID = 6

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='calibrated_gyro_y',
            field_id=self.ID,
            base_type=BaseType.FLOAT32,
            offset=0,
            scale=1,
            size=size,
            units='deg/s',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )


class GyroscopeDataCalibratedGyroZField(Field):
    ID = 7

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='calibrated_gyro_z',
            field_id=self.ID,
            base_type=BaseType.FLOAT32,
            offset=0,
            scale=1,
            size=size,
            units='deg/s',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )
