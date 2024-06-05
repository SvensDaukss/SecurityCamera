import paho.mqtt.client as mqtt
from capture import capture_image, capture_video

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code: {rc}")  # 0 = Success | 1-5 is bad
    client.subscribe("PiGuardian/takePhoto")
    client.subscribe("PiGuardian/takeVideo")

def on_message(client, userdata, msg):  # Callback function for when a PUBLISH message is received from the broker
    print(f"Received message on topic {msg.topic}: {msg.payload.decode('utf-8')}")

    try:
        if msg.topic == "PiGuardian/takePhoto":
            capture_image()
            print("Image captured successfully!")
        elif msg.topic == "PiGuardian/takeVideo":
            capture_video()
            print("Video captured successfully!")
    except Exception as e:
        print(e)

def start_mqtt_client():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("XXX.XXX.X.XX", 1883, 60)  # Replace localhost with your broker's IP address
    print("Listening Forever...")
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("Interrupted by user, shutting down...")
        client.disconnect()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    start_mqtt_client()
