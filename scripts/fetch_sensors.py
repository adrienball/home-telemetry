import os
from datetime import datetime

import pytz
import requests
from influxdb import InfluxDBClient

DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
DATABASE = "smart_home"

MEASUREMENTS = {
    "ZHATemperature": "temperature",
    "ZHAHumidity": "humidity",
    "ZHAPressure": "pressure",
}


def format_date(datetime_str):
    return pytz.utc.localize(datetime.strptime(datetime_str, DATETIME_FORMAT))


def get_sensor_measurement(data):
    data_time = format_date(data["state"]["lastupdated"])
    new_point = {
        "measurement": MEASUREMENTS[data["type"]],
        "tags": {"sensor": data["name"], "uniqueid": data["uniqueid"]},
        "time": data_time,
        "fields": {"value": data["state"][MEASUREMENTS[data["type"]]]},
    }
    if data["config"].get("battery") is not None:
        new_point["fields"]["battery"] = data["config"]["battery"]
    return new_point


if __name__ == "__main__":
    api_key = os.environ.get("API_KEY")
    if api_key is None:
        print("You must provide an API key for deCONZ rest plugin")
        exit(1)
    local_tz = pytz.timezone("Europe/Paris")
    deconz_url = f"http://localhost:8080/api/{api_key}/sensors"
    sensors_data_res = requests.get(deconz_url)
    sensors_data_res.raise_for_status()
    sensors_data = sensors_data_res.json()
    points = []
    for sensor_data in sensors_data.items():
        if sensor_data["type"] not in MEASUREMENTS:
            continue
        points.append(get_sensor_measurement(sensor_data))
    influxdb_client = InfluxDBClient(database=DATABASE)
    influxdb_client.write_points(points)
