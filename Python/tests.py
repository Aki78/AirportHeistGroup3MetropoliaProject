import pytest
import helper

def test_feet_to_meters():
    assert 3048 == int(round(10000*helper.feet_to_meters(1)))
