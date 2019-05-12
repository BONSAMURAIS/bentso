from bentso import CachingDataClient
from bentso.db import get_database
import numpy as np
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

def test_clean():
    cl = CachingDataClient(FIXTURES)
    df = cl.get_generation("DE", 2017)
    df_clean = cl.get_generation("DE", 2017, True)
    assert np.allclose(df.sum().sum(), df_clean.sum().sum())

def test_remove_zero_columns():
    cl = CachingDataClient(FIXTURES)
    df = cl.get_generation("DE", 2017)
    previous, missing = df.sum().sum(), df['Fossil Gas'].sum()
    df['Fossil Gas'] *= 0
    df = cl._remove_zero_columns(df)
    assert 'Fossil Gas' not in df
    assert np.allclose(previous - missing, df.sum().sum())

def test_remove_other():
    cl = CachingDataClient(FIXTURES)
    df = cl.get_generation("DE", 2017)
    other, total, gas = df['Other'].sum(), df.sum().sum(), df['Fossil Gas'].sum()
    df = cl._remove_other(df)
    assert 'Other' not in df
    assert np.allclose(df.sum().sum(), total)
    assert np.allclose(df['Fossil Gas'].sum(), gas / ((total - other) / total))

def test_remove_other_renewable():
    cl = CachingDataClient(FIXTURES)
    df = cl.get_generation("DE", 2017)
    our_renewables = ["Solar", "Geothermal", "Goofball"]
    solar, geo, total = df['Solar'].sum(), df['Geothermal'].sum(), df.sum().sum()
    other_r, gas = df['Other renewable'].sum(), df['Fossil Gas'].sum()
    scale = (other_r / (solar + geo)) + 1
    df = cl._remove_other_renewable(df, our_renewables)
    assert np.allclose(df.sum().sum(), total)
    assert 'Other renewable' not in df
    assert gas == df['Fossil Gas'].sum()
    assert np.allclose(df['Solar'].sum(), solar * scale)

def test_remove_other_renewable_error():
    cl = CachingDataClient(FIXTURES)
    df = cl.get_generation("DE", 2017)
    error_prone = {'foo', 'bar'}
    with pytest.raises(ValueError):
        cl._remove_other_renewable(df, error_prone)
