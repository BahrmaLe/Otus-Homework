"""Fixtures for tests.py"""
import pytest


@pytest.fixture()
def test_list_elements():
    """List generator function"""
    a = [i for i in range(1, 9)]
    return a


@pytest.fixture(scope="session")
def test_sum_two_strings():
    """String addition"""
    a = "somestring"
    b = "anotherstring"
    c = a + b
    return c


@pytest.fixture(scope="function")
def test_sum_two_int():
    """Integers addition"""
    x = 3
    y = 5
    z = x + y
    return z


@pytest.fixture()
def test_tuple():
    """Tuple generator"""
    a = (i for i in [(1, 2)])
    return a


@pytest.fixture()
def test_dict():
    """Dictionary"""
    a = dict(name='James', surname='Bond')
    return a


@pytest.fixture()
def test_set():
    """Set"""
    a = set('otusqacourse')
    return a


@pytest.fixture()
def test_float():
    """float"""
    a = 1.5
    return a


@pytest.fixture(scope="module", autouse=True)
def test_list_operators():
    """List"""
    a = list('Universe')
    return a
