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


class MonitoringInfoMessage(DataMessage):
    ID = 103
    NAME = 'monitoring_info'

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
        super().__init__(name=MonitoringInfoMessage.NAME,
                         global_id=MonitoringInfoMessage.ID,
                         local_id=definition_message.local_id if definition_message else local_id,
                         endian=definition_message.endian if definition_message else endian,
                         definition_message=definition_message,
                         developer_fields=developer_fields,
                         fields=[
        TimestampField(
            size=self.__get_field_size(definition_message, TimestampField.ID),
            growable=definition_message is None), 
        MonitoringInfoLocalTimestampField(
            size=self.__get_field_size(definition_message, MonitoringInfoLocalTimestampField.ID),
            growable=definition_message is None), 
        MonitoringInfoActivityTypeField(
            size=self.__get_field_size(definition_message, MonitoringInfoActivityTypeField.ID),
            growable=definition_message is None), 
        MonitoringInfoCyclesToDistanceField(
            size=self.__get_field_size(definition_message, MonitoringInfoCyclesToDistanceField.ID),
            growable=definition_message is None), 
        MonitoringInfoCyclesToCaloriesField(
            size=self.__get_field_size(definition_message, MonitoringInfoCyclesToCaloriesField.ID),
            growable=definition_message is None), 
        MonitoringInfoRestingMetabolicRateField(
            size=self.__get_field_size(definition_message, MonitoringInfoRestingMetabolicRateField.ID),
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
    def local_timestamp(self) -> Optional[int]:
        field = self.get_field(MonitoringInfoLocalTimestampField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @local_timestamp.setter
    def local_timestamp(self, value: int):
        field = self.get_field(MonitoringInfoLocalTimestampField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def activity_type(self) -> Optional[ActivityType]:
        field = self.get_field(MonitoringInfoActivityTypeField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @activity_type.setter
    def activity_type(self, value: ActivityType):
        field = self.get_field(MonitoringInfoActivityTypeField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def cycles_to_distance(self) -> Optional[float]:
        field = self.get_field(MonitoringInfoCyclesToDistanceField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @cycles_to_distance.setter
    def cycles_to_distance(self, value: float):
        field = self.get_field(MonitoringInfoCyclesToDistanceField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def cycles_to_calories(self) -> Optional[float]:
        field = self.get_field(MonitoringInfoCyclesToCaloriesField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @cycles_to_calories.setter
    def cycles_to_calories(self, value: float):
        field = self.get_field(MonitoringInfoCyclesToCaloriesField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def resting_metabolic_rate(self) -> Optional[int]:
        field = self.get_field(MonitoringInfoRestingMetabolicRateField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @resting_metabolic_rate.setter
    def resting_metabolic_rate(self, value: int):
        field = self.get_field(MonitoringInfoRestingMetabolicRateField.ID)

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


class MonitoringInfoLocalTimestampField(Field):
    ID = 0

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='local_timestamp',
            field_id=self.ID,
            base_type=BaseType.UINT32,
        offset = 0,
                 scale = 1,
                         size = size,
        units = 's',
        type_name = 'local_date_time',
        growable = growable,
                   sub_fields = [
        ]
        )


class MonitoringInfoActivityTypeField(Field):
    ID = 1

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='activity_type',
            field_id=self.ID,
            base_type=BaseType.ENUM,
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        ]
        )


class MonitoringInfoCyclesToDistanceField(Field):
    ID = 3

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='cycles_to_distance',
            field_id=self.ID,
            base_type=BaseType.UINT16,
        offset = 0,
                 scale = 5000,
                         size = size,
        units = 'm/cycle',
        type_name = '',
        growable = growable,
                   sub_fields = [
        ]
        )


class MonitoringInfoCyclesToCaloriesField(Field):
    ID = 4

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='cycles_to_calories',
            field_id=self.ID,
            base_type=BaseType.UINT16,
        offset = 0,
                 scale = 5000,
                         size = size,
        units = 'kcal/cycle',
        type_name = '',
        growable = growable,
                   sub_fields = [
        ]
        )


class MonitoringInfoRestingMetabolicRateField(Field):
    ID = 5

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='resting_metabolic_rate',
            field_id=self.ID,
            base_type=BaseType.UINT16,
        offset = 0,
                 scale = 1,
                         size = size,
        units = 'kcal / day',
        type_name = '',
        growable = growable,
                   sub_fields = [
        ]
        )