import pandas as pd


def run_backtest(
    data: pd.DataFrame,
    take_profit: float = 0.05,
    stop_loss: float = 0.02,
    initial_capital: float = 10000,
    fee: float = 0.0004,
) -> pd.DataFrame:
    """Run a simple long/short backtest using generated trading signals.

    The strategy opens a long position when signal equals 1 and a short
    position when signal equals -1. Positions are closed when either the
    take-profit or stop-loss threshold is reached. Trading fees are applied
    on both entry and exit.

    Args:
        data: DataFrame containing timestamp, mid_price and signal columns.
        take_profit: Profit threshold required to close a position.
        stop_loss: Loss threshold required to close a position.
        initial_capital: Starting capital used in the simulation.
        fee: One-way trading fee expressed as a decimal.

    Returns:
        DataFrame with executed trades and capital after each closed trade.
    """
    backtest_data = data.copy()
    trades = []

    position = 0
    entry_price = None
    entry_time = None
    capital = initial_capital

    for _, row in backtest_data.iterrows():
        price = row["mid_price"]
        signal = row["signal"]
        timestamp = row["timestamp"]

        if position == 0:
            if signal == 1:
                position = 1
                entry_price = price
                entry_time = timestamp
            elif signal == -1:
                position = -1
                entry_price = price
                entry_time = timestamp

        else:
            if position == 1:
                gross_return_pct = (price - entry_price) / entry_price
            else:
                gross_return_pct = (entry_price - price) / entry_price

            net_return_pct = gross_return_pct - (2 * fee)

            if gross_return_pct >= take_profit:
                exit_reason = "take_profit"
            elif gross_return_pct <= -stop_loss:
                exit_reason = "stop_loss"
            else:
                continue

            capital *= 1 + net_return_pct

            trades.append(
                {
                    "entry_time": entry_time,
                    "exit_time": timestamp,
                    "position": "LONG" if position == 1 else "SHORT",
                    "entry_price": entry_price,
                    "exit_price": price,
                    "gross_return_pct": gross_return_pct,
                    "net_return_pct": net_return_pct,
                    "capital": capital,
                    "exit_reason": exit_reason,
                }
            )

            position = 0
            entry_price = None
            entry_time = None

    return pd.DataFrame(trades)