
def rucksack_splitter(rucksack):
    half_len = len(rucksack) // 2
    first_compartment = list(rucksack[:half_len])
    second_compartment = list(rucksack[half_len:])
    return first_compartment, second_compartment


def recurring_item_finder(first_compartment, second_compartment):
    recurring_item = list(set(first_compartment) & set(second_compartment))
    return recurring_item[0]


def item_to_priority_number_converter(item):
    if item.islower():
        priority_number = ord(item) - 96

    if item.isupper():
        priority_number = ord(item) - 38

    return priority_number
