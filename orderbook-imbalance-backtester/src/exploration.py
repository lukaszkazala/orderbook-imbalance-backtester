"""
Exploratory analysis of collected Binance order book snapshots.
"""

import pandas as pd

order_book = pd.read_csv("data/orderbook_snapshots.csv")

print(order_book.head())

print("\nDataset shape:")
print(order_book.shape)

print("\nImbalance statistics:")
print(order_book["imbalance"].describe())
