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


def recurring_item_finder(first_compartment,
                          second_compartment,
                          third_compartment):
    if third_compartment is None:
        recurring_item = list(set(first_compartment) &
                              set(second_compartment))
    else:
        recurring_item = list(set(first_compartment) &
                              set(second_compartment) &
                              set(third_compartment))

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
                                           second_compartment,
                                           third_compartment=None)
    priority_number = item_to_priority_number_converter(recurring_item)
    return priority_number


def find_sum_of_priority_numbers(bags):
    total_score = sum(find_priority_number_for_bag(bag)
                      for bag in bags)
    return total_score


def three_bag_merger(bags):
    bags_of_three = list()
    three_bags = list()
    for count, bag in enumerate(bags, start=1):
        if count % 3 == 0:
            three_bags.append(bag)
            three_bags_filled = list(three_bags)
            bags_of_three.append(three_bags_filled)
            three_bags.clear()
        else:
            three_bags.append(bag)

    return bags_of_three


def find_priority_number_for_bags_of_three(path):
    bags = parse_bags(path)
    bags_of_three = three_bag_merger(bags)
    total_score = 0

    for bags in bags_of_three:
        recurring_item = recurring_item_finder(bags[0],
                                               bags[1],
                                               bags[2])
        priority_number = item_to_priority_number_converter(recurring_item)
        total_score += priority_number

    return total_score
