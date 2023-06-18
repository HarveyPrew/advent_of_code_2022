class Elf:
    def __init__(self, ID, calories):
        self.ID = ID
        self.calories = calories

    def _calculate_total_calories(self):
        # Calculate the total amount of calories.
        return sum(self.calories)