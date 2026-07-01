import pandas as pd

from src.backtester import run_backtest
from src.features import add_trading_signals
from src.metrics import calculate_metrics


def optimize_parameters(
    data: pd.DataFrame,
    initial_capital: float = 10000,
    fee: float = 0.0004,
    thresholds: list[float] | None = None,
    take_profits: list[float] | None = None,
    stop_losses: list[float] | None = None,
) -> pd.DataFrame:
    """Run a grid search over strategy parameters.

    Args:
        data: DataFrame containing order book features.
        initial_capital: Starting capital for each backtest.
        fee: One-way trading fee used in the backtest.
        thresholds: Imbalance thresholds used to generate trading signals.
        take_profits: Take-profit levels to test.
        stop_losses: Stop-loss levels to test.

    Returns:
        DataFrame with tested parameter combinations sorted by final capital.
    """
    if thresholds is None:
        thresholds = [0.2, 0.3, 0.4, 0.5]

    if take_profits is None:
        take_profits = [0.001, 0.002, 0.003]

    if stop_losses is None:
        stop_losses = [0.0005, 0.001]

    results = []

    for threshold in thresholds:
        data_with_signals = add_trading_signals(data, threshold=threshold)

        for take_profit in take_profits:
            for stop_loss in stop_losses:
                trades = run_backtest(
                    data_with_signals,
                    take_profit=take_profit,
                    stop_loss=stop_loss,
                    initial_capital=initial_capital,
                    fee=fee,
                )

                metrics = calculate_metrics(
                    trades,
                    initial_capital=initial_capital,
                )

                results.append(
                    {
                        "threshold": threshold,
                        "take_profit": take_profit,
                        "stop_loss": stop_loss,
                        "final_capital": metrics["final_capital"],
                        "total_return": metrics["total_return"],
                        "number_of_trades": metrics["number_of_trades"],
                        "win_rate": metrics["win_rate"],
                        "average_trade_return": metrics["average_trade_return"],
                        "best_trade": metrics["best_trade"],
                        "worst_trade": metrics["worst_trade"],
                    }
                )

    results_df = pd.DataFrame(results)
    results_df = results_df.sort_values(by="final_capital", ascending=False)

    return results_df