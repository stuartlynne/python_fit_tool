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


class GoalMessage(DataMessage):
    ID = 15
    NAME = 'goal'

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
        super().__init__(name=GoalMessage.NAME,
                         global_id=GoalMessage.ID,
                         local_id=definition_message.local_id if definition_message else local_id,
                         endian=definition_message.endian if definition_message else endian,
                         definition_message=definition_message,
                         developer_fields=developer_fields,
                         fields=[
        MessageIndexField(
            size=self.__get_field_size(definition_message, MessageIndexField.ID),
            growable=definition_message is None), 
        GoalSportField(
            size=self.__get_field_size(definition_message, GoalSportField.ID),
            growable=definition_message is None), 
        GoalSubSportField(
            size=self.__get_field_size(definition_message, GoalSubSportField.ID),
            growable=definition_message is None), 
        GoalStartDateField(
            size=self.__get_field_size(definition_message, GoalStartDateField.ID),
            growable=definition_message is None), 
        GoalEndDateField(
            size=self.__get_field_size(definition_message, GoalEndDateField.ID),
            growable=definition_message is None), 
        GoalTypeField(
            size=self.__get_field_size(definition_message, GoalTypeField.ID),
            growable=definition_message is None), 
        GoalValueField(
            size=self.__get_field_size(definition_message, GoalValueField.ID),
            growable=definition_message is None), 
        GoalRepeatField(
            size=self.__get_field_size(definition_message, GoalRepeatField.ID),
            growable=definition_message is None), 
        GoalTargetValueField(
            size=self.__get_field_size(definition_message, GoalTargetValueField.ID),
            growable=definition_message is None), 
        GoalRecurrenceField(
            size=self.__get_field_size(definition_message, GoalRecurrenceField.ID),
            growable=definition_message is None), 
        GoalRecurrenceValueField(
            size=self.__get_field_size(definition_message, GoalRecurrenceValueField.ID),
            growable=definition_message is None), 
        GoalEnabledField(
            size=self.__get_field_size(definition_message, GoalEnabledField.ID),
            growable=definition_message is None), 
        GoalSourceField(
            size=self.__get_field_size(definition_message, GoalSourceField.ID),
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
    def sport(self) -> Optional[Sport]:
        field = self.get_field(GoalSportField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @sport.setter
    def sport(self, value: Sport):
        field = self.get_field(GoalSportField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def sub_sport(self) -> Optional[SubSport]:
        field = self.get_field(GoalSubSportField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @sub_sport.setter
    def sub_sport(self, value: SubSport):
        field = self.get_field(GoalSubSportField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    
# timestamp : milliseconds from January 1st, 1970 at 00:00:00 UTC

    @property
    def start_date(self) -> Optional[int]:
        field = self.get_field(GoalStartDateField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None


    # timestamp : milliseconds from January 1st, 1970 at 00:00:00 UTC

    @start_date.setter
    def start_date(self, value: int):
        field = self.get_field(GoalStartDateField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    
# timestamp : milliseconds from January 1st, 1970 at 00:00:00 UTC

    @property
    def end_date(self) -> Optional[int]:
        field = self.get_field(GoalEndDateField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None


    # timestamp : milliseconds from January 1st, 1970 at 00:00:00 UTC

    @end_date.setter
    def end_date(self, value: int):
        field = self.get_field(GoalEndDateField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def type(self) -> Optional[Goal]:
        field = self.get_field(GoalTypeField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @type.setter
    def type(self, value: Goal):
        field = self.get_field(GoalTypeField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def value(self) -> Optional[int]:
        field = self.get_field(GoalValueField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @value.setter
    def value(self, value: int):
        field = self.get_field(GoalValueField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def repeat(self) -> Optional[bool]:
        field = self.get_field(GoalRepeatField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @repeat.setter
    def repeat(self, value: bool):
        field = self.get_field(GoalRepeatField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def target_value(self) -> Optional[int]:
        field = self.get_field(GoalTargetValueField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @target_value.setter
    def target_value(self, value: int):
        field = self.get_field(GoalTargetValueField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def recurrence(self) -> Optional[GoalRecurrence]:
        field = self.get_field(GoalRecurrenceField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @recurrence.setter
    def recurrence(self, value: GoalRecurrence):
        field = self.get_field(GoalRecurrenceField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def recurrence_value(self) -> Optional[int]:
        field = self.get_field(GoalRecurrenceValueField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @recurrence_value.setter
    def recurrence_value(self, value: int):
        field = self.get_field(GoalRecurrenceValueField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def enabled(self) -> Optional[bool]:
        field = self.get_field(GoalEnabledField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @enabled.setter
    def enabled(self, value: bool):
        field = self.get_field(GoalEnabledField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def source(self) -> Optional[GoalSource]:
        field = self.get_field(GoalSourceField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @source.setter
    def source(self, value: GoalSource):
        field = self.get_field(GoalSourceField.ID)

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
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        ]
        )


class GoalSportField(Field):
    ID = 0

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='sport',
            field_id=self.ID,
            base_type=BaseType.ENUM,
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        ]
        )


class GoalSubSportField(Field):
    ID = 1

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='sub_sport',
            field_id=self.ID,
            base_type=BaseType.ENUM,
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        ]
        )


class GoalStartDateField(Field):
    ID = 2

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='start_date',
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


class GoalEndDateField(Field):
    ID = 3

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='end_date',
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


class GoalTypeField(Field):
    ID = 4

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


class GoalValueField(Field):
    ID = 5

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='value',
            field_id=self.ID,
            base_type=BaseType.UINT32,
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        ]
        )


class GoalRepeatField(Field):
    ID = 6

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='repeat',
            field_id=self.ID,
            base_type=BaseType.UINT8,
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        ]
        )


class GoalTargetValueField(Field):
    ID = 7

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='target_value',
            field_id=self.ID,
            base_type=BaseType.UINT32,
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        ]
        )


class GoalRecurrenceField(Field):
    ID = 8

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='recurrence',
            field_id=self.ID,
            base_type=BaseType.ENUM,
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        ]
        )


class GoalRecurrenceValueField(Field):
    ID = 9

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='recurrence_value',
            field_id=self.ID,
            base_type=BaseType.UINT16,
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        ]
        )


class GoalEnabledField(Field):
    ID = 10

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='enabled',
            field_id=self.ID,
            base_type=BaseType.UINT8,
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        ]
        )


class GoalSourceField(Field):
    ID = 11

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='source',
            field_id=self.ID,
            base_type=BaseType.ENUM,
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        ]
        )