import pytest
import os


def test_no_key():
    with pytest.raises(ValueError):
        import bentso

def test_token_file(tmp_path):
    os.chdir(tmp_path)
    with open("entsoe_api_token.txt", "w") as f:
        f.write("find-me")
    import bentso
    assert bentso.TOKEN == "find-me"

def test_token_envvar():
    os.environ['ENTSOE_API_TOKEN'] = 'find-me'
    import bentso
    assert bentso.TOKEN == "find-me"
