import math
import string

def change_case(orig_string: str):
    print()

    new_string = ''

    for character in orig_string:
        if character.isupper():
            new_string += character.lower()
        elif character.islower():
            new_string += character.upper()
        else:
            new_string += character

    return new_string

def split_in_half(orig_string: str):

    string_halves = []

    split_here = (len(orig_string) / 2) - 1
    split_here = math.floor(split_here)

    first_half = ''
    second_half = ''

    for character in orig_string:
        
        if split_here >= 0:
            first_half += character
            split_here -= 1
        else:
            second_half += character
            split_here
    string_halves.append(first_half)
    string_halves.append(second_half)

    return tuple(string_halves)

def remove_special_characters(orig_string: str):

    new_string = ''

    for character in orig_string:
        if character in string.punctuation:
            pass
        elif character not in string.printable:
            pass
        else:
            new_string += character
            
    return new_string

if __name__ == "__main__": 
    change_case("Well hello there!")
    split_in_half("Well hello there!")
    remove_special_characters("This is a test, lets see how it goes!!!11!")
    remove_special_characters("Thi§ is a test test")