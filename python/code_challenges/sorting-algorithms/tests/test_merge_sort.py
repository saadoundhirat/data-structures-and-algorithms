import pytest

from labs_solution.merge_sort.merge_sort import merge_sort

# test merge_sort
def test_merge_sort_one_element():
    """test if the list has one element"""
    assert merge_sort([1]) == [1]


def test_merge_sort():
    """test if the list has more than one elements"""
    assert merge_sort([8, 4, 23, 42, 16, 15]) == [4, 8, 15, 16, 23, 42]
    assert merge_sort([8, 4, 23, 42, 16, 15, 1]) == [1, 4, 8, 15, 16, 23, 42]