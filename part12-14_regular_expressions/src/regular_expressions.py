# Write your solution here

import re

# part 1
def is_dotw(my_string: str):
    
    while True:
        if my_string == '':
            break
        if re.search('Mon|Tue|Wed|Thu|Fri|Sat|Sun', my_string):
            return True
        else:
            return False

# part 2
def all_vowels(my_string: str):
    
    while True:
        if my_string == '':
            break

        checks = []

        for character in my_string:
            if re.search('[aeiou]', character):
                checks.append(True)
            else:
                checks.append(False)

        if False in checks:
            return False
        else:
            return True

# part 3
def time_of_day(my_string: str):

    regex = '^([0-1][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$'
    
    while True:
        if my_string == '':
            break
        if re.search(regex, my_string):
            return True
        else:
            return False

if __name__ == '__main__':

    print('\n--- Part 01 ---\n')
    print(is_dotw("Mon"))
    print(is_dotw("Fri"))
    print(is_dotw("Tui"))

    print('\n--- Part 02 ---\n')
    print(all_vowels("eioueioieoieou"))
    print(all_vowels("autoooo"))

    print('\n--- Part 03 ---\n')
    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))

    print('\n--- TMC Tests ---\n')
    print(time_of_day("23:15:xx"))
    print(time_of_day("25:13:01"))
    print(time_of_day("20:10:30"))
    print()