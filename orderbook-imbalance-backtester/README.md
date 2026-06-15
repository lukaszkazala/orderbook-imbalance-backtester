# Order Book Imbalance Backtester

A quantitative trading research project based on Binance order book data.

## Project Overview

This project investigates whether order book imbalance can be used to generate profitable trading signals in the cryptocurrency market.

The strategy uses real-time Binance order book snapshots to calculate market imbalance and generate LONG and SHORT signals. Historical simulations are performed using a custom backtesting engine with transaction costs included.

## Features

* Real-time Binance Order Book Data Collection
* Order Book Imbalance Calculation
* LONG / SHORT Signal Generation
* Historical Backtesting Engine
* Take Profit / Stop Loss Management
* Transaction Fee Simulation
* Performance Metrics
* Equity Curve Visualization
* Parameter Optimization

## Project Structure

```text
orderbook-imbalance-backtester/
│
├── data/
│   └── orderbook_snapshots.csv
│
├── src/
│   ├── orderbook_loader.py
│   ├── collector.py
│   ├── features.py
│   ├── backtester.py
│   ├── metrics.py
│   ├── optimizer.py
│   └── visualization.py
│
├── main.py
└── README.md
```

## Strategy Logic

### Order Book Imbalance

The imbalance metric is calculated as:

Imbalance = (Bid Volume - Ask Volume) / (Bid Volume + Ask Volume)

Where:

* Positive values indicate stronger buying pressure
* Negative values indicate stronger selling pressure

### Trading Signals

LONG:

```python
imbalance > threshold
```

SHORT:

```python
imbalance < -threshold
```

NO POSITION:

```python
-threshold <= imbalance <= threshold
```

## Backtesting Rules

Initial Capital:

```text
$10,000
```

Position Management:

* Take Profit
* Stop Loss
* Transaction Fees

The backtester supports both LONG and SHORT positions.

## Dataset

Collected from Binance Spot Market:

```text
BTCUSDT
```

Current dataset:

```text
4161+ order book snapshots
```

Sampling frequency:

```text
Every 5 seconds
```

## Example Results

Best parameter configuration tested:

```text
Threshold: 0.20
Take Profit: 0.20%
Stop Loss: 0.10%
```

Results including transaction costs:

```text
Final Capital: $9,993.99
Total Return: -0.06%
Trades: 28
Win Rate: 46.43%
```

## Key Findings

The strategy generated positive results before transaction costs were included.

After introducing realistic trading fees, profitability decreased significantly.

This highlights the importance of considering execution costs during quantitative strategy development.

## Future Improvements

* Rolling Order Book Imbalance
* Multi-Level Order Book Features
* Spread Filters
* Market Regime Detection
* Walk-Forward Validation
* Binance Testnet Integration
* Live Paper Trading

## Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Binance REST API

## Author

Łukasz Kazała

Applied Mathematics – Data Analytics

Quantitative Trading & Data Science Projects
