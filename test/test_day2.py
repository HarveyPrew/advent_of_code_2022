from advent_of_code_2022.day_2 import (point_receiver, point_receiver_when_outcome_given,
                                       outcome_converter)
from advent_of_code_2022.move import Move


def test_point_receiver_part_2_is_correct_test():
    score = point_receiver_when_outcome_given('input_day_2_test.txt')
    assert score == 12


def test_point_receiver_part_2_is_correct():
    score = point_receiver_when_outcome_given('input_day_2.txt')
    assert score == 10334


def test_outcome_converter():
    raw_move = "A X"
    outcome = outcome_converter(raw_move[2], "X", "Y", "Z")
    assert outcome == "lose"

