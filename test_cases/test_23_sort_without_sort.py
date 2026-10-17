import importlib

module = importlib.import_module("23_sort_without_sort")
sort_without_sort = module.sort_without_sort


def test_normal_list():
    assert sort_without_sort([5, 2, 8, 1, 3]) == [1, 2, 3, 5, 8]


def test_already_sorted_list():
    assert sort_without_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_reverse_sorted_list():
    assert sort_without_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_duplicate_numbers():
    assert sort_without_sort([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]


def test_negative_numbers():
    assert sort_without_sort([-3, 5, -1, 0]) == [-3, -1, 0, 5]


def test_empty_list():
    assert sort_without_sort([]) == []


def test_original_list_unchanged():
    numbers = [4, 2, 1]
    sort_without_sort(numbers)
    assert numbers == [4, 2, 1]