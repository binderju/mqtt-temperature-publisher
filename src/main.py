import os
import time
import requests
import paho.mqtt.client as mqtt


def get_env(name, default=None, required=False):
    value = os.getenv(name, default)
    if required and value is None:
        raise ValueError(f"Missing required environment variable {name}")
    return value


def fetch_temperature(latitude: str, longitude: str) -> float:
    url = (
        "https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}&current_weather=true"
    )
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    return data["current_weather"]["temperature"]


def main():
    lat = get_env("LATITUDE", required=True)
    lon = get_env("LONGITUDE", required=True)
    mqtt_server = get_env("MQTT_SERVER", required=True)
    mqtt_port = int(get_env("MQTT_PORT", 1883))
    mqtt_topic = get_env("MQTT_TOPIC", "temperature")
    mqtt_username = get_env("MQTT_USERNAME", required=True)
    mqtt_password = get_env("MQTT_PASSWORD", required=True)
    interval = int(get_env("INTERVAL_SECONDS", 120))

    client = mqtt.Client()
    client.username_pw_set(mqtt_username, mqtt_password)
    client.connect(mqtt_server, mqtt_port, 60)

    while True:
        try:
            temperature = fetch_temperature(lat, lon)
            client.publish(mqtt_topic, payload=temperature)
            print(f"Published temperature {temperature} to {mqtt_topic}")
        except Exception as exc:
            print(f"Error during publish: {exc}")
        time.sleep(interval)


if __name__ == "__main__":
    main()
