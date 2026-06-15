import pandas as pd

from src.features import add_trading_signals
from src.backtester import run_backtest
from src.metrics import calculate_metrics


def optimize_parameters(data, initial_capital=10000):
    results = []

    thresholds = [0.2, 0.3, 0.4, 0.5]
    take_profits = [0.001, 0.002, 0.003]
    stop_losses = [0.0005, 0.001]

    for threshold in thresholds:
        data_with_signals = add_trading_signals(data, threshold=threshold)

        for take_profit in take_profits:
            for stop_loss in stop_losses:
                trades = run_backtest(
                    data_with_signals,
                    take_profit=take_profit,
                    stop_loss=stop_loss,
                    initial_capital=initial_capital,
                    fee=0.0004
                )

                metrics = calculate_metrics(
                    trades,
                    initial_capital=initial_capital
                )

                results.append({
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
                })

    results_df = pd.DataFrame(results)
    results_df = results_df.sort_values(by="final_capital", ascending=False)

    return results_df