"""This is a test suite for basic data types using fixtures."""


def test_list(test_list_elements):
    """Checking that the list length is 8 elements"""
    print(test_list_elements)
    assert len(test_list_elements) == 8


def test_string(test_sum_two_strings):
    """Checking addition of two strings"""
    print(test_sum_two_strings)
    assert test_sum_two_strings == "somestringanotherstring"


def test_int(test_sum_two_int):
    """Checking addition of two integers"""
    print(test_sum_two_int)
    assert test_sum_two_int == 8


def test_tuple_size(test_tuple):
    """Checking tuple size"""
    print(test_tuple)
    assert test_tuple.__sizeof__() == 96


def test_dict_name(test_dict):
    """Checking the dictionary value"""
    print(test_dict)
    assert test_dict['name'] == 'James'


def test_set_false(test_set):
    """Checking that the set contains values"""
    print(test_set)
    assert bool(test_set) is True


def test_float_type(test_float):
    """Checking variable type"""
    print(test_float)
    assert type(test_float) is float


def test_list_index_number(test_list_operators):
    """Checking index value of list"""
    print(test_list_operators)
    assert test_list_operators.index('r') == 5


def test_list_index_count(test_list_operators):
    """Checking for duplicate values of list"""
    print(test_list_operators)
    assert test_list_operators.count('e') == 2


def test_list_index_min(test_list_operators):
    """Checking minimal value of list"""
    print(test_list_operators)
    assert min(test_list_operators) == 'U'
