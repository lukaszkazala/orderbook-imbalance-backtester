import requests
import pandas as pd


BINANCE_DEPTH_URL = "https://api.binance.com/api/v3/depth"


def fetch_orderbook(symbol: str = "BTCUSDT", limit: int = 100):
    """
    Fetch current order book snapshot from Binance.

    Parameters:
    symbol : str
        Trading pair, for example BTCUSDT.
    limit : int
        Number of order book levels to download.

    Returns:
    bids : pandas.DataFrame
        Buy orders: price and quantity.
    asks : pandas.DataFrame
        Sell orders: price and quantity.
    """

    params = {
        "symbol": symbol,
        "limit": limit
    }

    response = requests.get(BINANCE_DEPTH_URL, params=params, timeout=10)
    response.raise_for_status()

    orderbook = response.json()

    bids = pd.DataFrame(orderbook["bids"], columns=["price", "quantity"])
    asks = pd.DataFrame(orderbook["asks"], columns=["price", "quantity"])

    bids["price"] = bids["price"].astype(float)
    bids["quantity"] = bids["quantity"].astype(float)

    asks["price"] = asks["price"].astype(float)
    asks["quantity"] = asks["quantity"].astype(float)

    return bids, asks


def summarize_orderbook(bids: pd.DataFrame, asks: pd.DataFrame):
    """
    Create a simple one-row summary of the order book.
    """

    best_bid = bids["price"].max()
    best_ask = asks["price"].min()

    bid_volume = bids["quantity"].sum()
    ask_volume = asks["quantity"].sum()

    mid_price = (best_bid + best_ask) / 2
    spread = best_ask - best_bid

    imbalance = (bid_volume - ask_volume) / (bid_volume + ask_volume)

    summary = {
        "best_bid": best_bid,
        "best_ask": best_ask,
        "mid_price": mid_price,
        "spread": spread,
        "bid_volume": bid_volume,
        "ask_volume": ask_volume,
        "imbalance": imbalance
    }

    return summary