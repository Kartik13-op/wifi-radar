# WiFi Radar

WiFi Radar is a Python-based environmental sensing tool that monitors changes in Wi-Fi signal characteristics between a router and a computer. By continuously analyzing signal strength, link speed, latency, and statistical anomalies, the system can detect movement or disturbances occurring along the wireless path.

This project uses only existing Wi-Fi hardware and does not require cameras, sensors, microphones, or additional external devices.

---

## Features

* Continuous Wi-Fi signal monitoring
* Real-time anomaly detection
* Movement and disturbance indication
* Live signal visualization
* Event logging
* Adaptive baseline generation
* No additional hardware required

---

## How It Works

The application periodically collects Wi-Fi metrics from the operating system and analyzes them for unexpected changes.

Metrics monitored include:

* Signal strength (RSSI / Signal Quality)
* Receive link speed
* Transmit link speed
* Ping latency
* Packet loss (optional)

A rolling baseline is maintained using historical measurements. Current measurements are compared against this baseline using statistical anomaly detection techniques.

When the deviation exceeds a configurable threshold, the event is classified as a potential environmental disturbance.

### Detection Principle

Router

\ Wi-Fi Signal Path

Computer

Any object entering or leaving the signal path may alter:

* Signal strength
* Link rate
* Latency
* Signal stability

These changes are analyzed to identify unusual activity.

---

## Limitations

This project is not a true radar system.

Because it relies on standard Wi-Fi metrics exposed by consumer operating systems, detection accuracy is limited compared to specialized Wi-Fi sensing systems based on CSI (Channel State Information).

Expected capabilities:

* Detect large movements
* Detect people walking through signal paths
* Detect environmental changes
* Detect signal disturbances

Not expected to reliably perform:

* Person identification
* Person counting
* Accurate localization
* Body volume estimation
* Reliable breathing detection
* Through-wall tracking

---

## Requirements

Python 3.10+

Packages:

```bash
pip install numpy pandas matplotlib
```

---

## Project Structure

```text
wifi_radar/
│
├── config.py
├── collector.py
├── detector.py
├── dashboard.py
├── radar.py
│
├── logs/
│   └── events.csv
│
├── data/
│   └── baseline.json
│
└── requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourname/wifi-radar.git
cd wifi-radar
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Open:

```python
config.py
```

Set the router IP address:

```python
ROUTER_IP = "192.168.1.1"
```

If your router uses a different gateway address, update accordingly.

---

## Obtaining Wi-Fi Details

### Windows

Open Command Prompt:

```cmd
netsh wlan show interfaces
```

Example output:

```text
Name                   : Wi-Fi
Signal                 : 87%
Receive rate (Mbps)    : 866
Transmit rate (Mbps)   : 866
```

These values are used by the radar for monitoring.

To find your gateway address:

```cmd
ipconfig
```

Look for:

```text
Default Gateway . . . . . . : 192.168.1.1
```

---

### Linux

Signal information:

```bash
iwconfig
```

or

```bash
nmcli device wifi
```

Gateway information:

```bash
ip route
```

Look for:

```text
default via 192.168.1.1
```

---

## Running

Start the radar:

```bash
python radar.py
```

Example output:

```text
Signal=87%
Latency=2ms
Speed=866
Score=0.73
```

When a significant anomaly is detected:

```text
MOTION DETECTED
```

Events are automatically stored in:

```text
logs/events.csv
```

---

## Understanding the Graph

The graph displays signal quality over time.

Small fluctuations are normal.

Typical causes include:

* Router power adjustments
* Wi-Fi channel interference
* Neighboring networks
* Operating system background scans
* Environmental reflections

A visible wave pattern does not necessarily indicate movement.

---

## Troubleshooting

### Ping Returns Exit Status 1

Error:

```text
Command 'ping -n 1 192.168.1.1' returned non-zero exit status 1
```

Possible causes:

* Incorrect gateway address
* Router does not respond to ICMP
* Network connection unavailable

Verify manually:

```cmd
ping 192.168.1.1
```

Check the correct gateway:

```cmd
ipconfig
```

---

### Constant Wave or "Breathing" Patterns

If the graph appears to show breathing-like oscillations:

* Ensure nobody is moving nearby
* Disable nearby fans if possible
* Stop large downloads
* Stop video streaming
* Leave the area for several minutes

In most cases, periodic patterns are caused by:

* Normal Wi-Fi fluctuations
* Link rate adaptation
* Environmental reflections
* Network interference

Consumer RSSI data is generally not accurate enough for reliable breathing detection.

---

### No Motion Detection

Possible reasons:

* Signal path is unobstructed
* Detection threshold is too high
* Router and computer are too close together
* Environmental changes are too small

Try:

* Increasing distance
* Lowering detection thresholds
* Using a 5 GHz connection

---

### Excessive False Positives

Possible causes:

* Heavy network traffic
* Multiple active devices
* Nearby wireless interference
* Unstable signal environment

Try:

* Using a dedicated test network
* Reducing background traffic
* Increasing anomaly thresholds

---

## Improving Accuracy

For best results:

* Use a stable Wi-Fi connection
* Use 5 GHz where available
* Keep router and computer stationary
* Minimize background traffic
* Collect a longer baseline period

---

## Future Improvements

Potential future additions:

* Machine Learning Classification
* Historical analytics

---

## Disclaimer

This project is an experimental Wi-Fi sensing tool intended for educational and research purposes. Detection results should be considered indicative rather than authoritative. Environmental conditions, hardware differences, and wireless interference can significantly affect performance.
