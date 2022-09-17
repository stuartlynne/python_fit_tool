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


class GpsMetadataMessage(DataMessage):
    ID = 160
    NAME = 'gps_metadata'

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
        super().__init__(name=GpsMetadataMessage.NAME,
                         global_id=GpsMetadataMessage.ID,
                         local_id=definition_message.local_id if definition_message else local_id,
                         endian=definition_message.endian if definition_message else endian,
                         definition_message=definition_message,
                         developer_fields=developer_fields,
                         fields=[
        TimestampField(
            size=self.__get_field_size(definition_message, TimestampField.ID),
            growable=definition_message is None), 
        GpsMetadataTimestampMsField(
            size=self.__get_field_size(definition_message, GpsMetadataTimestampMsField.ID),
            growable=definition_message is None), 
        GpsMetadataPositionLatField(
            size=self.__get_field_size(definition_message, GpsMetadataPositionLatField.ID),
            growable=definition_message is None), 
        GpsMetadataPositionLongField(
            size=self.__get_field_size(definition_message, GpsMetadataPositionLongField.ID),
            growable=definition_message is None), 
        GpsMetadataEnhancedAltitudeField(
            size=self.__get_field_size(definition_message, GpsMetadataEnhancedAltitudeField.ID),
            growable=definition_message is None), 
        GpsMetadataEnhancedSpeedField(
            size=self.__get_field_size(definition_message, GpsMetadataEnhancedSpeedField.ID),
            growable=definition_message is None), 
        GpsMetadataHeadingField(
            size=self.__get_field_size(definition_message, GpsMetadataHeadingField.ID),
            growable=definition_message is None), 
        GpsMetadataUtcTimestampField(
            size=self.__get_field_size(definition_message, GpsMetadataUtcTimestampField.ID),
            growable=definition_message is None), 
        GpsMetadataVelocityField(
            size=self.__get_field_size(definition_message, GpsMetadataVelocityField.ID),
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
        field = self.get_field(GpsMetadataTimestampMsField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @timestamp_ms.setter
    def timestamp_ms(self, value: int):
        field = self.get_field(GpsMetadataTimestampMsField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def position_lat(self) -> Optional[float]:
        field = self.get_field(GpsMetadataPositionLatField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @position_lat.setter
    def position_lat(self, value: float):
        field = self.get_field(GpsMetadataPositionLatField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def position_long(self) -> Optional[float]:
        field = self.get_field(GpsMetadataPositionLongField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @position_long.setter
    def position_long(self, value: float):
        field = self.get_field(GpsMetadataPositionLongField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def enhanced_altitude(self) -> Optional[float]:
        field = self.get_field(GpsMetadataEnhancedAltitudeField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @enhanced_altitude.setter
    def enhanced_altitude(self, value: float):
        field = self.get_field(GpsMetadataEnhancedAltitudeField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def enhanced_speed(self) -> Optional[float]:
        field = self.get_field(GpsMetadataEnhancedSpeedField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @enhanced_speed.setter
    def enhanced_speed(self, value: float):
        field = self.get_field(GpsMetadataEnhancedSpeedField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def heading(self) -> Optional[float]:
        field = self.get_field(GpsMetadataHeadingField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @heading.setter
    def heading(self, value: float):
        field = self.get_field(GpsMetadataHeadingField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    
# timestamp : milliseconds from January 1st, 1970 at 00:00:00 UTC

    @property
    def utc_timestamp(self) -> Optional[int]:
        field = self.get_field(GpsMetadataUtcTimestampField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None


    # timestamp : milliseconds from January 1st, 1970 at 00:00:00 UTC

    @utc_timestamp.setter
    def utc_timestamp(self, value: int):
        field = self.get_field(GpsMetadataUtcTimestampField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def velocity(self) -> Optional[float]:
        field = self.get_field(GpsMetadataVelocityField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @velocity.setter
    def velocity(self, value: float):
        field = self.get_field(GpsMetadataVelocityField.ID)

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


class GpsMetadataTimestampMsField(Field):
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


class GpsMetadataPositionLatField(Field):
    ID = 1

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='position_lat',
            field_id=self.ID,
            base_type=BaseType.SINT32,
        offset = 0,
                 scale = 11930464.711111112,
                         size = size,
        units = 'degrees',
        type_name = '',
        growable = growable,
                   sub_fields = [
        ]
        )


class GpsMetadataPositionLongField(Field):
    ID = 2

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='position_long',
            field_id=self.ID,
            base_type=BaseType.SINT32,
        offset = 0,
                 scale = 11930464.711111112,
                         size = size,
        units = 'degrees',
        type_name = '',
        growable = growable,
                   sub_fields = [
        ]
        )


class GpsMetadataEnhancedAltitudeField(Field):
    ID = 3

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='enhanced_altitude',
            field_id=self.ID,
            base_type=BaseType.UINT32,
        offset = 500,
                 scale = 5,
                         size = size,
        units = 'm',
        type_name = '',
        growable = growable,
                   sub_fields = [
        ]
        )


class GpsMetadataEnhancedSpeedField(Field):
    ID = 4

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='enhanced_speed',
            field_id=self.ID,
            base_type=BaseType.UINT32,
        offset = 0,
                 scale = 1000,
                         size = size,
        units = 'm/s',
        type_name = '',
        growable = growable,
                   sub_fields = [
        ]
        )


class GpsMetadataHeadingField(Field):
    ID = 5

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='heading',
            field_id=self.ID,
            base_type=BaseType.UINT16,
        offset = 0,
                 scale = 100,
                         size = size,
        units = 'degrees',
        type_name = '',
        growable = growable,
                   sub_fields = [
        ]
        )


class GpsMetadataUtcTimestampField(Field):
    ID = 6

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='utc_timestamp',
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


class GpsMetadataVelocityField(Field):
    ID = 7

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='velocity',
            field_id=self.ID,
            base_type=BaseType.SINT16,
        offset = 0,
                 scale = 100,
                         size = size,
        units = 'm/s',
        type_name = '',
        growable = growable,
                   sub_fields = [
        ]
        )