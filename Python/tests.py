import pytest
import helper
import game


def test_feet_to_meters():
    assert 3048 == int(round(10000*helper.feet_to_meters(1)))

def test_meters_to_km():
    assert 1000 == int(helper.meters_to_km(1))

def test_get_distances():
    assert  10000 < helper.get_distances((3.4, -75),(60.3, 24.9))
    assert  11000 > helper.get_distances((3.4, -75),(60.3, 24.9))

def test_get_possible_flights():
    result = helper.get_possible_flights(4500, (35.46, 15.06), [(49.62,6.20),(28.45,-13.86),(44.57,26.08),(53.52,-6.27),(39.52,-121.76),(29.10, -95.77)])
    print(result)
    assert result == [0, 1, 2, 3]

def test_deg_to_xy():
    assert 111  == round(helper.deg_to_xy((0,1))[1])
    assert round(0.63*111)  == round(helper.deg_to_xy((1,0))[0])

def test_get_min_max_distance():
    print("testing started: ", helper.get_min_max_distance([(1,1), (2,2), (3,3), (4,4)]))
    assert True

def get_ticket_price(distance):
    helper.get_distances((52.30, 4.76), (37.93, 23.94))
    result = game.get_ticket_price()
    assert result == 3271.5080131806762







