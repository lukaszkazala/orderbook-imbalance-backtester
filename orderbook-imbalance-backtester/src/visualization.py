import matplotlib.pyplot as plt
import pandas as pd


def plot_equity_curve(trades: pd.DataFrame) -> None:
    """Plot the portfolio equity curve.

    Args:
        trades: DataFrame containing executed trades.
    """
    if trades.empty:
        print("No trades to plot.")
        return

    plt.figure(figsize=(12, 6))

    plt.plot(
        trades["exit_time"],
        trades["capital"],
    )

    plt.title("Equity Curve")
    plt.xlabel("Time")
    plt.ylabel("Portfolio Value ($)")
    plt.grid(True)

    plt.tight_layout()
    plt.show()


def plot_price(data: pd.DataFrame) -> None:
    """Plot the BTC mid-price over time.

    Args:
        data: DataFrame containing collected market data.
    """
    plt.figure(figsize=(12, 6))

    plt.plot(
        data["timestamp"],
        data["mid_price"],
    )

    plt.title("BTC Mid Price")
    plt.xlabel("Time")
    plt.ylabel("Price ($)")
    plt.grid(True)

    plt.tight_layout()
    plt.show()