import pytest
import helper

def test_feet_to_meters():
    assert 3048 == int(round(10000*helper.feet_to_meters(1)))
def test_meters_to_km():
    assert 1 == helper.meters_to_km(1000)
def test_get_distances():
    assert  10000 < helper.get_distances((3.4, -75),(60.3, 24.9))
    assert  11000 > helper.get_distances((3.4, -75),(60.3, 24.9))

