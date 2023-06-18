from advent_of_code_2022.elf import Elf


def get_file(path):
    return open(path, "r")


def get_calorie_list(path):
    calories = []
    file = get_file(path)

    for line in file:

        if line == "\n":
            break

        calories.append(int(line))

    return calories


def create_elves():
    elves = [
        Elf(1, [1000, 2000, 3000]),
        Elf(2, [4000]),
        Elf(3, [5000, 6000]),
        Elf(4, [7000, 8000, 9000]),
        Elf(5, [10000])
    ]
    return elves


def find_elf_with_most_calories(elves):
    return max(elves, key=lambda elf: elf._calculate_total_calories())


def get_highest_caloried_elf_info():
    elves = create_elves()
    highest_caloried_elf = find_elf_with_most_calories(elves)
    elf_id = highest_caloried_elf.ID
    calories = highest_caloried_elf._calculate_total_calories()
    message = f"Elf {elf_id} has {calories} calories"
    return message
