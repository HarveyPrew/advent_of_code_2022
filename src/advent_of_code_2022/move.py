class Move:
    def __init__(self, opponent_move, my_move, outcome):
        self.opponent_move = opponent_move
        self.my_move = my_move
        self.outcome = outcome
        self.move_points = self.calculate_move_points()
        self.outcome_points = self.calculate_outcome_points()
        self.outcome_points_part_2 = self.calculate_outcome_points_part_2()
        self.my_move_when_outcome_given = self.calculate_my_move()
        self.total_points = None
        self.total_points_part_2 = None

    def calculate_outcome_points(self):
        if self.my_move == "rock" and self.opponent_move == "scissors":
            return 6
        elif self.my_move == "paper" and self.opponent_move == "rock":
            return 6
        elif self.my_move == "scissors" and self.opponent_move == "paper":
            return 6
        elif self.my_move == self.opponent_move:
            return 3
        elif self.my_move == 0:
            return 0
        else:
            return 0

    def calculate_outcome_points_part_2(self):
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
    
    def calculate_total_points_part_2(self):
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
