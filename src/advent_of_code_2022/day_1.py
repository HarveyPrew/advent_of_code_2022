from advent_of_code_2022.elf import Elf


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


def get_highest_caloried_elf_info(elves):
    highest_caloried_elf = find_elf_with_most_calories(elves)
    elf_id = highest_caloried_elf.ID
    calories = highest_caloried_elf._calculate_total_calories()
    message = f"Elf {elf_id} has {calories} calories"
    return message
