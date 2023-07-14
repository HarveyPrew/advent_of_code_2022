
def parse_assignment_pairs(path):
    bags = list()
    with open(path) as f:
        for line in f:
            bag = line.strip()
            bags.append(bag)

    return bags
