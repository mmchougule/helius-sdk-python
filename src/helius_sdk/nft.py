from abc import ABC
from helius_sdk.core import HeliusAPI


class NftAPI(HeliusAPI, ABC):
    """
    Get events data from Helius API.
    """

    def __init__(self, api_key=None, query=None, col_address=None, sources=None):
        """

        :param api_key:
        :param query:
        :param col_address:
        :param sources:
        """
        super().__init__(api_key=api_key, slug="nfts")
        self.sources = sources
        self.col_address = col_address
        self.query = query

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
        return q


class Nft(NftAPI):
    """
    Get sales data from Helius API.

    example:
    >>> from helius_sdk.nft import Nft
    >>> n = Nft(api_key="api_key", col_address="").get()
    >>> n.shape
    """
    def get(self, query=None, df=True):
        q = query or {"mints": [self.col_address]}
        return self.make_request(q, df)
