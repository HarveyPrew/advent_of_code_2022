from advent_of_code_2022.move import Move


def move_converter(move, rock, paper, scissors):
    if move == rock:
        return "rock"
    if move == paper:
        return "paper"
    if move == scissors:
        return "scissors"


def outcome_converter(move, lose, draw, win):
    if move == lose:
        return "lose"
    if move == draw:
        return "draw"
    if move == win:
        return "win"


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


def point_receiver_part_2(path):
    score = 0

    with open(path, "r") as file:
        for line in file:
            raw_move = line.strip()
            opponent_move = move_converter(raw_move[0], "A", "B", "C")
            outcome = outcome_converter(raw_move[2], "X", "Y", "Z")

            if outcome == "lose":
                score += 0
            if outcome == "draw":
                score += 3
            if outcome == "win":
                score += 6

            if outcome == "win" and opponent_move == "rock":
                score += 2
            if outcome == "win" and opponent_move == "paper":
                score += 3
            if outcome == "win" and opponent_move == "scissors":
                score += 1

            if outcome == "draw" and opponent_move == "rock":
                score += 1
            if outcome == "draw" and opponent_move == "paper":
                score += 2
            if outcome == "draw" and opponent_move == "scissors":
                score += 3

            if outcome == "lose" and opponent_move == "rock":
                score += 3
            if outcome == "lose" and opponent_move == "paper":
                score += 1
            if outcome == "lose" and opponent_move == "scissors":
                score += 2
    
    return score
