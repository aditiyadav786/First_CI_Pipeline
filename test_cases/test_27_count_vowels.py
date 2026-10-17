import importlib

module = importlib.import_module("27_count_vowels")
count_vowels = module.count_vowels


def test_normal_string():
    assert count_vowels("Hello World") == 3


def test_empty_string():
    assert count_vowels("") == 0


def test_uppercase_vowels():
    assert count_vowels("AEIOU") == 5


def test_no_vowels():
    assert count_vowels("rhythm") == 0


def test_all_vowels():
    assert count_vowels("aeiouaeiou") == 10