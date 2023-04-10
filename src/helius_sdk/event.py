from abc import ABC

import requests
from helius_sdk.core import HeliusAPI, to_df, CONFIG

YOOTS_ADDRESS = "4mKSoDDqApmF1DqXvVTSL6tu2zixrSSNjqMxUnwvVzy2"


class EventsAPI(HeliusAPI, ABC):
    """
    Get events data from Helius API.
    """

    def __init__(self, api_key=None, query=None, col_address=None, sources=None):
        """

        :param api_key:
        :param query:
        :param col_address:
        :param sources:

        e.g.:
        query = {
              "query": {
                "accounts": [
                  "79FjnnXFpSajugwpx3FfQbV7hJJTe7QXAusF7R4CMf6c"
                ],
                "types": [
                  "NFT_SALE"
                ],
                "sources": [
                  "MAGIC_EDEN"
                ],
                "startSlot": 162368570,
                "endSlot": 162368580,
                "startTime": 1669055189,
                "endTime": 1669070189,
                "nftCollectionFilters": {
                  "firstVerifiedCreator": [
                    "A4FM6h8T5Fmh9z2g3fKUrKfZn6BNFEgByR8QGpdbQhk1"
                  ],
                  "verifiedCollectionAddress": [
                    "4mKSoDDqApmF1DqXvVTSL6tu2zixrSSNjqMxUnwvVzy2"
                  ]
                }
              },
              "options": {
                "limit": 100,
                "sortOrder": "DESC",
                "paginationToken": "V1_162262948_99"
              }
            }
        """
        # super().__init__(api_key, )
        super().__init__(api_key=api_key, slug="nft-events")
        self.sources = sources
        self.col_address = col_address or YOOTS_ADDRESS
        # self.url = f"{self.BASE_URL}/nft-events?api-key={self.api_key}"
        self.query = query

    # def make_request(self, query, df=True):
    #     """
    #     Make post request to Helius API
    #     :param query:
    #     :param df:
    #     :return:
    #     """
    #     try:
    #         response = requests.post(self.url, json={"query": query})
    #         if not df:
    #             return response.json()
    #         return to_df(response.json())
    #     except Exception as e:
    #         raise e

    def get_query(self, qtype: [str], kwargs={}):
        """
        Build query for Helius API
        :param qtype:
        :param kwargs:
        :return:
        """
        q = {"types": qtype, "nftCollectionFilters": {"verifiedCollectionAddress": [self.col_address]}, **kwargs}
        if self.sources:
            q["sources"] = self.sources or ["MAGIC_EDEN"]
        return {"query": q}


class Sale(EventsAPI):
    """
    Get sales data from Helius API.

    example:
    >>> from helius_sdk.event import Sale
    >>> sale = Sale().get()
    >>> sale.shape
    """
    def get(self, query=None, df=True):
        q = query or self.get_query(["NFT_SALE"])
        return self.make_request(q, df)


class Listing(EventsAPI):
    """
    Get listings data from Helius API.

    example:
    >>> from helius_sdk.event import Listing
    >>> l = Listing().get()
    >>> l.shape

    """
    def get(self, query=None, df=True):
        q = query or self.get_query(["NFT_LISTING"])
        return self.make_request(q, df)


class Mint(EventsAPI):
    """
    Get mints data from Helius API.

    example:
    >>> from helius_sdk.event import Mint
    >>> m = Mint().get()
    >>> m.shape
    """
    def __init__(self, wallet_address=None, col_address=None, api_key=None, query=None, sources=None):
        super().__init__(api_key, query, col_address, sources)
        self.wallet_address = wallet_address

    def get(self, query=None, df=True):
        q = query or self.get_query(["NFT_MINT"], kwargs={"accounts": [self.wallet_address]})
        return self.make_request(q, df)


# Create a higher level API
# def get_sales(query=None):
#     sale = Sale(api_key=CONFIG["api_key"])
#     return sale.get(query)


# def get_mints(self, query=None):
#     sale = Sale(api_key=CONFIG["api_key"])
#     return Mint(self.api_key).get(query)
#
#
# def get_listings(self, query=None):
#     sale = Sale(api_key=CONFIG["api_key"])
#     return Listing(self.api_key).get(query)
