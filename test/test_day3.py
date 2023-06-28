from advent_of_code_2022.day_3 import rucksack_splitter, recurring_item_finder


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
    assert recurring_item == ['r']
