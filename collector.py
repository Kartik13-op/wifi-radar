import subprocess
import re
import platform


def get_wifi_info():

    cmd = "netsh wlan show interfaces"

    output = subprocess.check_output(
        cmd,
        shell=True,
        text=True,
        encoding="utf-8",
        errors="ignore"
    )

    signal = None
    rx_rate = None
    tx_rate = None

    for line in output.splitlines():

        if "Signal" in line:
            signal = int(re.findall(r"\d+", line)[0])

        if "Receive rate" in line:
            rx_rate = int(re.findall(r"\d+", line)[0])

        if "Transmit rate" in line:
            tx_rate = int(re.findall(r"\d+", line)[0])

    return {
        "signal": signal,
        "rx_rate": rx_rate,
        "tx_rate": tx_rate
    }


def ping_router(ip):

    cmd = f"ping -n 1 {ip}"

    output = subprocess.check_output(
        cmd,
        shell=True,
        text=True,
        encoding="utf-8",
        errors="ignore"
    )

    latency = None

    match = re.search(r"time[=<](\d+)", output)

    if match:
        latency = int(match.group(1))

    lost = "Lost = 1" in output

    return latency, lost