import requests
import pandas as pd


BINANCE_DEPTH_URL = "https://api.binance.com/api/v3/depth"


def fetch_orderbook(
    symbol: str = "BTCUSDT",
    limit: int = 100,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Fetch the current order book snapshot from Binance.

    Args:
        symbol: Trading pair symbol, for example "BTCUSDT".
        limit: Number of order book levels to download.

    Returns:
        Tuple containing bids and asks as DataFrames with price and quantity columns.
    """
    params = {
        "symbol": symbol,
        "limit": limit,
    }

    response = requests.get(BINANCE_DEPTH_URL, params=params, timeout=10)
    response.raise_for_status()

    orderbook = response.json()

    bids = pd.DataFrame(orderbook["bids"], columns=["price", "quantity"]).astype(float)
    asks = pd.DataFrame(orderbook["asks"], columns=["price", "quantity"]).astype(float)

    return bids, asks


def summarize_orderbook(bids: pd.DataFrame, asks: pd.DataFrame) -> dict[str, float]:
    """Create a one-row numerical summary of an order book snapshot.

    Args:
        bids: DataFrame with bid price levels and quantities.
        asks: DataFrame with ask price levels and quantities.

    Returns:
        Dictionary containing best bid, best ask, spread, volumes and imbalance.
    """
    best_bid = bids["price"].max()
    best_ask = asks["price"].min()

    bid_volume = bids["quantity"].sum()
    ask_volume = asks["quantity"].sum()

    mid_price = (best_bid + best_ask) / 2
    spread = best_ask - best_bid

    total_volume = bid_volume + ask_volume
    imbalance = 0.0 if total_volume == 0 else (bid_volume - ask_volume) / total_volume

    return {
        "best_bid": best_bid,
        "best_ask": best_ask,
        "mid_price": mid_price,
        "spread": spread,
        "bid_volume": bid_volume,
        "ask_volume": ask_volume,
        "imbalance": imbalance,
    }