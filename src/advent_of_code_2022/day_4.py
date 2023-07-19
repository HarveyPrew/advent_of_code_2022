
def parse_assignment_pairs(path):
    list_of_section_assignment_pairs = list()
    with open(path) as f:
        for line in f:
            section_assignment_pairs = list(line.strip().partition(','))
            section_assignment_pairs.remove(',')
            list_of_section_assignment_pairs.append(section_assignment_pairs)

    return list_of_section_assignment_pairs


def range_extractor(section_assignment):
    assignment_split = list(section_assignment.partition('-'))
    assignment_split.remove('-')
    assignment_range = [eval(i) for i in assignment_split]
    full_assignment_range = list(range(assignment_range[0], assignment_range[1] + 1))
    return full_assignment_range
