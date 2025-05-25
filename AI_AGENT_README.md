# AI Agent Documentation

This project was created using Codex, an AI coding agent. The initial user
prompt requested a Python application that periodically retrieves temperature
information from Open-Meteo and publishes it via MQTT. The agent searched for
any `AGENTS.md` instructions but none were found.

The following steps were performed:

1. Created `src/main.py` implementing the periodic temperature retrieval and
   MQTT publishing.
2. Added `requirements.txt` listing dependencies (`requests` and `paho-mqtt`).
3. Added a `Dockerfile` to run the application in a container.
4. Updated `README.md` with build and run instructions, including how to pass
   configuration via environment variables and how to run automatically on
   reboot using Docker's restart policy or a systemd unit.
5. Documented these steps in this file for future reference.

The prompts used were primarily the original user request in German to create
this repository and provide all necessary documentation for running the tool.
