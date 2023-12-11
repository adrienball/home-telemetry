import os
from datetime import datetime

import pytz
import requests
from influxdb import InfluxDBClient

DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
DATABASE = "smart_home"


def format_date(datetime_str):
    return pytz.utc.localize(datetime.strptime(datetime_str, DATETIME_FORMAT))


def get_power_measurement(data):
    data_time = format_date(data["state"]["lastupdated"])
    return {
        "measurement": "power",
        "tags": {"sensor": data["name"], "uniqueid": data["uniqueid"]},
        "time": data_time,
        "fields": {"power": data["state"]["power"]},
    }


def get_consumption_measurement(data):
    data_time = format_date(data["state"]["lastupdated"])
    return {
        "measurement": "consumption",
        "tags": {"sensor": data["name"], "uniqueid": data["uniqueid"]},
        "time": data_time,
        "fields": {"consumption": data["state"]["consumption"]},
    }


if __name__ == "__main__":
    api_key = os.environ.get("API_KEY")
    if api_key is None:
        print("You must provide an API key for deCONZ rest plugin")
        exit(1)
    deconz_url = f"http://localhost:8080/api/{api_key}/sensors"
    sensors_data_res = requests.get(deconz_url)
    sensors_data_res.raise_for_status()
    sensors_data = sensors_data_res.json()
    points = []
    for sensor_data in sensors_data.values():
        if sensor_data.get("type") == "ZHAPower":
            if sensor_data["state"]["lastupdated"] != "none":
                points.append(get_power_measurement(sensor_data))
            continue
        if sensor_data.get("type") == "ZHAConsumption":
            if sensor_data["state"]["lastupdated"] != "none":
                points.append(get_consumption_measurement(sensor_data))
            continue

    influxdb_client = InfluxDBClient(database=DATABASE)
    influxdb_client.write_points(points)
