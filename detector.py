import numpy as np


class RadarDetector:

    def __init__(self):

        self.signal_history = []
        self.latency_history = []
        self.speed_history = []

    def update(self, signal, latency, speed):

        self.signal_history.append(signal)
        self.latency_history.append(latency)
        self.speed_history.append(speed)

        if len(self.signal_history) < 60:
            return 0, False

        signal_score = self.zscore(
            signal,
            self.signal_history
        )

        latency_score = self.zscore(
            latency,
            self.latency_history
        )

        speed_score = self.zscore(
            speed,
            self.speed_history
        )

        combined = (
            signal_score * 0.5 +
            latency_score * 0.3 +
            speed_score * 0.2
        )

        detected = combined > 2.5

        return combined, detected

    def zscore(self, value, history):

        mean = np.mean(history)
        std = np.std(history)

        if std == 0:
            return 0

        return abs(value - mean) / std