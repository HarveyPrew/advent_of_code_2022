from advent_of_code_2022.day_4 import parse_assignment_pairs


def test_parse_assignments():
    list_of_pairs = parse_assignment_pairs("input_day_4_test.txt")

    assert list_of_pairs == ['2-88,13-89',
                             '12-94,12-94',
                             '34-69,34-61']
