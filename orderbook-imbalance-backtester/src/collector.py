import os
import time
from datetime import datetime

import pandas as pd

from src.orderbook_loader import fetch_orderbook, summarize_orderbook


def collect_orderbook_data(
    symbol="BTCUSDT",
    interval_seconds=5,
    iterations=None
):
    """
    Collect order book snapshots and save them to CSV.

    If iterations is None, the collector runs until stopped manually.
    """

    records = []
    i = 0

    try:
        while iterations is None or i < iterations:
            bids, asks = fetch_orderbook(symbol=symbol, limit=100)

            summary = summarize_orderbook(bids, asks)
            summary["timestamp"] = datetime.utcnow()

            records.append(summary)
            i += 1

            print(
                f"[{i}] "
                f"imbalance={summary['imbalance']:.4f} "
                f"mid_price={summary['mid_price']:.2f}"
            )

            time.sleep(interval_seconds)

    except KeyboardInterrupt:
        print("\nCollector stopped manually.")

    df = pd.DataFrame(records)

    os.makedirs("data", exist_ok=True)
    output_path = "data/orderbook_snapshots.csv"

    if os.path.exists(output_path):
        df.to_csv(output_path, mode="a", header=False, index=False)
    else:
        df.to_csv(output_path, index=False)

    print(f"\nSaved {len(df)} rows to {output_path}")

    return df