# Please write a function named square_roots(numbers: list) which takes a list of integers as its argument. 
# The function should return a new list containing the square roots of the original integers.

import math

def square_roots(numbers: list):
    return [math.sqrt(number) for number in numbers]

if __name__ == "__main__":
    lines = square_roots([1,2,3,4])
    for line in lines:
        print(line)