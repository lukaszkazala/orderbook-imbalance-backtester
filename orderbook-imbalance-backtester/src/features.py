import pandas as pd


def load_snapshot_data(path="data/orderbook_snapshots.csv"):
    data = pd.read_csv(path)
    data["timestamp"] = pd.to_datetime(data["timestamp"])
    return data


def add_trading_signals(data, threshold=0.2):
    data = data.copy()

    data["signal"] = 0
    data.loc[data["imbalance"] > threshold, "signal"] = 1
    data.loc[data["imbalance"] < -threshold, "signal"] = -1

    return data