from mqtt_client import start_mqtt_client

if __name__ == "__main__":
    try:
        start_mqtt_client()
    except KeyboardInterrupt:
        print("Program terminated by user.")
