from src.features import load_snapshot_data, add_trading_signals
from src.backtester import run_backtest


def main():
    initial_capital = 10000

    data = load_snapshot_data()
    data = add_trading_signals(data, threshold=0.2)

    trades = run_backtest(
        data,
        take_profit=0.0005,
        stop_loss=0.0002,
        initial_capital=initial_capital
    )

    print("\nTrades:")
    print(trades)

    print("\nNumber of trades:")
    print(len(trades))

    if len(trades) > 0:
        final_capital = trades["capital"].iloc[-1]
        profit = final_capital - initial_capital
        profit_pct = profit / initial_capital

        print(f"\nInitial capital: ${initial_capital:,.2f}")
        print(f"Final capital: ${final_capital:,.2f}")
        print(f"Profit: ${profit:,.2f}")
        print(f"Return: {profit_pct:.2%}")
    else:
        print("\nNo closed trades yet.")
        print("Collect more order book snapshots or lower TP/SL thresholds for testing.")


if __name__ == "__main__":
    main()