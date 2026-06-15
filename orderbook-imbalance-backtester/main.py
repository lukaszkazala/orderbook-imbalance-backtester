# from src.features import load_snapshot_data, add_trading_signals
# from src.backtester import run_backtest
# from src.metrics import calculate_metrics, print_metrics
# from src.visualization import plot_equity_curve
# from src.visualization import (
#     plot_equity_curve,
#     plot_price
# )



# def main():
#     initial_capital = 10000

#     data = load_snapshot_data("data/orderbook_snapshots.csv")

#     print("\nData shape:")
#     print(data.shape)

#     data = add_trading_signals(data, threshold=0.2)

#     print("\nSignal counts:")
#     print(data["signal"].value_counts())

#     trades = run_backtest(
#         data,
#         take_profit=0.0005,
#         stop_loss=0.0002,
#         initial_capital=initial_capital,
#         fee=0.0004
#     )

#     print("\nNumber of trades:")
#     print(len(trades))

#     print("\nTrades:")
#     print(trades)

#     metrics = calculate_metrics(
#         trades,
#         initial_capital=initial_capital
#     )

#     print_metrics(metrics)

#     plot_equity_curve(trades)
    
#     plot_price(data)
#     #plot_equity_curve(trades)


# if __name__ == "__main__":
#     main()





from src.features import load_snapshot_data
from src.optimizer import optimize_parameters


def main():
    data = load_snapshot_data("data/orderbook_snapshots.csv")

    results = optimize_parameters(
        data,
        initial_capital=10000
    )

    print(results.head(10))


if __name__ == "__main__":
    main()