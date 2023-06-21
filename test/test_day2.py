from advent_of_code_2022.day_2 import get_file, point_receiver
from advent_of_code_2022.move import Move


def test_file_opens():
    opened_file = get_file('input_day_2_test.txt')
    assert opened_file is not None


def test_move_score_is_correct():
    score = point_receiver('input_day_2_test.txt')
    assert score == 15


def test_win_found_rock():
    move = Move('C', 'X')
    assert move.calculate_result_points() == 6


def test_win_found_paper():
    move = Move('A', 'Y')
    assert move.calculate_result_points() == 6


def test_win_found_scissors():
    move = Move('B', 'Z')
    assert move.calculate_result_points() == 6


def test_draw_found_rock():
    move = Move('A', 'X')
    assert move.calculate_result_points() == 3


def test_draw_found_paper():
    move = Move('B', 'Y')
    assert move.calculate_result_points() == 3


def test_draw_found_scissors():
    move = Move('C', 'Z')
    assert move.calculate_result_points() == 3


def test_lost_found_rock():
    move = Move('B', 'X')
    assert move.calculate_result_points() == 0


def test_lost_found_paper():
    move = Move('C', 'Y')
    assert move.calculate_result_points() == 0


def test_lost_found_scissors():
    move = Move('A', 'Z')
    assert move.calculate_result_points() == 0
