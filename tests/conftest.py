import os
import pytest


@pytest.fixture(scope="session", autouse=True)
def data_file_path() -> str:
    data_file = "geosub/data/geonames_all_countries_sorted.tsv"
    if not os.path.exists(data_file):
        raise ValueError(
            f"ERROR: need to ensure {data_file} is extracted by running `tox -e extract_data`",
        )

    return "geosub/data/geonames_all_countries_sorted.tsv"
