import requests
from helius_sdk.core import HeliusAPI


class SalesAPI(HeliusAPI):
    def get_data(self, query, to_df=True):
        url = f"{self.BASE_URL}/nft-events?api-key={self.api_key}"
        response = requests.post(url, json={"query": query})
        if to_df:
            return self.to_df(response.json())
        return response.json()
