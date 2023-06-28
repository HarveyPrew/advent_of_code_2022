
def rucksack_splitter(rucksack):
    half_len = len(rucksack) // 2
    first_compartment = rucksack[:half_len]
    second_compartment = rucksack[half_len:]
    return first_compartment, second_compartment
