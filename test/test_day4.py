from advent_of_code_2022.day_4 import (parse_assignment_pairs,
                                       range_extractor)


def test_parse_assignments():
    list_of_pairs = parse_assignment_pairs("input_day_4_test.txt")

    assert list_of_pairs is not None


def test_string_to_range():
    string_range = '3-6'

    actual_answer = range_extractor(string_range)

    assert actual_answer == [3, 4, 5, 6]

