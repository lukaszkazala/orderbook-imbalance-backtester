import os
import time
from datetime import datetime

import pandas as pd

from src.orderbook_loader import fetch_orderbook, summarize_orderbook


def collect_orderbook_data(
    symbol: str = "BTCUSDT",
    interval_seconds: int = 5,
    iterations: int | None = None,
    output_path: str = "data/orderbook_snapshots.csv",
) -> pd.DataFrame:
    """Collect Binance order book snapshots and save them to a CSV file.

    Args:
        symbol: Trading pair symbol, for example "BTCUSDT".
        interval_seconds: Delay between consecutive API requests.
        iterations: Number of snapshots to collect. If None, runs until stopped.
        output_path: Path where collected snapshots should be saved.

    Returns:
        DataFrame with collected order book summary records.
    """
    records = []
    iteration = 0

    try:
        while iterations is None or iteration < iterations:
            bids, asks = fetch_orderbook(symbol=symbol, limit=100)

            summary = summarize_orderbook(bids, asks)
            summary["timestamp"] = datetime.utcnow()

            records.append(summary)
            iteration += 1

            print(
                f"[{iteration}] "
                f"imbalance={summary['imbalance']:.4f} "
                f"mid_price={summary['mid_price']:.2f}"
            )

            time.sleep(interval_seconds)

    except KeyboardInterrupt:
        print("\nCollector stopped manually.")

    df = pd.DataFrame(records)

    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    file_exists = os.path.exists(output_path)
    df.to_csv(output_path, mode="a" if file_exists else "w", header=not file_exists, index=False)

    print(f"\nSaved {len(df)} rows to {output_path}")

    return df