import math
import psycopg2


def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


def test_psql():
    conn = psycopg2.connect(
        database="postgres", user='postgres', password='postgres'
    )
    cur = conn.cursor()
    cur.execute('select * from lol;')
    aa = cur.fetchone()
    print(aa)
    assert aa == (14, 'maggie')


if __name__ == '__main__':
    test_psql()
