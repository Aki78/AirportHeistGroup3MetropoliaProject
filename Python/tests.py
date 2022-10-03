import pytest
import helper


def test_feet_to_meters():
    assert 3048 == int(round(10000*helper.feet_to_meters(1)))

def test_meters_to_km():
    assert 1000 == int(helper.meters_to_km(1))

def test_get_distances():
    assert  10000 < helper.get_distances((3.4, -75),(60.3, 24.9))
    assert  11000 > helper.get_distances((3.4, -75),(60.3, 24.9))

def test_get_possible_flights():
    helper.get_possible_flights(99, [(0,0),(100,0),(0,100),(1000,1000),(10000,10000),(0.1,0.1)])

def test_deg_to_xy():
    assert 111  == round(helper.deg_to_xy((0,1))[1])
    assert round(0.63*111)  == round(helper.deg_to_xy((1,0))[0])

def test_get_min_max_distance():
    print("testing started: ", helper.get_min_max_distance([(1,1), (2,2), (3,3), (4,4)]))
    assert True





