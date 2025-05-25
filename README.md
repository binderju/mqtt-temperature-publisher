# mqtt-temperature-publisher

This small Python application periodically retrieves the current temperature for a
configurable location from the [Open-Meteo](https://open-meteo.com/) API and
publishes it to a configurable MQTT topic.

## Building the Docker image

```
docker build -t mqtt-temperature-publisher .
```

## Running

The application is configured using environment variables:

- `LATITUDE` – latitude of the location
- `LONGITUDE` – longitude of the location
- `MQTT_SERVER` – hostname or IP of the MQTT broker
- `MQTT_PORT` – port of the MQTT broker (default: `1883`)
- `MQTT_TOPIC` – topic to publish the temperature to (default: `temperature`)
- `MQTT_USERNAME` – MQTT username
- `MQTT_PASSWORD` – MQTT password
- `INTERVAL_SECONDS` – interval between updates in seconds (default: `120`)

Example run command:

```
docker run -d --restart unless-stopped \
  -e LATITUDE=52.52 -e LONGITUDE=13.41 \
  -e MQTT_SERVER=mqtt.example.com \
  -e MQTT_PORT=1883 \
  -e MQTT_TOPIC=home/temperature \
  -e MQTT_USERNAME=user -e MQTT_PASSWORD=secret \
  mqtt-temperature-publisher
```

The `--restart unless-stopped` flag ensures the container is restarted
automatically on system reboot.

## Running on another server automatically at boot

When using Docker, the simplest way is to run the container with the
`--restart unless-stopped` flag as shown above. Docker will then start the
container on boot. If Docker is not available, you can install Docker and use
systemd to manage the container, for example via a systemd unit:

```
[Unit]
Description=MQTT Temperature Publisher
After=docker.service
Requires=docker.service

[Service]
Restart=always
ExecStart=/usr/bin/docker run --rm \
  -e LATITUDE=52.52 -e LONGITUDE=13.41 \
  -e MQTT_SERVER=mqtt.example.com \
  -e MQTT_PORT=1883 \
  -e MQTT_TOPIC=home/temperature \
  -e MQTT_USERNAME=user -e MQTT_PASSWORD=secret \
  --name mqtt-temp mqtt-temperature-publisher
ExecStop=/usr/bin/docker stop mqtt-temp

[Install]
WantedBy=multi-user.target
```

Enable the unit with `systemctl enable your-unit.service` to start it
automatically.
