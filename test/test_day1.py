from advent_of_code_2022.day_1 import (create_elves, Elf,
                                       find_elf_with_most_calories,
                                       get_highest_caloried_elf_info,
                                       get_file,
                                       get_calorie_list)


def test_list_of_elves_is_correct():
    elf_list = create_elves()
    assert len(elf_list) == 5


def test_if_calories_is_calculated():
    elf_test = Elf(1, [20, 30])
    total_calories = elf_test._calculate_total_calories()
    assert total_calories == 50


def test_right_elf_is_selected():
    elves = create_elves()
    elf_with_most_calories = find_elf_with_most_calories(elves)
    assert elf_with_most_calories.ID == 4


def test_highest_caloried_elf_info_is_correct():
    highest_caloried_elf_info = get_highest_caloried_elf_info()
    assert highest_caloried_elf_info == "Elf 4 has 24000 calories"


def test_file_opens():
    opened_file = get_file('input_day_1.txt')
    assert opened_file is not None


def test_calorie_list_filled():
    calorie_list = get_calorie_list('input_day_1.txt')
    assert calorie_list is not None
