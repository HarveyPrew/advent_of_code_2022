class Move:
    def __init__(self, oppenent_move, my_move):
        self.oppenent_move = oppenent_move
        self.my_move = my_move
        self.move_points = None
        self.outcome_points = 0
        self.total_points = None

    def calculate_move_points(self):
        if self.my_move == "X":
            self.move_points = 1

        if self.my_move == "Y":
            self.move_points = 2

        if self.my_move == "Z":
            self.move_points = 3

        return self.move_points

    def return_win_points(self, oppenent, me):
        if oppenent in self.oppenent_move and me in self.my_move:
            self.outcome_points = 6
        return self.outcome_points
    
    def return_draw_points(self, oppenent, me):
        if oppenent in self.oppenent_move and me in self.my_move:
            self.outcome_points = 3
        return self.outcome_points

    def calculate_result_points(self):
        self.outcome_points = self.return_win_points("C", "X")
        self.outcome_points = self.return_win_points("A", "Y")
        self.outcome_points = self.return_win_points("B", "Z")

        self.outcome_points = self.return_draw_points("B", "Y")
        self.outcome_points = self.return_draw_points("A", "X")
        self.outcome_points = self.return_draw_points("C", "Z")

        return self.outcome_points

    def calculate_total_points(self):
        self.total_points = self.move_points + self.outcome_points
        return (self.total_points)
