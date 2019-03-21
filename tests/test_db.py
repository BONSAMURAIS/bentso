from bentso.db import get_database, File
from pathlib import Path
import pytest


@pytest.fixture
def tdb(tmp_path):
    db = get_database(str(tmp_path))
    return tmp_path, db


def test_directory_setup(tdb):
    dir, db = tdb
    assert list(dir.iterdir()) == [dir / "bentso_cache.db"]
