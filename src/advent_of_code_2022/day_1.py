from advent_of_code_2022.elf import Elf


def elfList():
    elves = [
        Elf(1, [1000, 2000, 3000]),
        Elf(2, [4000]),
        Elf(3, [5000, 6000]),
        Elf(4, [7000, 8000, 9000]),
        Elf(5, [10000])
    ]
    return elves


def elfWithMostCalories():
    list_of_elves = elfList()

    # The elf with the highest calculate total calories is selected.
    highest_caloried_elf = max(list_of_elves,
                               key=lambda elf: elf._calculate_total_calories())

    return highest_caloried_elf


def highestCaloriedElfInfo():
    highest_caloried_elf = elfWithMostCalories()
    elf_id = highest_caloried_elf.ID
    calories = highest_caloried_elf._calculate_total_calories()
    message = f"Elf {elf_id} has {calories} calories"
    return message
