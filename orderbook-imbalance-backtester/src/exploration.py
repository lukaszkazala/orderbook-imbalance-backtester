import pandas as pd

order_book = pd.read_csv("data/orderbook_snapshots.csv")

print(order_book.head())
print(order_book.shape)

print(order_book["imbalance"].describe())

metrics = calculate_metrics(trades, initial_capital=initial_capital)
print_metrics(metrics)

