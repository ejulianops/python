import random

def lottery_numbers(amount: int, lower: int, upper: int):

    numbers = []

    while len(numbers) < amount:
        random_number = random.randint(lower, upper)
        if random_number not in numbers:
            numbers.append(random_number)

    numbers.sort()
    return numbers