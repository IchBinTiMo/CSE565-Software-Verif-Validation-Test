import pytest
from main import heapsort

def test_large_list():
    arr = list(range(1000, 0, -1))
    assert heapsort(arr.copy()) == sorted(arr)

def test_mixed_types_int_float():
    arr = [3, 1.5, 2, 4.2, 0]
    assert heapsort(arr.copy()) == sorted(arr)

def test_list_with_none():
    arr = [3, None, 2]
    with pytest.raises(TypeError):
        heapsort(arr.copy())

def test_list_with_strings():
    arr = ["apple", "banana", "pear", "banana"]
    assert heapsort(arr.copy()) == sorted(arr)

def test_list_with_mixed_types():
    arr = [1, "a", 2]
    with pytest.raises(TypeError):
        heapsort(arr.copy())

def test_sorted_output_is_new_object():
    arr = [5, 4, 3, 2, 1]
    result = heapsort(arr.copy())
    assert result is not arr

def test_list_with_boolean():
    arr = [True, False, True]
    assert heapsort(arr.copy()) == sorted(arr)

def test_list_with_large_negative_numbers():
    arr = [-1000000, -999999, -1000001, 0]
    assert heapsort(arr.copy()) == sorted(arr)

def test_list_with_floats():
    arr = [3.1, 2.4, 5.6, 1.0]
    assert heapsort(arr.copy()) == sorted(arr)

def test_list_with_repeated_floats():
    arr = [2.2, 2.2, 2.2]
    assert heapsort(arr.copy()) == sorted(arr)