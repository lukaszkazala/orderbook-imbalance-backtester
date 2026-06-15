import matplotlib.pyplot as plt


def plot_equity_curve(trades):

    if trades.empty:
        print("No trades to plot.")
        return

    plt.figure(figsize=(12, 6))

    plt.plot(
        trades["exit_time"],
        trades["capital"]
    )

    plt.title("Equity Curve")
    plt.xlabel("Time")
    plt.ylabel("Capital ($)")

    plt.grid(True)

    plt.tight_layout()

    plt.show()


def plot_price(data):

    import matplotlib.pyplot as plt

    plt.figure(figsize=(12, 6))

    plt.plot(
        data["timestamp"],
        data["mid_price"]
    )

    plt.title("BTC Mid Price")
    plt.xlabel("Time")
    plt.ylabel("Price")

    plt.grid(True)

    plt.tight_layout()

    plt.show()