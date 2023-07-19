
def parse_assignment_pairs(path):
    assignments = list()
    with open(path) as f:
        for line in f:
            assignment = list(line.strip().partition(','))
            assignment.pop(1)
            assignments.append(assignment)

    return assignments
