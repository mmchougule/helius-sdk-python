from abc import ABC, abstractmethod
import yaml
import polars as pl


def load_config(config_path="conf/base.yml"):
    with open(config_path, "r") as config_file:
        config = yaml.safe_load(config_file)
    return config["helius"]


CONFIG = load_config()


class HeliusAPI(ABC):
    BASE_URL = CONFIG["base_url"]

    def __init__(self, api_key):
        self.api_key = api_key or CONFIG["api_key"]
        self.query = None

    @abstractmethod
    def get(self, query=None):
        pass


def to_df(data, pandas=False):
    if pandas:
        import pandas as pd

        return pd.DataFrame(data["result"])
    return pl.DataFrame(data["result"])
