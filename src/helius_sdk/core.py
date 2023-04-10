import os
from abc import ABC, abstractmethod

import requests
import yaml
import polars as pl


def load_config(config_path="conf/base.yml"):
    if os.path.exists(config_path):
        with open(config_path, "r") as config_file:
            config = yaml.safe_load(config_file)
        return config["helius"]
    else:
        return {
            "base_url": os.getenv("BASE_URL") or "https://api.helius.xyz/v1",
            "api_key": os.getenv("API_KEY"),
        }


CONFIG = load_config()


class HeliusAPI(ABC):
    BASE_URL = CONFIG["base_url"]

    def __init__(self, api_key, slug=None):
        self.api_key = api_key or CONFIG["api_key"]
        if os.getenv("API_KEY"):
            self.api_key = os.getenv("API_KEY")

        if not self.api_key:
            raise ValueError("No API key provided")
        self.query = None
        self.url = f"{self.BASE_URL}/{slug}?api-key={self.api_key}" if slug else None

    @abstractmethod
    def get(self, query=None):
        pass

    def make_request(self, query, df=True):
        """
        Make post request to Helius API
        :param query:
        :param df:
        :return:
        """
        try:
            response = requests.post(self.url, json=query)
            if not df:
                return response.json()
            return to_df(response.json())
        except Exception as e:
            print(e)
            raise e


def to_df(data, pandas=False):
    if "result" in data:
        data = data["result"]
    if pandas:
        import pandas as pd
        return pd.DataFrame(data)
    return pl.DataFrame(data)
