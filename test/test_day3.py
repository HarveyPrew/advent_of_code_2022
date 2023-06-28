from advent_of_code_2022.day_3 import (rucksack_splitter,
                                       recurring_item_finder,
                                       item_to_priority_number_converter,
                                       find_sum_of_priority_numbers,
                                       parse_ruck_sacks)


def test_rucksack_splits():
    rucksack = "vJrw"
    first_compartment, second_compartment = rucksack_splitter(rucksack)
    assert first_compartment == ['v', 'J']
    assert second_compartment == ['r', 'w']


def test_item_in_both_compartments():
    first_compartment = ['v', 'J', 'r']
    second_compartment = ['r', 'w', 'z']

    recurring_item = recurring_item_finder(first_compartment,
                                           second_compartment)
    assert recurring_item == 'r'


def test_item_converts_lower():
    item = 'a'
    priority_number = item_to_priority_number_converter(item)

    assert priority_number == 1


def test_item_converts_upper():
    item = 'A'
    priority_number = item_to_priority_number_converter(item)

    assert priority_number == 27


def test_sum_of_priorities():
    ruck_sacks = parse_ruck_sacks("input_day_3_test.txt")
    sum_of_priorities = find_sum_of_priority_numbers(ruck_sacks)

    assert sum_of_priorities == 157
