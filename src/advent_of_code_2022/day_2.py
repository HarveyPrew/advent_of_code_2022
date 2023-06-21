from advent_of_code_2022.move import Move


def get_file(path):
    return open(path, "r")


def point_receiver(path):
    score = 0

    with get_file(path) as file:
        for line in file:
            raw_move = line.strip()

            move = Move(raw_move[0], raw_move[2])
            move.calculate_move_points()
            move.calculate_result_points()
            move.calculate_total_points()
            score += move.total_points

    return score
