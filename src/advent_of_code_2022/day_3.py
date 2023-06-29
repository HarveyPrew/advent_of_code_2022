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


def recurring_item_finder(compartment_1,
                          compartment_2,
                          compartment_3):
    if compartment_3 is None:
        recurring_item = list(set(compartment_1) &
                              set(compartment_2))
    else:
        recurring_item = list(set(compartment_1) &
                              set(compartment_2) &
                              set(compartment_3))

    return recurring_item[0]


def convert_item_to_priority_number(item):
    if item.islower():
        priority_number = ord(item) - 96

    if item.isupper():
        priority_number = ord(item) - 38

    return priority_number


def find_priority_number_for_bag(bag):
    first_compartment, second_compartment = bag_splitter(bag)
    recurring_item = recurring_item_finder(first_compartment,
                                           second_compartment,
                                           compartment_3=None)
    priority_number = convert_item_to_priority_number(recurring_item)
    return priority_number


def find_priority_number_for_three_bags(grouped_bags):
    recurring_item = recurring_item_finder(*grouped_bags)
    priority_number = convert_item_to_priority_number(recurring_item)
    return priority_number


def find_sum_of_priority_numbers(bags):
    total_score = sum(find_priority_number_for_bag(bag)
                      for bag in bags)
    return total_score


def group_bags(bags, group_size):
    grouped_bags = [bags[i:i + group_size]
                    for i in range(0, len(bags), group_size)]
    return grouped_bags


def sum_priority_number_for_groups(bags, group_size):
    grouped_bags = group_bags(bags, group_size)
    total_score = sum(find_priority_number_for_three_bags(grouped_bags)
                      for grouped_bags in grouped_bags)
    return total_score
