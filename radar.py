import time
import csv
import os

from collector import *
from detector import *
from dashboard import *
from config import *

detector = RadarDetector()

os.makedirs("logs", exist_ok=True)

with open("logs/events.csv", "a", newline="") as f:

    writer = csv.writer(f)

    while True:

        try:

            wifi = get_wifi_info()

            latency, lost = ping_router(
                ROUTER_IP
            )

            signal = wifi["signal"]

            speed = wifi["rx_rate"]

            score, movement = detector.update(
                signal,
                latency if latency else 0,
                speed
            )

            print(
                f"Signal={signal}% "
                f"Latency={latency}ms "
                f"Speed={speed} "
                f"Score={score:.2f}"
            )

            if movement:

                print(
                    "\nMOTION DETECTED\n"
                )

                writer.writerow([
                    time.time(),
                    signal,
                    latency,
                    speed,
                    score
                ])

                f.flush()

            update_graph(signal)

            time.sleep(
                SAMPLE_INTERVAL
            )

        except KeyboardInterrupt:
            break

        except Exception as e:
            print(e)