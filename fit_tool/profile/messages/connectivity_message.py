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


class ConnectivityMessage(DataMessage):
    ID = 127
    NAME = 'connectivity'

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
        super().__init__(name=ConnectivityMessage.NAME,
                         global_id=ConnectivityMessage.ID,
                         local_id=definition_message.local_id if definition_message else local_id,
                         endian=definition_message.endian if definition_message else endian,
                         definition_message=definition_message,
                         developer_fields=developer_fields,
                         fields=[
                             ConnectivityBluetoothEnabledField(
                                 size=self.__get_field_size(definition_message, ConnectivityBluetoothEnabledField.ID),
                                 growable=definition_message is None),
                             ConnectivityBluetoothLeEnabledField(
                                 size=self.__get_field_size(definition_message, ConnectivityBluetoothLeEnabledField.ID),
                                 growable=definition_message is None),
                             ConnectivityAntEnabledField(
                                 size=self.__get_field_size(definition_message, ConnectivityAntEnabledField.ID),
                                 growable=definition_message is None),
                             ConnectivityNameField(
                                 size=self.__get_field_size(definition_message, ConnectivityNameField.ID),
                                 growable=definition_message is None),
                             ConnectivityLiveTrackingEnabledField(
                                 size=self.__get_field_size(definition_message,
                                                            ConnectivityLiveTrackingEnabledField.ID),
                                 growable=definition_message is None),
                             ConnectivityWeatherConditionsEnabledField(
                                 size=self.__get_field_size(definition_message,
                                                            ConnectivityWeatherConditionsEnabledField.ID),
                                 growable=definition_message is None),
                             ConnectivityWeatherAlertsEnabledField(
                                 size=self.__get_field_size(definition_message,
                                                            ConnectivityWeatherAlertsEnabledField.ID),
                                 growable=definition_message is None),
                             ConnectivityAutoActivityUploadEnabledField(
                                 size=self.__get_field_size(definition_message,
                                                            ConnectivityAutoActivityUploadEnabledField.ID),
                                 growable=definition_message is None),
                             ConnectivityCourseDownloadEnabledField(
                                 size=self.__get_field_size(definition_message,
                                                            ConnectivityCourseDownloadEnabledField.ID),
                                 growable=definition_message is None),
                             ConnectivityWorkoutDownloadEnabledField(
                                 size=self.__get_field_size(definition_message,
                                                            ConnectivityWorkoutDownloadEnabledField.ID),
                                 growable=definition_message is None),
                             ConnectivityGpsEphemerisDownloadEnabledField(
                                 size=self.__get_field_size(definition_message,
                                                            ConnectivityGpsEphemerisDownloadEnabledField.ID),
                                 growable=definition_message is None),
                             ConnectivityIncidentDetectionEnabledField(
                                 size=self.__get_field_size(definition_message,
                                                            ConnectivityIncidentDetectionEnabledField.ID),
                                 growable=definition_message is None),
                             ConnectivityGrouptrackEnabledField(
                                 size=self.__get_field_size(definition_message, ConnectivityGrouptrackEnabledField.ID),
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
    def bluetooth_enabled(self) -> Optional[bool]:
        field = self.get_field(ConnectivityBluetoothEnabledField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @bluetooth_enabled.setter
    def bluetooth_enabled(self, value: bool):
        field = self.get_field(ConnectivityBluetoothEnabledField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def bluetooth_le_enabled(self) -> Optional[bool]:
        field = self.get_field(ConnectivityBluetoothLeEnabledField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @bluetooth_le_enabled.setter
    def bluetooth_le_enabled(self, value: bool):
        field = self.get_field(ConnectivityBluetoothLeEnabledField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def ant_enabled(self) -> Optional[bool]:
        field = self.get_field(ConnectivityAntEnabledField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @ant_enabled.setter
    def ant_enabled(self, value: bool):
        field = self.get_field(ConnectivityAntEnabledField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def connectivity_name(self) -> Optional[str]:
        field = self.get_field(ConnectivityNameField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @connectivity_name.setter
    def connectivity_name(self, value: str):
        field = self.get_field(ConnectivityNameField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def live_tracking_enabled(self) -> Optional[bool]:
        field = self.get_field(ConnectivityLiveTrackingEnabledField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @live_tracking_enabled.setter
    def live_tracking_enabled(self, value: bool):
        field = self.get_field(ConnectivityLiveTrackingEnabledField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def weather_conditions_enabled(self) -> Optional[bool]:
        field = self.get_field(ConnectivityWeatherConditionsEnabledField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @weather_conditions_enabled.setter
    def weather_conditions_enabled(self, value: bool):
        field = self.get_field(ConnectivityWeatherConditionsEnabledField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def weather_alerts_enabled(self) -> Optional[bool]:
        field = self.get_field(ConnectivityWeatherAlertsEnabledField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @weather_alerts_enabled.setter
    def weather_alerts_enabled(self, value: bool):
        field = self.get_field(ConnectivityWeatherAlertsEnabledField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def auto_activity_upload_enabled(self) -> Optional[bool]:
        field = self.get_field(ConnectivityAutoActivityUploadEnabledField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @auto_activity_upload_enabled.setter
    def auto_activity_upload_enabled(self, value: bool):
        field = self.get_field(ConnectivityAutoActivityUploadEnabledField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def course_download_enabled(self) -> Optional[bool]:
        field = self.get_field(ConnectivityCourseDownloadEnabledField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @course_download_enabled.setter
    def course_download_enabled(self, value: bool):
        field = self.get_field(ConnectivityCourseDownloadEnabledField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def workout_download_enabled(self) -> Optional[bool]:
        field = self.get_field(ConnectivityWorkoutDownloadEnabledField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @workout_download_enabled.setter
    def workout_download_enabled(self, value: bool):
        field = self.get_field(ConnectivityWorkoutDownloadEnabledField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def gps_ephemeris_download_enabled(self) -> Optional[bool]:
        field = self.get_field(ConnectivityGpsEphemerisDownloadEnabledField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @gps_ephemeris_download_enabled.setter
    def gps_ephemeris_download_enabled(self, value: bool):
        field = self.get_field(ConnectivityGpsEphemerisDownloadEnabledField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def incident_detection_enabled(self) -> Optional[bool]:
        field = self.get_field(ConnectivityIncidentDetectionEnabledField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @incident_detection_enabled.setter
    def incident_detection_enabled(self, value: bool):
        field = self.get_field(ConnectivityIncidentDetectionEnabledField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def grouptrack_enabled(self) -> Optional[bool]:
        field = self.get_field(ConnectivityGrouptrackEnabledField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @grouptrack_enabled.setter
    def grouptrack_enabled(self, value: bool):
        field = self.get_field(ConnectivityGrouptrackEnabledField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)


class ConnectivityBluetoothEnabledField(Field):
    ID = 0

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='bluetooth_enabled',
            field_id=self.ID,
            base_type=BaseType.UINT8,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class ConnectivityBluetoothLeEnabledField(Field):
    ID = 1

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='bluetooth_le_enabled',
            field_id=self.ID,
            base_type=BaseType.UINT8,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class ConnectivityAntEnabledField(Field):
    ID = 2

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='ant_enabled',
            field_id=self.ID,
            base_type=BaseType.UINT8,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class ConnectivityNameField(Field):
    ID = 3

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='name',
            field_id=self.ID,
            base_type=BaseType.STRING,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class ConnectivityLiveTrackingEnabledField(Field):
    ID = 4

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='live_tracking_enabled',
            field_id=self.ID,
            base_type=BaseType.UINT8,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class ConnectivityWeatherConditionsEnabledField(Field):
    ID = 5

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='weather_conditions_enabled',
            field_id=self.ID,
            base_type=BaseType.UINT8,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class ConnectivityWeatherAlertsEnabledField(Field):
    ID = 6

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='weather_alerts_enabled',
            field_id=self.ID,
            base_type=BaseType.UINT8,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class ConnectivityAutoActivityUploadEnabledField(Field):
    ID = 7

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='auto_activity_upload_enabled',
            field_id=self.ID,
            base_type=BaseType.UINT8,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class ConnectivityCourseDownloadEnabledField(Field):
    ID = 8

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='course_download_enabled',
            field_id=self.ID,
            base_type=BaseType.UINT8,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class ConnectivityWorkoutDownloadEnabledField(Field):
    ID = 9

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='workout_download_enabled',
            field_id=self.ID,
            base_type=BaseType.UINT8,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class ConnectivityGpsEphemerisDownloadEnabledField(Field):
    ID = 10

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='gps_ephemeris_download_enabled',
            field_id=self.ID,
            base_type=BaseType.UINT8,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class ConnectivityIncidentDetectionEnabledField(Field):
    ID = 11

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='incident_detection_enabled',
            field_id=self.ID,
            base_type=BaseType.UINT8,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class ConnectivityGrouptrackEnabledField(Field):
    ID = 12

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='grouptrack_enabled',
            field_id=self.ID,
            base_type=BaseType.UINT8,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )
