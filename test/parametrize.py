import pytest


@pytest.mark.parametrize("passwd", ["123456", "abcdefdfs", "as52345fasdf4"])
def test_passwd_length(passwd):
    assert len(passwd) >= 8


@pytest.fixture(params=[("redis", "6379"), ("elasticsearch", "9200")])
def param(request):
    return request.param


@pytest.fixture(autouse=True)
def db(param):
    print("\nSucceed to connect %s:%s" % param)

    yield

    print("\nSucceed to close %s:%s" % param)


def test_api():
    assert 1 == 1
