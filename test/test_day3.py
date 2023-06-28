from advent_of_code_2022.day_3 import (rucksack_splitter, 
                                       recurring_item_finder,
                                       item_to_priority_number_converter)


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
    sum_of_priorities = 0
    with open('input_day_3_test.txt') as f:
        for line in f:
            rucksack = line.strip()
            first_compartment, second_compartment = rucksack_splitter(rucksack)
            recurring_item = recurring_item_finder(first_compartment,
                                                   second_compartment)
            priority_number = item_to_priority_number_converter(recurring_item)
            sum_of_priorities += priority_number

    assert sum_of_priorities == 157
