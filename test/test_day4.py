from advent_of_code_2022.day_4 import (parse_assignment_pairs,
                                       range_extractor,
                                       identify_duplicate_ranges,
                                       shared_ranges_count,
                                       shared_overlap_count)


def test_parse_assignments():
    list_of_pairs = parse_assignment_pairs("input_day_4_test.txt")

    assert list_of_pairs is not None


def test_parse_assignments_len():
    list_of_pairs = parse_assignment_pairs("input_day_4.txt")

    assert len(list_of_pairs) == 1000


def test_string_to_range():
    string_range = '3-6'

    actual_answer = range_extractor(string_range)

    assert actual_answer == [3, 4, 5, 6]


def test_identify_full_ranges():
    section_assignment_pairs = [[1, 2, 3], [1, 2, 3, 4]]

    actual_answer = identify_duplicate_ranges(section_assignment_pairs)

    assert actual_answer is True


def test_identify_full_ranges_other_way():
    section_assignment_pairs = [[1, 2, 3, 4], [1, 2, 3]]

    actual_answer = identify_duplicate_ranges(section_assignment_pairs)

    assert actual_answer is True


def test_identify_number_of_shared_ranges():
    list_of_section_assignment_pairs = [[[1, 2, 3, 4, 5], [2, 3]],
                                        [[4, 5], [1, 2, 3]],
                                        [[1, 2, 3, 4], [1, 2, 3]],
                                        [[1, 2, 3, 4, 5], [5, 6, 7]]]

    actual_answer = shared_ranges_count(list_of_section_assignment_pairs)

    assert actual_answer == 2


def test_shared_range():
    list_of_pairs = parse_assignment_pairs("input_day_4.txt")
    actual_answer = shared_ranges_count(list_of_pairs)

    assert actual_answer == 515


def test_shared_overlap():
    list_of_pairs = parse_assignment_pairs("input_day_4.txt")
    actual_answer = shared_overlap_count(list_of_pairs)

    assert actual_answer == 883
