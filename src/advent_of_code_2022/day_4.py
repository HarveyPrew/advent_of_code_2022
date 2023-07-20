
def parse_assignment_pairs(path):
    list_of_section_assignment_pairs = list()
    with open(path) as f:
        for line in f:
            section_assignment_pairs = line.strip().split(',')
            sap = assignments_converter(section_assignment_pairs)
            list_of_section_assignment_pairs.append(sap)

    return list_of_section_assignment_pairs


def range_extractor(section_assignment):
    start, _, end = section_assignment.partition('-')
    assignment_range = list(range(int(start), int(end) + 1))
    return assignment_range


def assignments_converter(section_assignment_pairs):
    sap = [range_extractor(assignment) for
           assignment in section_assignment_pairs]
    return sap


def identify_duplicate_ranges(sap):
    section_assignments1, section_assignments2 = sap
    set_assignments1 = set(section_assignments1)
    set_assignments2 = set(section_assignments2)

    return (set_assignments1.issubset(set_assignments2) or
            set_assignments2.issubset(set_assignments1))


def identify_any_overlap(sap):
    section_assignments1, section_assignments2 = sap
    return (set(section_assignments2) & set(section_assignments1))


def shared_ranges_count(list_of_section_assignment_pairs):
    duplicate_pair_list = [identify_duplicate_ranges(pair)
                           for pair in list_of_section_assignment_pairs]

    shared_range_count = sum(bool(x) for x in duplicate_pair_list)
    return shared_range_count


def shared_overlap_count(list_of_section_assignment_pairs):
    duplicate_pair_list = [identify_any_overlap(pair)
                           for pair in list_of_section_assignment_pairs]

    shared_range_count = sum(bool(x) for x in duplicate_pair_list)
    return shared_range_count
