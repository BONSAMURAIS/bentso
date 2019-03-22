# NOTE: Need to first change the client code to only get one month of data!!
from bentso import CachingDataClient
import os
import itertools


cl = CachingDataClient(os.path.dirname(os.path.realpath(__file__)))

COUNTRIES = ["FR", "DE", "ES"]

for country in COUNTRIES:
    cl.get_generation(country, 2017)
    cl.get_consumption(country, 2017)
    cl.get_capacity(country, 2017)

for a, b in itertools.permutations(COUNTRIES, 2):
    if sorted([a, b]) == ["DE", "ES"]:
        continue
    cl.get_trade(a, b, 2017)
