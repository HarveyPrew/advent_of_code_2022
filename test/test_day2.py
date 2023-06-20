from advent_of_code_2022.day_2 import get_file, point_receiver
from advent_of_code_2022.move import Move


def test_file_opens():
    opened_file = get_file('input_day_2_test.txt')
    assert opened_file is not None


def test_move_score_is_correct():
    score = point_receiver('input_day_2_test.txt')
    assert score == 6


def test_win_found():
    move = Move('C', 'X')
    assert move.calculate_result_points() == 6
