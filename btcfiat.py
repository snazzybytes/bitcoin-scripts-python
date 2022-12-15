# btcprice.py
import argparse
import json
import urllib.request

# Create the parser
my_parser = argparse.ArgumentParser(
    description="Get current BTC price in requested currency (default is USD)",
    epilog="Diamond Hands 💎🙌!",
)

# Add the CLI arguments
my_parser.add_argument(
    "-c",
    metavar="--currency",
    nargs="?",
    default="USD",
    type=str,
    help="requested display currency",
)

# Execute the parse_args() method first
args = my_parser.parse_args()
user_currency = args.c


def get_price(currency):
    print("Calling Coinbase API to retrieve price in " + currency)

    webURL = urllib.request.urlopen(
        "https://api.coinbase.com/v2/prices/spot?currency=" + currency
    )
    encoding = webURL.info().get_content_charset('utf-8')
    data = webURL.read()
    coinbaseData = json.loads(data.decode(encoding))
    
    return coinbaseData


resp = get_price(user_currency)
print("Price(" + user_currency + "): " + str(round(float(resp["data"]["amount"]), 4)))
satsPerUsd = round(100000000 / float(resp["data"]["amount"]), 2)  # 100 million sats
print("Sats per " + user_currency + ": " + str(satsPerUsd))
