from advent_of_code_2022.day_2 import get_file


def test_file_opens():
    opened_file = get_file('input_day_2_test.txt')
    assert opened_file is not None
