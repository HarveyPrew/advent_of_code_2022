from advent_of_code_2022.elf import Elf
from collections import Counter


def get_file(path):
    return open(path, "r")


def get_calorie_list(path):
    calories = []
    single_calorie = []
    file = get_file(path)

    for line in file:

        if line == "\n":
            finished_calorie_list = list(single_calorie)
            calories.append(finished_calorie_list)
            single_calorie.clear()
            continue

        single_calorie.append(int(line))

    finished_calorie_list = list(single_calorie)
    calories.append(finished_calorie_list)
    return calories


def create_elves(path):
    calories = get_calorie_list(path)
    elves = []
    elf_number = 1

    for element in calories:
        elf = Elf(elf_number, element)
        elves.append(elf)
        elf_number += 1

    return elves


def find_elf_with_most_calories(elves):
    return max(elves, key=lambda elf: elf._calculate_total_calories())


def elf_dictionary_maker(elves):
    elf_dict = dict()
    for elf in elves:
        elf_dict[elf.ID] = sum(elf.calories)

    return elf_dict


def find_top_3_elves_with_most_calories(elves):
    top_3_elves = max(elves, key=lambda elf: elf._calculate_total_calories())[:3]
    return top_3_elves


def get_highest_caloried_elf_info(elves):
    highest_caloried_elf = find_elf_with_most_calories(elves)
    elf_id = highest_caloried_elf.ID
    calories = highest_caloried_elf._calculate_total_calories()
    message = f"Elf {elf_id} has {calories} calories"
    return message


def get_top_3_highest_calories(elves):
    elf_dict = elf_dictionary_maker(elves)

    k = Counter(elf_dict)

    top_3_values = k.most_common(3)

    total_calorie_count = 0
    for value in top_3_values:
        total_calorie_count += value[1]

    return total_calorie_count
