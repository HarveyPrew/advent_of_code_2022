class Move:
    def __init__(self, oppenent_move, my_move):
        self.oppenent_move = oppenent_move
        self.my_move = my_move
        self.move_points = None
        self.outcome_points = 0
        self.total_points = None

    def calculate_move_points(self):
        if "X" in self.my_move:
            self.move_points = 1

        if "Y" in self.my_move:
            self.move_points = 2

        if "Z" in self.my_move:
            self.move_points = 3

        return self.move_points

    def calculate_result_points(self):
        if "C" in self.oppenent_move and "X" in self.my_move:
            self.outcome_points = 6
        if "A" in self.oppenent_move and "Y" in self.my_move:
            self.outcome_points = 6
        if "B" in self.oppenent_move and "Z" in self.my_move:
            self.outcome_points = 6

        return self.outcome_points

    def calculate_total_points(self):
        self.total_points = self.move_points + self.outcome_points
        return (self.total_points)
