from advent_of_code_2022.day_2 import (parseRounds, scoreRounds)
from advent_of_code_2022.move import Move


def test_point_receiver_part_2_is_correct_test():
    rounds = parseRounds('input_day_2_test.txt')
    score = scoreRounds(rounds)
    assert score == 12


def test_point_receiver_part_2_is_correct():
    rounds = parseRounds('input_day_2.txt')
    score = scoreRounds(rounds)
    assert score == 10334

