import os
import sys
import gzip


def extract_data_lazy(source: str, target: str) -> None:
    """Decompresses the source file to the target file if the target doesn't already exist."""
    if not os.path.exists(target):
        with gzip.open(source, "rb") as gzfile, open(target, "wb") as outfile:
            outfile.writelines(gzfile)


if __name__ == "__main__":
    extract_data_lazy(
        source="geosub/data/geonames_all_countries_sorted.tsv.gz",
        target="geosub/data/geonames_all_countries_sorted.tsv",
    )
