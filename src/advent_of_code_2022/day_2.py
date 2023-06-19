def get_file(path):
    return open(path, "r")


def point_receiver(path):
    score = 0

    with get_file(path) as file:
        for line in file:
            move = line.strip()

            if "X" in move:
                score += 1

            if "Y" in move:
                score += 2

            if "Z" in move:
                score += 3

    return score
