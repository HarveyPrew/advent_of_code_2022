class Elf:
    def __init__(self, ID, calories):
        self.ID = ID
        self. calories = calories


def elfList():
    elf_1 = Elf(1, [1000, 2000, 3000])
    elf_2 = Elf(2, [4000])
    elf_3 = Elf(3, [5000, 6000])
    elf_4 = Elf(4, [7000, 8000, 9000])
    elf_5 = Elf(5, [10000])

    list_of_elves = [elf_1, elf_2, elf_3, elf_4, elf_5]

    return list_of_elves
