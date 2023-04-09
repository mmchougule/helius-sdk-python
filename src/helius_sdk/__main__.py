"""
Entrypoint module, in case you use `python -mhelius_sdk`.
"""
import pandas as pd
from helius_sdk.core import CONFIG
from helius_sdk.event import Sale, Mint, Listing

COL_ADDRESS = "4mKSoDDqApmF1DqXvVTSL6tu2zixrSSNjqMxUnwvVzy2"
WALLET_ADDRESS = "GYpFo2YSBQMZefhR9bTTTx7YAugvgKyodX7tUG1pDCux"


def main():
    sale = Sale(CONFIG["api_key"], col_address="")
    s = sale.get()

    listing = Listing(CONFIG["api_key"], col_address=COL_ADDRESS)
    l = listing.get()
    print(l.shape)

    pd.set_option("display.max_colwidth", 100)

    mint = Mint(api_key=CONFIG["api_key"], wallet_address=WALLET_ADDRESS)
    m = mint.get()
    print(m.shape)


if __name__ == "__main__":
    main()
