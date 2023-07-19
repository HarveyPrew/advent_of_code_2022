
def parse_assignment_pairs(path):
    list_of_section_assignment_pairs = list()
    with open(path) as f:
        for line in f:
            section_assignment_pairs = list(line.strip().partition(','))
            section_assignment_pairs.remove(',')
            sap = assignments_converter(section_assignment_pairs)
            list_of_section_assignment_pairs.append(sap)

    return list_of_section_assignment_pairs


def range_extractor(section_assignment):
    assignment_split = list(section_assignment.partition('-'))
    assignment_split.remove('-')
    assignment_range = [eval(i) for i in assignment_split]
    full_assignment_range = list(range(assignment_range[0],
                                       assignment_range[1] + 1))
    return full_assignment_range


def assignments_converter(section_assignment_pairs):
    sap = section_assignment_pairs
    for assignment in range(len(sap)):
        sap[assignment] = range_extractor(sap[assignment])

    return sap


def identify_duplicate_ranges(section_assignment_pairs):
    if any(x in section_assignment_pairs[0]
           for x in section_assignment_pairs[1]):
        return True
    else:
        return False


def shared_ranges_count(list_of_section_assignment_pairs):
    shared_range_count = 0

    for pair in list_of_section_assignment_pairs:
        if identify_duplicate_ranges(pair) is True:
            shared_range_count += 1

    return shared_range_count
