# Write your solution here!

import statistics

class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.storage = []

    def add_number(self, number:int):        
        self.storage.append(number)

    def count_numbers(self):
        return len(self.storage)

    def get_sum(self):
        if len(self.storage) > 0: 
            return sum(self.storage)
        else:
            return 0

    def average(self):
        if len(self.storage) > 0: 
            return statistics.mean(self.storage)
        else:
            return 0

all_numbers = NumberStats()
even_numbers = NumberStats()
odd_numbers = NumberStats()

while True:

    user_input = int(input('Type an integer. Or -1 to exit: '))

    if user_input == -1:
        break
    
    elif user_input % 2 == 0:
        even_numbers.add_number(user_input)

    elif user_input % 2 != 0:
        odd_numbers.add_number(user_input)

    all_numbers.add_number(user_input)
    
print('Sum of numbers:', all_numbers.get_sum())
print('Mean of numbers:', float(all_numbers.average()))
print('Sum of even numbers:', even_numbers.get_sum())
print('Sum of odd numbers:', odd_numbers.get_sum())
