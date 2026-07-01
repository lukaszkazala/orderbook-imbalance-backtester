from src.backtester import run_backtest
from src.features import add_trading_signals, load_snapshot_data
from src.metrics import calculate_metrics, print_metrics
from src.visualization import plot_equity_curve, plot_price


def main() -> None:
    """Run the complete trading strategy backtest."""

    initial_capital = 10000

    data = load_snapshot_data()

    data = add_trading_signals(
        data,
        threshold=0.2,
    )

    trades = run_backtest(
        data,
        take_profit=0.0005,
        stop_loss=0.0002,
        initial_capital=initial_capital,
        fee=0.0004,
    )

    metrics = calculate_metrics(
        trades,
        initial_capital=initial_capital,
    )

    print_metrics(metrics)

    plot_equity_curve(trades)
    plot_price(data)


if __name__ == "__main__":
    main()