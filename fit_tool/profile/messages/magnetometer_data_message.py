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


class MagnetometerDataMessage(DataMessage):
    ID = 208
    NAME = 'magnetometer_data'

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
        super().__init__(name=MagnetometerDataMessage.NAME,
                         global_id=MagnetometerDataMessage.ID,
                         local_id=definition_message.local_id if definition_message else local_id,
                         endian=definition_message.endian if definition_message else endian,
                         definition_message=definition_message,
                         developer_fields=developer_fields,
                         fields=[
                             TimestampField(
                                 size=self.__get_field_size(definition_message, TimestampField.ID),
                                 growable=definition_message is None),
                             MagnetometerDataTimestampMsField(
                                 size=self.__get_field_size(definition_message, MagnetometerDataTimestampMsField.ID),
                                 growable=definition_message is None),
                             MagnetometerDataSampleTimeOffsetField(
                                 size=self.__get_field_size(definition_message,
                                                            MagnetometerDataSampleTimeOffsetField.ID),
                                 growable=definition_message is None),
                             MagnetometerDataMagXField(
                                 size=self.__get_field_size(definition_message, MagnetometerDataMagXField.ID),
                                 growable=definition_message is None),
                             MagnetometerDataMagYField(
                                 size=self.__get_field_size(definition_message, MagnetometerDataMagYField.ID),
                                 growable=definition_message is None),
                             MagnetometerDataMagZField(
                                 size=self.__get_field_size(definition_message, MagnetometerDataMagZField.ID),
                                 growable=definition_message is None),
                             MagnetometerDataCalibratedMagXField(
                                 size=self.__get_field_size(definition_message, MagnetometerDataCalibratedMagXField.ID),
                                 growable=definition_message is None),
                             MagnetometerDataCalibratedMagYField(
                                 size=self.__get_field_size(definition_message, MagnetometerDataCalibratedMagYField.ID),
                                 growable=definition_message is None),
                             MagnetometerDataCalibratedMagZField(
                                 size=self.__get_field_size(definition_message, MagnetometerDataCalibratedMagZField.ID),
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
        field = self.get_field(MagnetometerDataTimestampMsField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @timestamp_ms.setter
    def timestamp_ms(self, value: int):
        field = self.get_field(MagnetometerDataTimestampMsField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def sample_time_offset(self) -> Optional[int]:
        field = self.get_field(MagnetometerDataSampleTimeOffsetField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @sample_time_offset.setter
    def sample_time_offset(self, value: int):
        field = self.get_field(MagnetometerDataSampleTimeOffsetField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def mag_x(self) -> Optional[int]:
        field = self.get_field(MagnetometerDataMagXField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @mag_x.setter
    def mag_x(self, value: int):
        field = self.get_field(MagnetometerDataMagXField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def mag_y(self) -> Optional[int]:
        field = self.get_field(MagnetometerDataMagYField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @mag_y.setter
    def mag_y(self, value: int):
        field = self.get_field(MagnetometerDataMagYField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def mag_z(self) -> Optional[int]:
        field = self.get_field(MagnetometerDataMagZField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @mag_z.setter
    def mag_z(self, value: int):
        field = self.get_field(MagnetometerDataMagZField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def calibrated_mag_x(self) -> Optional[float]:
        field = self.get_field(MagnetometerDataCalibratedMagXField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @calibrated_mag_x.setter
    def calibrated_mag_x(self, value: float):
        field = self.get_field(MagnetometerDataCalibratedMagXField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def calibrated_mag_y(self) -> Optional[float]:
        field = self.get_field(MagnetometerDataCalibratedMagYField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @calibrated_mag_y.setter
    def calibrated_mag_y(self, value: float):
        field = self.get_field(MagnetometerDataCalibratedMagYField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def calibrated_mag_z(self) -> Optional[float]:
        field = self.get_field(MagnetometerDataCalibratedMagZField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @calibrated_mag_z.setter
    def calibrated_mag_z(self, value: float):
        field = self.get_field(MagnetometerDataCalibratedMagZField.ID)

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


class MagnetometerDataTimestampMsField(Field):
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


class MagnetometerDataSampleTimeOffsetField(Field):
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


class MagnetometerDataMagXField(Field):
    ID = 2

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='mag_x',
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


class MagnetometerDataMagYField(Field):
    ID = 3

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='mag_y',
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


class MagnetometerDataMagZField(Field):
    ID = 4

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='mag_z',
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


class MagnetometerDataCalibratedMagXField(Field):
    ID = 5

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='calibrated_mag_x',
            field_id=self.ID,
            base_type=BaseType.FLOAT32,
            offset=0,
            scale=1,
            size=size,
            units='G',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )


class MagnetometerDataCalibratedMagYField(Field):
    ID = 6

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='calibrated_mag_y',
            field_id=self.ID,
            base_type=BaseType.FLOAT32,
            offset=0,
            scale=1,
            size=size,
            units='G',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )


class MagnetometerDataCalibratedMagZField(Field):
    ID = 7

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='calibrated_mag_z',
            field_id=self.ID,
            base_type=BaseType.FLOAT32,
            offset=0,
            scale=1,
            size=size,
            units='G',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )
