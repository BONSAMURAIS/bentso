from . import TOKEN, DEFAULT_DATA_DIR, USER_PATH
from .db import get_database, File
from .filesystem import create_dir, sha256
from entsoe import EntsoePandasClient
from peewee import DoesNotExist
import os
import pandas as pd


class CachingDataClient:
    def __init__(self, location=None):
        self.dir = location or USER_PATH or DEFAULT_DATA_DIR
        create_dir(self.dir)
        get_database(self.dir)
        self.data_dir = os.path.join(self.dir, "data")
        create_dir(self.data_dir)
        print("Using data directory {}".format(self.dir))
        self.client = EntsoePandasClient(api_key=TOKEN)

    def get_trade(self, from_country, to_country, year):
        year = int(year)
        country_field = "{}-{}".format(from_country, to_country)
        try:
            obj = File.select().where(File.kind=='trade',
                                      File.country==country_field,
                                      File.year==year).get()
            return self._load_df(obj)
        except DoesNotExist:
            print("Querying ENTSO-E API. Please be patient...")
            start, end = self._get_start_end(year)
            df = self.client.query_crossborder_flows(from_country, to_country,
                                                     start=start, end=end)
            hash, path = self._store_df(
                df,
                "trade-{}-{}.pickle".format(country_field, year)
            )
            File.create(
                filepath=path,
                country=country_field,
                year=year,
                sha256=hash,
                kind='trade',
            )
            return df

    def get_consumption(self, country, year):
        year = int(year)
        try:
            obj = File.select().where(File.kind=='load',
                                      File.country==country,
                                      File.year==year).get()
            return self._load_df(obj)
        except DoesNotExist:
            print("Querying ENTSO-E API. Please be patient...")
            start, end = self._get_start_end(year)
            df = self.client.query_load(country, start=start, end=end)
            hash, path = self._store_df(
                df,
                "load-{}-{}.pickle".format(country, year)
            )
            File.create(
                filepath=path,
                country=country,
                year=year,
                sha256=hash,
                kind='load',
            )
            return df

    def get_generation(self, country, year):
        year = int(year)
        try:
            obj = File.select().where(File.kind=='generation',
                                      File.country==country,
                                      File.year==year).get()
            return self._load_df(obj)
        except DoesNotExist:
            print("Querying ENTSO-E API. Please be patient...")
            start, end = self._get_start_end(year)
            df = self.client.query_generation(country, start=start, end=end)
            hash, path = self._store_df(
                df,
                "generation-{}-{}.pickle".format(country, year)
            )
            File.create(
                filepath=path,
                country=country,
                year=year,
                sha256=hash,
                kind='generation',
            )
            return df

    def get_hydro_charging(self, country, year):
        pass

    def _get_start_end(self, year):
        return (
            pd.Timestamp(year=year, month=1, day=1, hour=0, tz='Europe/Brussels'),
            pd.Timestamp(year=year + 1, month=1, day=1, hour=0, tz='Europe/Brussels'),
        )

    def _store_df(self, df, name):
        path = os.path.join(self.data_dir, name)
        df.to_pickle(path)
        return sha256(path), path

    def _load_df(self, obj):
        return pd.read_pickle(obj.filepath)
