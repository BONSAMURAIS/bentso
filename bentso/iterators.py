from .client import CachingDataClient
import itertools


COUNTRIES = ['AT','BE','BA','BG','HR','CY','CZ','DK','EE','FI','FR',
             'DE','GR','HU','IE','IS','IT','LV','LU','MK','ME','NL',
             'NI','NO','PL','PT','RO','RS','SK','SI','SE','CH']


def iterate_generation(year):
    """Iterate over all countries and technology types, and return annual
    generation sums as ``(technology, country, amount)``.

    All data returned are in ENTSO-E labels and ISO country codes."""
    c = CachingDataClient(key="cache-only", verbose=False)

    for country in COUNTRIES:
        gen = c.get_generation(country, year)
        if gen is not None:
            # Unit conversion from MWh to MJ
            gen = gen.sum() * 3600
            for technology, amount in zip(gen.index, gen):
                yield technology, country, amount


def iterate_trade(year):
    """Iterate over all country combinations, and return annual trade sums as
    ``(from country, to country, amount)``.

    All country labels returned are in ISO country codes."""
    c = CachingDataClient(key="cache-only", verbose=False)

    for from_country, to_country in itertools.combinations(COUNTRIES, 2):
        trd = c.get_trade(from_country, to_country, year)
        if trd is not None:
            # Unit conversion from MWh to MJ
            yield from_country, to_country, trd.sum() * 3600
