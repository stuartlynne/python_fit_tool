import datetime
import math

import gpxpy
from geopy.distance import geodesic

from fit_tool.fit_file_builder import FitFileBuilder
from fit_tool.profile.messages.event_message import EventMessage
from fit_tool.profile.messages.file_id_message import FileIdMessage
from fit_tool.profile.messages.lap_message import LapMessage
from fit_tool.profile.messages.record_message import RecordMessage
from fit_tool.profile.profile_type import FileType, Manufacturer, Event, EventType


def main():
    # Set auto_define to true, so that the builder creates the required Definition Messages for us.
    builder = FitFileBuilder(auto_define=True, min_string_size=50)

    # Read position data from a GPX file
    gpx_file = open('../tests/data/old_stage_left_hand_lee.gpx', 'r')
    gpx = gpxpy.parse(gpx_file)

    message = FileIdMessage()
    message.type = FileType.ACTIVITY
    message.manufacturer = Manufacturer.DEVELOPMENT.value
    message.product = 0
    message.timeCreated = round(datetime.datetime.now().timestamp() * 1000)
    message.serialNumber = 0x12345678
    builder.add(message)

    # Timer Events are a best practice for FIT activity files
    start_timestamp = round(datetime.datetime.now().timestamp() * 1000)
    message = EventMessage()
    message.event = Event.TIMER
    message.event_type = EventType.START
    message.timestamp = start_timestamp
    builder.add(message)

    distance = 0.0
    timestamp = start_timestamp

    records = []

    prev_coordinate = None

    for index, track_point in enumerate(gpx.tracks[0].segments[0].points):
        current_coordinate = (track_point.latitude, track_point.longitude)

        # calculate distance from previous coordinate and accumulate distance
        if prev_coordinate:
            delta = geodesic(prev_coordinate, current_coordinate).meters
        else:
            delta = 0.0
        distance += delta

        message = RecordMessage()
        message.position_lat = track_point.latitude
        message.position_long = track_point.longitude
        message.distance = distance
        message.timestamp = timestamp
        message.power = round(20 * math.sin(2 * math.pi * index / 50) + 200)
        records.append(message)

        timestamp += 10000
        prev_coordinate = current_coordinate

    builder.add_all(records)

    # Every FIT course file MUST contain a Lap message
    elapsed_time = timestamp - start_timestamp
    message = LapMessage()
    message.timestamp = timestamp
    message.start_time = start_timestamp
    message.total_elapsed_time = elapsed_time/1000  # seconds
    message.total_timer_time = elapsed_time/1000    # seconds
    builder.add(message)

    # Finally build the FIT file object and write it to a file
    fit_file = builder.build()

    out_path = '../tests/out/old_stage_activity.fit'
    fit_file.to_file(out_path)
    csv_path = '../tests/out/old_stage_activity.csv'
    fit_file.to_csv(csv_path)


if __name__ == "__main__":
    main()
