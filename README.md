# Centralized-IoT-System
Build a Centralized IoT System Objective: Develop a centralized IoT system where a Master Hub communicates with and controls multiple device domains: Home Appliances Robot Mobile Interface Desktop/Web Dashboard The system should demonstrate real-time communication, control, and monitoring across all domains.

# Centralized IoT System using MQTT

## 📌 Project Overview
First, we created a virtual ESP32 using a Python script that sends scripted temperature, humidity, and LED status data every 2 seconds to Node-RED through MQTT using the HiveMQ broker, where the data is processed and displayed on the dashboard, and when a user sends commands like LED ON/OFF or robot movement from the dashboard, those commands are sent via Node-RED → MQTT → ESP32, the device receives and executes them, sends back the updated status, and all communication is tracked through HiveMQ Cloud, enabling continuous bidirectional communication and real-time monitoring.
This project demonstrates a **Centralized IoT System** where multiple domains such as **Home Appliances, Robot Control, Mobile Interface, and Web Dashboard** communicate through a **single Master Hub (MQTT Broker)**.

The system enables **real-time monitoring and bidirectional control**, allowing devices to send data and receive commands seamlessly.

---

## 🎯 Objective

To design and implement a system where:

* Devices publish sensor data
* Users monitor data in real time
* Users send control commands
* Devices respond instantly

---

## 🏗️ System Architecture

Start
  │
  ▼
Python Device (Virtual ESP32)
  │
  │ Publishes Sensor Data (Temperature)
  ▼
MQTT Broker (HiveMQ)
  │
  ▼
Node-RED Dashboard
  │
  │ Display Data (Real-time)
  ▼
User Interaction (Button / Control)
  │
  │ Send Command (LED / Robot)
  ▼
MQTT Broker (HiveMQ)
  │
  ▼
Python Device Receives Command
  │
  ▼
Perform Action (LED ON / Robot Move)
  │
  ▼
End (Loop Continues)

* **Device Layer**: Python script simulating ESP32
* **Communication Layer**: MQTT Broker (HiveMQ Cloud)
* **Application Layer**: Node-RED Dashboard, Web MQTT Client

1.Data Flow
Python Device → MQTT Broker → Dashboard / Web Client

2.Control Flow
Dashboard / Web Client(cloud) → MQTT Broker → Device → Action (LED / Robot)


## ⚙️ Working Principle (Step-by-Step)

### Step 1

The system starts with a **virtual device** implemented using a Python script.

### Step 2

The script generates sensor data such as **temperature** and publishes it to an MQTT topic.

### Step 3

The **MQTT broker (HiveMQ)** acts as the central communication layer.

### Step 4

**Node-RED** subscribes to this data, processes it, and updates the dashboard in real time.

### Step 5

The user interacts with the dashboard to control devices like:

* LED (Home Appliance)
* Robot movement

### Step 6

These commands are sent back through MQTT topics.

### Step 7

The device receives the command and performs the action, completing the **bidirectional communication loop**.

---

## 🔄 MQTT Communication Flow

### Data Flow (Device → Dashboard)

```id="xolr1j"
Device → MQTT Topic (sensor/data) → Node-RED → Dashboard
```

### Control Flow (Dashboard → Device)

```id="xucaea"
Dashboard → MQTT Topic (robot/control or home/led) → Device → Action
```

---

##  MQTT Topics Used

| Topic Name    | Description             |
| ------------- | ----------------------- |
| sensor/data   | Publishes sensor values |
| home/led      | LED ON/OFF control      |
| robot/control | Robot movement commands |
| robot/status  | Robot action feedback   |

---

##  Web MQTT Client (HiveMQ)

In addition to Node-RED and mobile app, a web-based MQTT client is used for testing and monitoring.

* Web Client: HiveMQ WebSocket Client
* URL: https://www.hivemq.com/demos/websocket-client/

### Configuration:

```id="wssconfig"
Host: broker.hivemq.com  
Port: 8884  
Connection Type: Secure WebSocket (WSS)
```

### Usage:

* Subscribe to topics like:

  * balaji/esp32/sensor
  * balaji/esp32/robot
* Publish commands:

  * `FORWARD`
  * `ON` / `OFF`

This allows real-time testing without installing any software.

---

##  Features Implemented

* Real-time sensor monitoring
* Bidirectional MQTT communication
* Dashboard-based control system
* Mobile app integration (MQTT Dash)
* Web-based MQTT client testing
* Robot command simulation (Forward, Backward, Left, Right)
* Feedback system from device

---

##  Technologies Used

* Python (Device Simulation)
* MQTT Protocol
* HiveMQ Cloud Broker
* Node-RED (Dashboard)
* MQTT Dash (Mobile App)
* WebSocket MQTT Client

---

## 🚀 Setup Instructions

### 1. MQTT Broker

```id="1bfn2f"
broker.hivemq.com
port: 1883 (TCP)
port: 8884 (WebSocket Secure)
```

---

### 2. Run Python Device

Install required library:

```id="ryjsfn"
pip install paho-mqtt
```

Run:

```id="t5adtp"
python device.py
```

---

### 3. Setup Node-RED

Start Node-RED:

```id="xi06s4"
node-red
```

* Import `flow.json`
* Configure MQTT broker:

```id="zeac0b"
broker.hivemq.com
```

---

### 4. Access Dashboard


http://localhost:1880/ui

---

### 5. Mobile App Setup

* Install MQTT Dash
* Configure:

  * Broker: `broker.hivemq.com`
* Add topics:

  * `balaji/esp32sensor`
  * `balaji/esp32/control`
  * *'balaji/esp32/robot'

---

### 6. Web Client Setup HiveMQ Cloud

the data will store here
* Open: https://www.hivemq.com/demos/websocket-client/
* Enter:

  * Host: `broker.hivemq.com`
  * Port: `8884`
* Connect and test publish/subscribe

---

## 🎥 Demo

The demo video showcases:

* Live sensor data updates
* LED control from dashboard
* Robot movement commands
* Mobile app interaction
* Web client testing
* Full bidirectional communication

---


## 📌 Conclusion

This project successfully demonstrates a **Centralized IoT System** using MQTT with multiple interfaces including dashboard, mobile, and web client.

It highlights:

* Real-time communication
* Centralized architecture
* Scalable IoT design
* Cross-platform control

---

## 🔮 Future Improvements

* Secure authentication (MQTT TLS with credentials)
* Cloud database integration
* Multiple device scalability
* Remote deployment

---

## 👨‍💻 Author

Balaji
Embedded Software & IoT Developer

