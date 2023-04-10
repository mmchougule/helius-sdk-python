from abc import ABC
from helius_sdk.core import HeliusAPI


class TransactionAPI(HeliusAPI, ABC):
    """
    Get events data from Helius API.
    """

    def __init__(self, api_key=None, query=None, tx_address=None):
        """

        :param api_key:
        :param query:
        :param tx_address:
        """
        super().__init__(api_key=api_key, slug="transactions")
        self.query = query
        self.url = self.url.replace("v1", "v0")
        # f"{self.BASE_URL}/v0/transactions?api-key={self.api_key}"
        self.tx_address = tx_address


class Transaction(TransactionAPI):
    """
    Get sales data from Helius API.

    example:
    >>> from helius_sdk.transaction import Transaction
    >>> t = Transaction(api_key="api_key", tx_address="").get()
    >>> t.shape
    """
    def get(self, query=None, df=True):
        q = query or {"transactions": [self.tx_address]}
        return self.make_request(q, df)
