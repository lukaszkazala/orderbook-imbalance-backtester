def calculate_metrics(trades, initial_capital=10000):
    if trades.empty:
        return {
            "initial_capital": initial_capital,
            "final_capital": initial_capital,
            "total_return": 0,
            "number_of_trades": 0,
            "win_rate": 0,
            "average_trade_return": 0,
            "best_trade": 0,
            "worst_trade": 0,
        }

    final_capital = trades["capital"].iloc[-1]
    total_return = (final_capital - initial_capital) / initial_capital

    number_of_trades = len(trades)

    winning_trades = trades[trades["net_return_pct"] > 0]
    win_rate = len(winning_trades) / number_of_trades

    average_trade_return = trades["net_return_pct"].mean()
    best_trade = trades["net_return_pct"].max()
    worst_trade = trades["net_return_pct"].min()

    return {
        "initial_capital": initial_capital,
        "final_capital": final_capital,
        "total_return": total_return,
        "number_of_trades": number_of_trades,
        "win_rate": win_rate,
        "average_trade_return": average_trade_return,
        "best_trade": best_trade,
        "worst_trade": worst_trade,
    }


def print_metrics(metrics):
    print("\nPerformance metrics:")
    print(f"Initial capital: ${metrics['initial_capital']:,.2f}")
    print(f"Final capital: ${metrics['final_capital']:,.2f}")
    print(f"Total return: {metrics['total_return']:.2%}")
    print(f"Number of trades: {metrics['number_of_trades']}")
    print(f"Win rate: {metrics['win_rate']:.2%}")
    print(f"Average trade return: {metrics['average_trade_return']:.4%}")
    print(f"Best trade: {metrics['best_trade']:.4%}")
    print(f"Worst trade: {metrics['worst_trade']:.4%}")