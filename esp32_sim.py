import paho.mqtt.client as mqtt
import time
import random
import json

broker = "broker.hivemq.com"
port = 1883

# Initialize MQTT client
client = mqtt.Client(client_id="ESP32_VIRTUAL")

# Global variable to keep LED state
led_state = "OFF"

# Callback for messages from Node-RED
def on_message(client, userdata, msg):
    global led_state  # Use the global variable

    command = msg.payload.decode()
    print("Command from dashboard:", command)

    if command == "LED_ON":
        led_state = "ON"
        print("Virtual LED ON")
    elif command == "LED_OFF":
        led_state = "OFF"
        print("Virtual LED OFF")
    elif command == "FORWARD":
        print("Robot moves one step forward")
        client.publish("balaji/esp32/robot", "STEP_FORWARD")
    elif command == "BACKWARD":
        print("Robot moves one step backward")
        client.publish("balaji/esp32/robot", "STEP_BACKWARD")

# Attach callback
client.on_message = on_message

# Connect to broker
client.connect(broker, port)
client.subscribe("balaji/esp32/control")
client.loop_start()

while True:
    # Simulate sensor readings
    data = {
        "temperature": round(random.uniform(25, 35), 2),
        "humidity": round(random.uniform(40, 60), 2),
        "led_state": led_state  # Send current LED state
    }

    # Send sensor data to Node-RED
    client.publish("balaji/esp32/sensor", json.dumps(data))
    print("Sending:", data)

    time.sleep(2)  # wait 2 seconds before next reading