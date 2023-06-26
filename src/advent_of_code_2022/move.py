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
        return Move.OUTCOME_POINTS_MAP.get((self.my_move, self.opponent_move),
                                           0)

    def calculate_outcome_converter(self):
        return Move.OUTCOME_CONVERTER_MAP.get(self.outcome, 0)

    def calculate_move_points(self):
        return Move.MOVE_POINTS_MAP.get(self.my_move, 0)

    def calculate_total_points(self):
        return self.move_points + self.outcome_points

    def calculate_my_move(self):
        return Move.MY_MOVE_MAP.get((self.outcome, self.opponent_move), 0)
