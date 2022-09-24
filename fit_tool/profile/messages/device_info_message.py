# Autogenerated. Do not modify.
#
# Profile: 21.60
from typing import List as list
from typing import Optional

from fit_tool.base_type import BaseType
from fit_tool.data_message import DataMessage
from fit_tool.definition_message import DefinitionMessage
from fit_tool.developer_field import DeveloperField
from fit_tool.endian import Endian
from fit_tool.field import Field
from fit_tool.profile.profile_type import *
from fit_tool.sub_field import SubField


class DeviceInfoMessage(DataMessage):
    ID = 23
    NAME = 'device_info'

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
        super().__init__(name=DeviceInfoMessage.NAME,
                         global_id=DeviceInfoMessage.ID,
                         local_id=definition_message.local_id if definition_message else local_id,
                         endian=definition_message.endian if definition_message else endian,
                         definition_message=definition_message,
                         developer_fields=developer_fields,
                         fields=[
                             TimestampField(
                                 size=self.__get_field_size(definition_message, TimestampField.ID),
                                 growable=definition_message is None),
                             DeviceInfoDeviceIndexField(
                                 size=self.__get_field_size(definition_message, DeviceInfoDeviceIndexField.ID),
                                 growable=definition_message is None),
                             DeviceInfoDeviceTypeField(
                                 size=self.__get_field_size(definition_message, DeviceInfoDeviceTypeField.ID),
                                 growable=definition_message is None),
                             DeviceInfoManufacturerField(
                                 size=self.__get_field_size(definition_message, DeviceInfoManufacturerField.ID),
                                 growable=definition_message is None),
                             DeviceInfoSerialNumberField(
                                 size=self.__get_field_size(definition_message, DeviceInfoSerialNumberField.ID),
                                 growable=definition_message is None),
                             DeviceInfoProductField(
                                 size=self.__get_field_size(definition_message, DeviceInfoProductField.ID),
                                 growable=definition_message is None),
                             DeviceInfoSoftwareVersionField(
                                 size=self.__get_field_size(definition_message, DeviceInfoSoftwareVersionField.ID),
                                 growable=definition_message is None),
                             DeviceInfoHardwareVersionField(
                                 size=self.__get_field_size(definition_message, DeviceInfoHardwareVersionField.ID),
                                 growable=definition_message is None),
                             DeviceInfoCumOperatingTimeField(
                                 size=self.__get_field_size(definition_message, DeviceInfoCumOperatingTimeField.ID),
                                 growable=definition_message is None),
                             DeviceInfoBatteryVoltageField(
                                 size=self.__get_field_size(definition_message, DeviceInfoBatteryVoltageField.ID),
                                 growable=definition_message is None),
                             DeviceInfoBatteryStatusField(
                                 size=self.__get_field_size(definition_message, DeviceInfoBatteryStatusField.ID),
                                 growable=definition_message is None),
                             DeviceInfoSensorPositionField(
                                 size=self.__get_field_size(definition_message, DeviceInfoSensorPositionField.ID),
                                 growable=definition_message is None),
                             DeviceInfoDescriptorField(
                                 size=self.__get_field_size(definition_message, DeviceInfoDescriptorField.ID),
                                 growable=definition_message is None),
                             DeviceInfoAntTransmissionTypeField(
                                 size=self.__get_field_size(definition_message, DeviceInfoAntTransmissionTypeField.ID),
                                 growable=definition_message is None),
                             DeviceInfoAntDeviceNumberField(
                                 size=self.__get_field_size(definition_message, DeviceInfoAntDeviceNumberField.ID),
                                 growable=definition_message is None),
                             DeviceInfoAntNetworkField(
                                 size=self.__get_field_size(definition_message, DeviceInfoAntNetworkField.ID),
                                 growable=definition_message is None),
                             DeviceInfoSourceTypeField(
                                 size=self.__get_field_size(definition_message, DeviceInfoSourceTypeField.ID),
                                 growable=definition_message is None),
                             DeviceInfoProductNameField(
                                 size=self.__get_field_size(definition_message, DeviceInfoProductNameField.ID),
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
    def device_index(self) -> Optional[int]:
        field = self.get_field(DeviceInfoDeviceIndexField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @device_index.setter
    def device_index(self, value: int):
        field = self.get_field(DeviceInfoDeviceIndexField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def device_type(self) -> Optional[int]:
        field = self.get_field(DeviceInfoDeviceTypeField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @device_type.setter
    def device_type(self, value: int):
        field = self.get_field(DeviceInfoDeviceTypeField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def antplus_device_type(self) -> Optional[int]:
        field = self.get_field(DeviceInfoDeviceTypeField.ID)
        type_field = self.get_field(DeviceInfoSourceTypeField.ID)

        is_sub_field_valid = type_field and type_field.get_value() in [1]
        if field and field.is_valid() and is_sub_field_valid:
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @antplus_device_type.setter
    def antplus_device_type(self, value: int):
        field = self.get_field(DeviceInfoDeviceTypeField.ID)
        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def ant_device_type(self) -> Optional[int]:
        field = self.get_field(DeviceInfoDeviceTypeField.ID)
        type_field = self.get_field(DeviceInfoSourceTypeField.ID)

        is_sub_field_valid = type_field and type_field.get_value() in [0]
        if field and field.is_valid() and is_sub_field_valid:
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @ant_device_type.setter
    def ant_device_type(self, value: int):
        field = self.get_field(DeviceInfoDeviceTypeField.ID)
        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def manufacturer(self) -> Optional[int]:
        field = self.get_field(DeviceInfoManufacturerField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @manufacturer.setter
    def manufacturer(self, value: int):
        field = self.get_field(DeviceInfoManufacturerField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def serial_number(self) -> Optional[int]:
        field = self.get_field(DeviceInfoSerialNumberField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @serial_number.setter
    def serial_number(self, value: int):
        field = self.get_field(DeviceInfoSerialNumberField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def product(self) -> Optional[int]:
        field = self.get_field(DeviceInfoProductField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @product.setter
    def product(self, value: int):
        field = self.get_field(DeviceInfoProductField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def favero_product(self) -> Optional[int]:
        field = self.get_field(DeviceInfoProductField.ID)
        type_field = self.get_field(DeviceInfoManufacturerField.ID)

        is_sub_field_valid = type_field and type_field.get_value() in [263]
        if field and field.is_valid() and is_sub_field_valid:
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @favero_product.setter
    def favero_product(self, value: int):
        field = self.get_field(DeviceInfoProductField.ID)
        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def garmin_product(self) -> Optional[int]:
        field = self.get_field(DeviceInfoProductField.ID)
        type_field = self.get_field(DeviceInfoManufacturerField.ID)

        is_sub_field_valid = type_field and type_field.get_value() in [1, 15, 13, 89]
        if field and field.is_valid() and is_sub_field_valid:
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @garmin_product.setter
    def garmin_product(self, value: int):
        field = self.get_field(DeviceInfoProductField.ID)
        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def software_version(self) -> Optional[float]:
        field = self.get_field(DeviceInfoSoftwareVersionField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @software_version.setter
    def software_version(self, value: float):
        field = self.get_field(DeviceInfoSoftwareVersionField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def hardware_version(self) -> Optional[int]:
        field = self.get_field(DeviceInfoHardwareVersionField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @hardware_version.setter
    def hardware_version(self, value: int):
        field = self.get_field(DeviceInfoHardwareVersionField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def cum_operating_time(self) -> Optional[int]:
        field = self.get_field(DeviceInfoCumOperatingTimeField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @cum_operating_time.setter
    def cum_operating_time(self, value: int):
        field = self.get_field(DeviceInfoCumOperatingTimeField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def battery_voltage(self) -> Optional[float]:
        field = self.get_field(DeviceInfoBatteryVoltageField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @battery_voltage.setter
    def battery_voltage(self, value: float):
        field = self.get_field(DeviceInfoBatteryVoltageField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def battery_status(self) -> Optional[int]:
        field = self.get_field(DeviceInfoBatteryStatusField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @battery_status.setter
    def battery_status(self, value: int):
        field = self.get_field(DeviceInfoBatteryStatusField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def sensor_position(self) -> Optional[BodyLocation]:
        field = self.get_field(DeviceInfoSensorPositionField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @sensor_position.setter
    def sensor_position(self, value: BodyLocation):
        field = self.get_field(DeviceInfoSensorPositionField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def descriptor(self) -> Optional[str]:
        field = self.get_field(DeviceInfoDescriptorField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @descriptor.setter
    def descriptor(self, value: str):
        field = self.get_field(DeviceInfoDescriptorField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def ant_transmission_type(self) -> Optional[int]:
        field = self.get_field(DeviceInfoAntTransmissionTypeField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @ant_transmission_type.setter
    def ant_transmission_type(self, value: int):
        field = self.get_field(DeviceInfoAntTransmissionTypeField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def ant_device_number(self) -> Optional[int]:
        field = self.get_field(DeviceInfoAntDeviceNumberField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @ant_device_number.setter
    def ant_device_number(self, value: int):
        field = self.get_field(DeviceInfoAntDeviceNumberField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def ant_network(self) -> Optional[AntNetwork]:
        field = self.get_field(DeviceInfoAntNetworkField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @ant_network.setter
    def ant_network(self, value: AntNetwork):
        field = self.get_field(DeviceInfoAntNetworkField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def source_type(self) -> Optional[SourceType]:
        field = self.get_field(DeviceInfoSourceTypeField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @source_type.setter
    def source_type(self, value: SourceType):
        field = self.get_field(DeviceInfoSourceTypeField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def product_name(self) -> Optional[str]:
        field = self.get_field(DeviceInfoProductNameField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @product_name.setter
    def product_name(self, value: str):
        field = self.get_field(DeviceInfoProductNameField.ID)

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


class DeviceInfoDeviceIndexField(Field):
    ID = 0

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='device_index',
            field_id=self.ID,
            base_type=BaseType.UINT8,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class DeviceInfoDeviceTypeField(Field):
    ID = 1

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='device_type',
            field_id=self.ID,
            base_type=BaseType.UINT8,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
                SubField(
                    name='antplus_device_type',
                    base_type=BaseType.UINT8,
                    scale=1,
                    offset=0,
                    reference_map={
                        DeviceInfoSourceTypeField.ID: [1]
                    }),
                SubField(
                    name='ant_device_type',
                    base_type=BaseType.UINT8,
                    scale=1,
                    offset=0,
                    reference_map={
                        DeviceInfoSourceTypeField.ID: [0]
                    })
            ]
        )


class DeviceInfoManufacturerField(Field):
    ID = 2

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='manufacturer',
            field_id=self.ID,
            base_type=BaseType.UINT16,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class DeviceInfoSerialNumberField(Field):
    ID = 3

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='serial_number',
            field_id=self.ID,
            base_type=BaseType.UINT32Z,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class DeviceInfoProductField(Field):
    ID = 4

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='product',
            field_id=self.ID,
            base_type=BaseType.UINT16,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
                SubField(
                    name='favero_product',
                    base_type=BaseType.UINT16,
                    scale=1,
                    offset=0,
                    reference_map={
                        DeviceInfoManufacturerField.ID: [263]
                    }),
                SubField(
                    name='garmin_product',
                    base_type=BaseType.UINT16,
                    scale=1,
                    offset=0,
                    reference_map={
                        DeviceInfoManufacturerField.ID: [1, 15, 13, 89]
                    })
            ]
        )


class DeviceInfoSoftwareVersionField(Field):
    ID = 5

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='software_version',
            field_id=self.ID,
            base_type=BaseType.UINT16,
            offset=0,
            scale=100,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class DeviceInfoHardwareVersionField(Field):
    ID = 6

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='hardware_version',
            field_id=self.ID,
            base_type=BaseType.UINT8,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class DeviceInfoCumOperatingTimeField(Field):
    ID = 7

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='cum_operating_time',
            field_id=self.ID,
            base_type=BaseType.UINT32,
            offset=0,
            scale=1,
            size=size,
            units='s',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )


class DeviceInfoBatteryVoltageField(Field):
    ID = 10

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='battery_voltage',
            field_id=self.ID,
            base_type=BaseType.UINT16,
            offset=0,
            scale=256,
            size=size,
            units='V',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )


class DeviceInfoBatteryStatusField(Field):
    ID = 11

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='battery_status',
            field_id=self.ID,
            base_type=BaseType.UINT8,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class DeviceInfoSensorPositionField(Field):
    ID = 18

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='sensor_position',
            field_id=self.ID,
            base_type=BaseType.ENUM,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class DeviceInfoDescriptorField(Field):
    ID = 19

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='descriptor',
            field_id=self.ID,
            base_type=BaseType.STRING,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class DeviceInfoAntTransmissionTypeField(Field):
    ID = 20

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='ant_transmission_type',
            field_id=self.ID,
            base_type=BaseType.UINT8Z,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class DeviceInfoAntDeviceNumberField(Field):
    ID = 21

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='ant_device_number',
            field_id=self.ID,
            base_type=BaseType.UINT16Z,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class DeviceInfoAntNetworkField(Field):
    ID = 22

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='ant_network',
            field_id=self.ID,
            base_type=BaseType.ENUM,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class DeviceInfoSourceTypeField(Field):
    ID = 25

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='source_type',
            field_id=self.ID,
            base_type=BaseType.ENUM,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class DeviceInfoProductNameField(Field):
    ID = 27

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='product_name',
            field_id=self.ID,
            base_type=BaseType.STRING,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )
