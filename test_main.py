import pytest
from main import heapsort

def test_empty_list():
    assert heapsort([]) == []

def test_single_element():
    assert heapsort([1]) == [1]

def test_already_sorted():
    arr = [1, 2, 3, 4, 5]
    assert heapsort(arr.copy()) == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    arr = [5, 4, 3, 2, 1]
    assert heapsort(arr.copy()) == [1, 2, 3, 4, 5]

def test_duplicates():
    arr = [2, 3, 2, 1, 3]
    assert heapsort(arr.copy()) == [1, 2, 2, 3, 3]

def test_negative_numbers():
    arr = [-2, -1, -3, 0]
    assert heapsort(arr.copy()) == [-3, -2, -1, 0]

def test_all_identical():
    arr = [7, 7, 7, 7]
    assert heapsort(arr.copy()) == [7, 7, 7, 7]

def test_large_list():
    arr = list(range(10000, 0, -1))
    assert heapsort(arr.copy()) == sorted(arr)

def test_mixed_types():
    arr = [3, -1, 0, 2, -5, 8, 8, 2]
    assert heapsort(arr.copy()) == sorted(arr)

def test_mixed_types_int_float():
    arr = [3, 1.5, 2, 4.2, 0]
    assert heapsort(arr.copy()) == sorted(arr)

def test_float_values():
    arr = [2.5, 3.1, 1.0, 2.5, -1.2]
    assert heapsort(arr.copy()) == sorted(arr)

def test_list_with_zero():
    arr = [0, 0, 0, 0]
    assert heapsort(arr.copy()) == [0, 0, 0, 0]

def test_list_with_large_negative_numbers():
    arr = [-1000000, -999999, -1000001, 0]
    assert heapsort(arr.copy()) == sorted(arr)

def test_list_with_boolean():
    arr = [True, False, True]
    assert heapsort(arr.copy()) == sorted(arr)

def test_list_with_strings():
    arr = ["apple", "banana", "pear", "banana"]
    assert heapsort(arr.copy()) == sorted(arr)

def test_list_with_mixed_types():
    arr = [1, "a", 2]
    with pytest.raises(TypeError):
        heapsort(arr.copy())