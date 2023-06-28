def parse_bags(path):
    bags = list()
    with open(path) as f:
        for line in f:
            bag = line.strip()
            bags.append(bag)

    return bags


def bag_splitter(bag):
    half_len = len(bag) // 2
    first_compartment = list(bag[:half_len])
    second_compartment = list(bag[half_len:])
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


def find_priority_number_for_bag(bag):
    first_compartment, second_compartment = bag_splitter(bag)
    recurring_item = recurring_item_finder(first_compartment,
                                           second_compartment)
    priority_number = item_to_priority_number_converter(recurring_item)
    return priority_number


def find_sum_of_priority_numbers(bags):
    total_score = sum(find_priority_number_for_bag(bag)
                      for bag in bags)
    return total_score
