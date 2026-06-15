import pandas as pd


def run_backtest(
    data,
    take_profit=0.05,
    stop_loss=0.02,
    initial_capital=10000,
    fee=0.0004
):
    data = data.copy()

    trades = []

    position = 0
    entry_price = None
    entry_time = None
    capital = initial_capital

    for i in range(len(data)):
        row = data.iloc[i]

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

            capital = capital * (1 + net_return_pct)

            trades.append({
                "entry_time": entry_time,
                "exit_time": timestamp,
                "position": "LONG" if position == 1 else "SHORT",
                "entry_price": entry_price,
                "exit_price": price,
                "gross_return_pct": gross_return_pct,
                "net_return_pct": net_return_pct,
                "capital": capital,
                "exit_reason": exit_reason
            })

            position = 0
            entry_price = None
            entry_time = None

    return pd.DataFrame(trades)