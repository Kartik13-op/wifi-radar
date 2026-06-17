import matplotlib.pyplot as plt

plt.ion()

signals = []

def update_graph(signal):

    signals.append(signal)

    if len(signals) > 100:
        signals.pop(0)

    plt.clf()

    plt.plot(signals)

    plt.title("WiFi Radar")

    plt.xlabel("Samples")
    plt.ylabel("Signal %")

    plt.pause(0.01)