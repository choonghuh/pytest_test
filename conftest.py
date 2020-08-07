import pytest
import os
import sqlite3


@pytest.fixture(scope='function')
def db():
    file = os.path.join(os.getcwd(), "test.db")
    conn = sqlite3.connect(file)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS people (id, name)")
    yield cur
    cur.close()
    conn.close()
