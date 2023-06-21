from advent_of_code_2022.day_2 import point_receiver, outcome_converter
from advent_of_code_2022.move import Move


def test_total_score_is_correct_test():
    score = point_receiver('input_day_2_test.txt')
    assert score == 15


def test_outcome_converter():
    raw_move = "A X"
    outcome = outcome_converter(raw_move[2], "X", "Y", "Z")
    assert outcome == "lose"


def test_total_score_is_correct():
    score = point_receiver('input_day_2.txt')
    assert score == 10404


def test_win_found_rock():
    move = Move('scissors', 'rock')
    assert move.total_points == 7


def test_win_found_paper():
    move = Move('rock', 'paper')
    assert move.total_points == 8


def test_win_found_scissors():
    move = Move('paper', 'scissors')
    assert move.total_points == 9


def test_draw_found_rock():
    move = Move('rock', 'rock')
    assert move.total_points == 4


def test_draw_found_paper():
    move = Move('paper', 'paper')
    assert move.total_points == 5


def test_draw_found_scissors():
    move = Move('scissors', 'scissors')
    assert move.total_points == 6


def test_lost_found_rock():
    move = Move('paper', 'rock')
    assert move.total_points == 1


def test_lost_found_paper():
    move = Move('scissors', 'paper')
    assert move.total_points == 2


def test_lost_found_scissors():
    move = Move('rock', 'scissors')
    assert move.total_points == 3
