from advent_of_code_2022.day_3 import (bag_splitter,
                                       recurring_item_finder,
                                       convert_item_to_priority_number,
                                       find_sum_of_priority_numbers,
                                       parse_bags,
                                       group_bags,
                                       sum_priority_number_for_groups)


def test_bag_split():
    bag = "vJrw"
    first_compartment, second_compartment = bag_splitter(bag)
    assert first_compartment == ['v', 'J']
    assert second_compartment == ['r', 'w']


def test_item_in_both_compartments():
    first_compartment = ['v', 'J', 'r']
    second_compartment = ['r', 'w', 'z']

    recurring_item = recurring_item_finder(first_compartment,
                                           second_compartment,
                                           compartment_3=None)
    assert recurring_item == 'r'


def test_item_converts_lower():
    item = 'a'
    priority_number = convert_item_to_priority_number(item)

    assert priority_number == 1


def test_item_converts_upper():
    item = 'A'
    priority_number = convert_item_to_priority_number(item)

    assert priority_number == 27


def test_sum_of_priorities_test():
    bags = parse_bags("input_day_3_test.txt")
    sum_of_priorities = find_sum_of_priority_numbers(bags)

    assert sum_of_priorities == 157


def test_sum_of_priorities():
    bags = parse_bags("input_day_3.txt")
    sum_of_priorities = find_sum_of_priority_numbers(bags)

    assert sum_of_priorities == 7597


def test_sum_of_three_bags_test():
    bags = parse_bags("input_day_3_test.txt")
    total_score = sum_priority_number_for_groups(bags, 3)

    assert total_score == 70


def test_sum_of_three_bags():
    bags = parse_bags("input_day_3.txt")
    total_score = sum_priority_number_for_groups(bags, 3)

    assert total_score == 2607


def test_three_bag_merger():
    bags = ["vJrw", "zvqa", "cdvg",
            "vJrw", "zvqa", "cdvg",
            "vJrw", "zvqa", "cdvg"]

    three_bags = group_bags(bags, 3)

    assert three_bags == [["vJrw", "zvqa", "cdvg"],
                          ["vJrw", "zvqa", "cdvg"],
                          ["vJrw", "zvqa", "cdvg"]]

