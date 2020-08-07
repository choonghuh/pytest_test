import math
import functions
import pytest


@pytest.mark.general
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


@pytest.mark.rand
def test_rand():
    arr = functions.generate_random_ints(1, 10, 3)
    assert len(arr) == 3
    assert itemsAreUnique(arr)


def itemsAreUnique(arr):
    unique = True
    for aa in arr:
        if arr.count(aa) != 1:
            unique = False
    return unique


@pytest.mark.db
def test_db(db):  # fixture
    test_data = (1, "dave davidson")
    db.execute('insert into people (id, name) values (?,?)', test_data)
    db.execute('select * from people')
    data = db.fetchall()[0]
    assert data == test_data
