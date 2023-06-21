from advent_of_code_2022.move import Move


def move_converter(move, rock, paper, scissors):
    if move == rock:
        return "rock"
    if move == paper:
        return "paper"
    if move == scissors:
        return "scissors"


def point_receiver(path):
    score = 0

    with open(path, "r") as file:
        for line in file:
            raw_move = line.strip()
            opponent_move = move_converter(raw_move[0], "A", "B", "C")
            my_move = move_converter(raw_move[2], "X", "Y", "Z")

            move = Move(opponent_move, my_move)
            score += move.total_points

    return score
