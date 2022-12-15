# Bitcoin Scripts with Python

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

Small collection of Bitcoin related scripts in Python for learning purposes as we go down the rabbit hole 🐇🕳.

😤 Don't Trust, Verify 😤!!!

---

### btcfiat.py

- returns "price" + "sat per fiat" for requested currency (defaults to USD)
- uses Coinbase API as data source

### btchalving.py

- uses Mempool API to calculate **"Bitcoin Halving Date"** by fetching bitcoin block data for given time range (3 days default, configurable via `TimeRange` enum)
- uses `config.ini` properties (defaults provided)
  - change _[BitcoinHalving]_ config section to use your personal mempool api URL

---

## Getting Started <a name = "getting_started"></a>

Clone this repo to run the scripts on your local machine. Play around, explore, debug, modify.

> If you have "Mempool" running on your own ⚡️ node (UmbrelOS/EmbassyOS/etc), change "config.ini" to point to your own URLs instead

### Prerequisites

- Python 3.10+ installed

## Usage <a name = "usage"></a>

### btcfiat.py

#### example

```
# defaults to USD
python btcfiat.py

# with requested currency
python btcfiat.py -c EUR
```

![alt text](../media/btcfiat.png?raw=true)

### btchalving.py

```
python btchalving.py
```

(Optional) You can also choose different TimeRange enum by changing `btchalving.py`:

```
# run the script
estimateHalvingDateTime(TimeRange.THREE_DAYS)
```

![alt text](../media/btchalving.png?raw=true)

#### Sample config.ini

```
[DEFAULT]
blockTipHeightUrl = https://mempool.space/api/blocks/tip/height
blockDataUrl = https://mempool.space/api/v1/mining/blocks/sizes-weights/

[BitcoinHalving]
blockTipHeightUrl = https://YourLocalMempoolURL/api/blocks/tip/height
blockDataUrl = https://YourLocalMempoolURL/api/v1/mining/blocks/sizes-weights/
```
