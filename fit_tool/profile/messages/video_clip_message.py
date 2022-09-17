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


class VideoClipMessage(DataMessage):
    ID = 187
    NAME = 'video_clip'

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
        super().__init__(name=VideoClipMessage.NAME,
                         global_id=VideoClipMessage.ID,
                         local_id=definition_message.local_id if definition_message else local_id,
                         endian=definition_message.endian if definition_message else endian,
                         definition_message=definition_message,
                         developer_fields=developer_fields,
                         fields=[
        VideoClipClipNumberField(
            size=self.__get_field_size(definition_message, VideoClipClipNumberField.ID),
            growable=definition_message is None), 
        VideoClipStartTimestampField(
            size=self.__get_field_size(definition_message, VideoClipStartTimestampField.ID),
            growable=definition_message is None), 
        VideoClipStartTimestampMsField(
            size=self.__get_field_size(definition_message, VideoClipStartTimestampMsField.ID),
            growable=definition_message is None), 
        VideoClipEndTimestampField(
            size=self.__get_field_size(definition_message, VideoClipEndTimestampField.ID),
            growable=definition_message is None), 
        VideoClipEndTimestampMsField(
            size=self.__get_field_size(definition_message, VideoClipEndTimestampMsField.ID),
            growable=definition_message is None), 
        VideoClipClipStartField(
            size=self.__get_field_size(definition_message, VideoClipClipStartField.ID),
            growable=definition_message is None), 
        VideoClipClipEndField(
            size=self.__get_field_size(definition_message, VideoClipClipEndField.ID),
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
    def clip_number(self) -> Optional[int]:
        field = self.get_field(VideoClipClipNumberField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @clip_number.setter
    def clip_number(self, value: int):
        field = self.get_field(VideoClipClipNumberField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    
# timestamp : milliseconds from January 1st, 1970 at 00:00:00 UTC

    @property
    def start_timestamp(self) -> Optional[int]:
        field = self.get_field(VideoClipStartTimestampField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None


    # timestamp : milliseconds from January 1st, 1970 at 00:00:00 UTC

    @start_timestamp.setter
    def start_timestamp(self, value: int):
        field = self.get_field(VideoClipStartTimestampField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def start_timestamp_ms(self) -> Optional[int]:
        field = self.get_field(VideoClipStartTimestampMsField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @start_timestamp_ms.setter
    def start_timestamp_ms(self, value: int):
        field = self.get_field(VideoClipStartTimestampMsField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    
# timestamp : milliseconds from January 1st, 1970 at 00:00:00 UTC

    @property
    def end_timestamp(self) -> Optional[int]:
        field = self.get_field(VideoClipEndTimestampField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None


    # timestamp : milliseconds from January 1st, 1970 at 00:00:00 UTC

    @end_timestamp.setter
    def end_timestamp(self, value: int):
        field = self.get_field(VideoClipEndTimestampField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def end_timestamp_ms(self) -> Optional[int]:
        field = self.get_field(VideoClipEndTimestampMsField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @end_timestamp_ms.setter
    def end_timestamp_ms(self, value: int):
        field = self.get_field(VideoClipEndTimestampMsField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def clip_start(self) -> Optional[int]:
        field = self.get_field(VideoClipClipStartField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @clip_start.setter
    def clip_start(self, value: int):
        field = self.get_field(VideoClipClipStartField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    

    @property
    def clip_end(self) -> Optional[int]:
        field = self.get_field(VideoClipClipEndField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None



    @clip_end.setter
    def clip_end(self, value: int):
        field = self.get_field(VideoClipClipEndField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    





class VideoClipClipNumberField(Field):
    ID = 0

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='clip_number',
            field_id=self.ID,
            base_type=BaseType.UINT16,
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        ]
        )


class VideoClipStartTimestampField(Field):
    ID = 1

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='start_timestamp',
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


class VideoClipStartTimestampMsField(Field):
    ID = 2

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='start_timestamp_ms',
            field_id=self.ID,
            base_type=BaseType.UINT16,
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        ]
        )


class VideoClipEndTimestampField(Field):
    ID = 3

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='end_timestamp',
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


class VideoClipEndTimestampMsField(Field):
    ID = 4

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='end_timestamp_ms',
            field_id=self.ID,
            base_type=BaseType.UINT16,
        offset = 0,
                 scale = 1,
                         size = size,
        growable = growable,
                   sub_fields = [
        ]
        )


class VideoClipClipStartField(Field):
    ID = 6

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='clip_start',
            field_id=self.ID,
            base_type=BaseType.UINT32,
        offset = 0,
                 scale = 1,
                         size = size,
        units = 'ms',
        type_name = '',
        growable = growable,
                   sub_fields = [
        ]
        )


class VideoClipClipEndField(Field):
    ID = 7

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='clip_end',
            field_id=self.ID,
            base_type=BaseType.UINT32,
        offset = 0,
                 scale = 1,
                         size = size,
        units = 'ms',
        type_name = '',
        growable = growable,
                   sub_fields = [
        ]
        )