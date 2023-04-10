"""
Entrypoint module, in case you use `python -mhelius_sdk`.
"""
import pandas as pd
from helius_sdk.core import CONFIG
from helius_sdk.event import Sale, Mint, Listing
from helius_sdk.nft import Nft
from helius_sdk.transaction import Transaction

COL_ADDRESS = "4mKSoDDqApmF1DqXvVTSL6tu2zixrSSNjqMxUnwvVzy2"
WALLET_ADDRESS = "GYpFo2YSBQMZefhR9bTTTx7YAugvgKyodX7tUG1pDCux"
TX_ADDRESS = "4Mv6CFqtYTdCf1ShunYStgrvFBEZFJSfwjTRc4asmXYdZsJgQ15RgUSU6xZQACtYTyDWSrNH9eEuCF5Ypf9zek89"

def main():
    sale = Sale(CONFIG["api_key"], col_address="")
    s = sale.get()

    listing = Listing(CONFIG["api_key"], col_address=COL_ADDRESS)
    l = listing.get()
    print(s.columns)
    pd.set_option("display.max_colwidth", 100)
    print(s.head().to_pandas().iloc[0])
    print(s.head())

    pd.set_option("display.max_colwidth", 100)

    mint = Mint(api_key=CONFIG["api_key"], wallet_address=WALLET_ADDRESS)
    m = mint.get()
    print(m.shape)

    n = Nft(api_key=CONFIG["api_key"], col_address="KG6f4Fa6YxAW8cG2Dhb18DiMn3rQ3rSLa1Eo2FYM4gi").get()
    print(n.shape)

    t = Transaction(api_key=CONFIG["api_key"],
                    tx_address=TX_ADDRESS).get()
    print(t)


if __name__ == "__main__":
    main()
