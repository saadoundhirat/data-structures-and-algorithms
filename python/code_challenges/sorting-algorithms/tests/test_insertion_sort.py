import pytest
from labs_solution.insertion_sort.insertion_sort  import insertion_sort


# if list has no element 
def test_insertion_sort_empty():
    assert insertion_sort([]) == []

# if list has one element 
def test_insertion_sort_one_element():
    assert insertion_sort([29]) == [29]

# test some cases list 
def test_insertion_sort():
    assert insertion_sort([8,4,23,42,16,15]) == [4,8,15,16,23,42]
    assert insertion_sort([20,18,12,8,5,-2]) == [-2,5,8,12,18,20]
    assert insertion_sort([5,12,7,5,5,7]) == [5,5,5,7,7,12]
    assert insertion_sort([2,3,5,7,13,11]) == [2,3,5,7,11,13]