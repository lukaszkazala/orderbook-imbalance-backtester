from src.collector import collect_orderbook_data


def main():
    collect_orderbook_data(
        symbol="BTCUSDT",
        interval_seconds=5,
        iterations=None
    )


if __name__ == "__main__":
    main()