import os
import gzip
from importlib import resources


project = "geosub"

release = "0.1"
version = "0.1.0"

extensions = [
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

html_theme = "sphinx_rtd_theme"

doctest_global_setup = """
import geosub
"""

# Extract data if necessary
data_file_name = "geonames_all_countries_sorted.tsv"
gz_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), "..", "geosub", "data", f"{data_file_name}.gz"
    )
)

with resources.path("geosub.data", data_file_name) as data_path:
    if not os.path.exists(data_path):
        print(f"Decompressing {gz_path} to {data_path}...")
        with gzip.open(gz_path, "rb") as gzfile, open(data_path, "wb") as dest_file:
            dest_file.writelines(gzfile)
        print("Decompression complete.")
