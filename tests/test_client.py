from bentso import CachingDataClient
from bentso.db import get_database
import os
import pandas as pd
import pytest

FIXTURES = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "fixtures",
)


def test_request_parameters(monkeypatch, tmp_path):
    class FakeClient:
        def __init__(self, api_key):
            pass

        def query_crossborder_flows(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    monkeypatch.setattr(
        'bentso.client.EntsoePandasClient',
        FakeClient
    )
    monkeypatch.setattr(
        'bentso.client.CachingDataClient._store_df',
        lambda x, y, z: ("foo", "bar")
    )
    cl = CachingDataClient(str(tmp_path))
    cl.get_trade("CH", "AT", 2017)
    assert cl.client.args == ("CH", "AT")
    assert cl.client.kwargs["end"] == pd.Timestamp(year=2018, month=1, day=1, hour=0, tz='Europe/Brussels')
    assert cl.client.kwargs["start"] == pd.Timestamp(year=2017, month=1, day=1, hour=0, tz='Europe/Brussels')

def test_fixtures():
    cl = CachingDataClient(FIXTURES)
    df = cl.get_generation("FR", 2017)
    assert df['Biomass'].sum() == 229279.
    df = cl.get_capacity("ES", 2017)
    assert df['Wind Onshore'].sum() == 22813.
    df = cl.get_consumption("DE", 2017)
    assert df.sum() == 207975376.
    df = cl.get_trade("ES", "FR", 2017)
    assert df.sum() == 832100.
