def parse_ruck_sacks(path):
    ruck_sacks = list()
    with open(path) as f:
        for line in f:
            ruck_sack = line.strip()
            ruck_sacks.append(ruck_sack)

    return ruck_sacks


def rucksack_splitter(ruck_sack):
    half_len = len(ruck_sack) // 2
    first_compartment = list(ruck_sack[:half_len])
    second_compartment = list(ruck_sack[half_len:])
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


def find_priority_number_for_bag(ruck_sack):
    first_compartment, second_compartment = rucksack_splitter(ruck_sack)
    recurring_item = recurring_item_finder(first_compartment,
                                           second_compartment)
    priority_number = item_to_priority_number_converter(recurring_item)
    return priority_number


def find_sum_of_priority_numbers(ruck_sacks):
    total_score = sum(find_priority_number_for_bag(ruck_sack)
                      for ruck_sack in ruck_sacks)
    return total_score
