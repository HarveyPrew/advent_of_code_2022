class Move:
    def __init__(self, oppenent_move, my_move):
        self.oppenent_move = oppenent_move
        self.my_move = my_move
        self.move_points = self.calculate_move_points()
        self.outcome_points = self.calculate_outcome_points()
        self.total_points = self.calculate_total_points()

    def calculate_outcome_points(self):
        if self.my_move == "rock" and self.oppenent_move == "scissors":
            return 6
        elif self.my_move == "paper" and self.oppenent_move == "rock":
            return 6
        elif self.my_move == "scissors" and self.oppenent_move == "paper":
            return 6
        elif self.my_move == self.oppenent_move:
            return 3
        else:
            return 0

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
