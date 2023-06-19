from advent_of_code_2022.elf import Elf
from collections import Counter


def get_file(path):
    return open(path, "r")


def get_calorie_list(path):
    calories = []
    single_calorie = []

    with get_file(path) as file:
        for line in file:
            calorie = line.strip()

            if not calorie:
                finished_calorie_list = list(single_calorie)
                calories.append(finished_calorie_list)
                single_calorie.clear()

            else:
                single_calorie.append(int(calorie))

    calories.append(finished_calorie_list)
    return calories


def create_elves(path):
    calorie_list = get_calorie_list(path)
    elves = []

    for id, calorie in enumerate(calorie_list, start=1):
        elf = Elf(id, calorie)
        elves.append(elf)

    return elves


def find_elf_with_most_calories(elves):
    return max(elves, key=lambda elf: elf._calculate_total_calories())


def create_elf_dictionary(elves):
    elf_dict = {elf.ID: sum(elf.calories) for elf in elves}
    return elf_dict


def find_top_3_elves_with_most_calories(elves):
    top_3_elves = max(elves,
                      key=lambda elf: elf._calculate_total_calories())[:3]
    return top_3_elves


def get_highest_caloried_elf_info(elves):
    highest_caloried_elf = find_elf_with_most_calories(elves)
    elf_id = highest_caloried_elf.ID
    calories = highest_caloried_elf._calculate_total_calories()
    message = f"Elf {elf_id} has {calories} calories"
    return message


def get_top_3_highest_calories(elves):
    elf_dict = create_elf_dictionary(elves)
    top_3_values = Counter(elf_dict).most_common(3)

    total_calorie_count = 0

    for value in top_3_values:
        total_calorie_count += value[1]

    return total_calorie_count
