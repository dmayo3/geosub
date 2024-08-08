geosub v0.1.0a0
===============

`GitHub repository <https://github.com/dmayo3/geosub>`_

Lookup ISO 3166-2 geographic subdivisions from postal and country codes.

It leverages offline data from www.geonames.org to determine the approximate
location and search for the geographic subdivision information from pycountry,
all without the need for network requests or external APIs.

Contents:
---------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   api
   license

Introduction
------------

geosub aims to provide a straightforward and efficient solution for applications requiring geographic
subdivision data.

It is less feature-rich and complete, but easier to use and lighter than API-based services.

Features include:

- **No API Key Required**: No need to manage API keys, pay fees, or use external API services.
- **Offline Functionality**: Performs all operations offline.
- **Bundled Data**: Comes packaged with all necessary geographical data.
- **On-Demand Data Loading**: Loads data as needed to minimize memory usage.
- **Minimal Dependencies**: Keeps additional dependencies to a minimum.

Getting Started
---------------

To get started with geosub, see the Installation section, followed by the
Usage guide to see how to implement geosub in your projects.

Limitations
-----------

Some countries are not supported, and there are no guarantees that every postal code will be found.

Here are some details about supported and unsupported locations:

.. automodule:: geosub
   :members: UNSUPPORTED_LOCATIONS, UNSUPPORTED_COUNTRY_CODES, SUPPORTED_COUNTRY_CODES, SUPPORTED_LOCATIONS


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
