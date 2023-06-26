class Move:
    OUTCOME_POINTS_MAP = {
        ("rock", "scissors"): 6,
        ("paper", "rock"): 6,
        ("scissors", "paper"): 6,
        ("rock", "rock"): 3,
        ("paper", "paper"): 3,
        ("scissors", "scissors"): 3,
    }

    OUTCOME_CONVERTER_MAP = {
        "lose": 0,
        "draw": 3,
        "win": 6,
    }

    MOVE_POINTS_MAP = {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
    }

    MY_MOVE_MAP = {
        ("win", "rock"): 2,
        ("win", "paper"): 3,
        ("win", "scissors"): 1,
        ("draw", "rock"): 1,
        ("draw", "paper"): 2,
        ("draw", "scissors"): 3,
        ("lose", "rock"): 3,
        ("lose", "paper"): 1,
        ("lose", "scissors"): 2,
    }

    def __init__(self, opponent_move, my_move, outcome):
        self.opponent_move = opponent_move
        self.my_move = my_move
        self.outcome = outcome
        self.move_points = self.calculate_move_points()
        self.outcome_points = self.calculate_outcome_points()
        self.outcome_converter = self.calculate_outcome_converter()
        self.my_move_when_outcome_given = self.calculate_my_move()
        self.total_points = None

    def calculate_outcome_points(self):
        if self.my_move == self.opponent_move:
            return Move.OUTCOME_POINTS_MAP.get((self.my_move,
                                                self.opponent_move), 0)
        return 0

    def calculate_outcome_converter(self):
        if self.outcome == "lose":
            return 0
        if self.outcome == "draw":
            return 3
        if self.outcome == "win":
            return 6

    def calculate_move_points(self):
        if self.my_move == "rock":
            return 1

        if self.my_move == "paper":
            return 2

        if self.my_move == "scissors":
            return 3

        else:
            return 0

    def calculate_total_points(self):
        return self.move_points + self.outcome_points

    def calculate_my_move(self):
        if self.outcome == "win" and self.opponent_move == "rock":
            return 2
        if self.outcome == "win" and self.opponent_move == "paper":
            return 3
        if self.outcome == "win" and self.opponent_move == "scissors":
            return 1

        if self.outcome == "draw" and self.opponent_move == "rock":
            return 1
        if self.outcome == "draw" and self.opponent_move == "paper":
            return 2
        if self.outcome == "draw" and self.opponent_move == "scissors":
            return 3

        if self.outcome == "lose" and self.opponent_move == "rock":
            return 3
        if self.outcome == "lose" and self.opponent_move == "paper":
            return 1
        if self.outcome == "lose" and self.opponent_move == "scissors":
            return 2
