# Write your solution here
def even_numbers(beginning: int, maximum: int):
    number = beginning

    while number <= maximum:
        if number % 2 == 0:
            yield number
            number += 1
        else:
            number += 1 

if __name__ == "__main__":
    print('example 1:')
    numbers = even_numbers(2, 10)
    for number in numbers:
        print(number)

    print('example 2:')
    numbers = even_numbers(11, 21)
    for number in numbers:
        print(number)