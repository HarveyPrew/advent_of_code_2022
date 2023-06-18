from advent_of_code_2022.day_1 import elfList


def test_list_of_elves_is_correct():
    elf_list = elfList()
    assert len(elf_list) == 5
