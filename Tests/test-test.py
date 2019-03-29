import pytest


@pytest.fixture()
def test_list_elements():
    a = [i for i in range(1, 9)]
    return a


def test_list(test_list_elements):
    print(test_list_elements)
    assert len(test_list_elements) == 8


@pytest.fixture()
def test_sum_two_strings():
    a = "somestring"
    b = "anotherstring"
    c = a + b
    return c


def test_string(test_sum_two_strings):
    print(test_sum_two_strings)
    assert test_sum_two_strings == "somestringanotherstring"


@pytest.fixture()
def test_sum_two_int():
    x = 4
    y = 5
    z = x + y
    return z


def test_int(test_sum_two_int):
    print(test_sum_two_int)
    assert test_sum_two_int == 8

# Добавить тесты на:
#     1. Кортежи
#     2. Множества
#     3. Словари
#     4. Можно float
#     5. Что ещё? Смешать типы? надо еще три теста
