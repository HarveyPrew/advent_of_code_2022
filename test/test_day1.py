from advent_of_code_2022.day_1 import elfList, Elf, elfWithMostCalories


def test_list_of_elves_is_correct():
    elf_list = elfList()
    assert len(elf_list) == 5


def test_if_calories_is_calculated():
    elf_test = Elf(1, [20, 30])
    total_calories = elf_test._calculate_total_calories()
    assert total_calories == 50


def test_right_elf_is_selected():
    elf_with_most_calories = elfWithMostCalories()
    assert elf_with_most_calories == 4
