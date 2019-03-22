import pytest
import os
import bentso


def test_no_key(monkeypatch):
    monkeypatch.setenv('ENTSOE_API_TOKEN', '')
    with pytest.raises(ValueError):
        import bentso
        bentso.CachingDataClient()

def test_token_file(tmp_path, monkeypatch):
    monkeypatch.setenv('ENTSOE_API_TOKEN', '')
    os.chdir(tmp_path)
    with open("entsoe_api_token.txt", "w") as f:
        f.write("find-me")
    assert bentso.filesystem.load_token() == "find-me"

def test_token_envvar(monkeypatch):
    assert bentso.filesystem.load_token() == "fake"
    monkeypatch.setenv('ENTSOE_API_TOKEN', 'find-me')
    assert bentso.filesystem.load_token() == "find-me"
