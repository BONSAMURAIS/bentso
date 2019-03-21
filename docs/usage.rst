Usage
=====

The basic class for data retrieval is ``bentso.client.CachingDataClient``. It will retrieve yearly data from the ENTSO-E API, cache it, and then use the cache when possible. Here is a simple example:

.. code-block:: python

    from bentso import *
    cl = CachingDataClient()
    cl.get_generation("FR", 2016)

``CachingDataClient`` supports the following methods:

* get_trade(from_country, to_country, year)
* get_consumption(country, year)
* get_generation(country, year)
* get_capacity(country, year)

Country codes should always be a two-letter ISO code; year should always be an integer.

Using a custom data directory
-----------------------------

You can pass a directory path to ``CachingDataClient`` to use a custom data directory, e.g. ``CachingDataClient("/Users/me/my/cool/data")``.

