import math
import psycopg2
import functions


def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


def test_rand():
    arr = functions.generate_random_ints(5)
    assert len(arr) == 5
