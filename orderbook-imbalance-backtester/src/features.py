import pandas as pd


def load_snapshot_data(
    path: str = "data/orderbook_snapshots.csv",
) -> pd.DataFrame:
    """Load collected Binance order book snapshots.

    Args:
        path: Path to the CSV file containing collected snapshots.

    Returns:
        DataFrame with parsed timestamps.
    """
    data = pd.read_csv(path)
    data["timestamp"] = pd.to_datetime(data["timestamp"])

    return data


def add_trading_signals(
    data: pd.DataFrame,
    threshold: float = 0.2,
) -> pd.DataFrame:
    """Generate trading signals based on order book imbalance.

    Long signal (1) is generated when imbalance is greater than the
    specified threshold. Short signal (-1) is generated when imbalance
    is lower than the negative threshold. Otherwise, the signal is 0.

    Args:
        data: DataFrame containing order book features.
        threshold: Absolute imbalance threshold used to generate signals.

    Returns:
        DataFrame with an additional ``signal`` column.
    """
    signals = data.copy()

    signals["signal"] = 0
    signals.loc[signals["imbalance"] > threshold, "signal"] = 1
    signals.loc[signals["imbalance"] < -threshold, "signal"] = -1

    return signals