from advent_of_code_2022.day_3 import rucksack_splitter


def test_rucksack_splits():
    rucksack = "vJrw"
    first_compartment, second_compartment = rucksack_splitter(rucksack)
    assert first_compartment == 'vJ'
    assert second_compartment == 'rw'
