import pytest
from pymysql import connect

conn = connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="test")


@pytest.mark.skip(reason="out-of-date api")
def test_connect():
    pass


@pytest.mark.skipif(conn.__version__ < "0.2.0", reason="not supported until v0.2.0")
def test_api():
    pass
