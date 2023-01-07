from pathlib import Path

import pooch
import pytest

import xyzdata


@pytest.mark.request
@pytest.mark.parametrize("name", xyzdata.data.flatten())
def test_data_exists(name):
    dataset = xyzdata.data.query_name(name)
    path = pooch.retrieve(dataset["url"], known_hash=dataset["hash"])
    assert Path(path).exists()