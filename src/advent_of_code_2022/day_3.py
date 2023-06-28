
def rucksack_splitter(rucksack):
    half_len = len(rucksack) // 2
    first_compartment = list(rucksack[:half_len])
    second_compartment = list(rucksack[half_len:])
    return first_compartment, second_compartment


def recurring_item_finder(first_compartment, second_compartment):
    recurring_item = list(set(first_compartment) & set(second_compartment))
    return recurring_item
