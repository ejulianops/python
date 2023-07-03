import random
import string

def generate_password(length: int):

    password = ''
    
    for character in range(length):
        index = random.randint(1, len(string.ascii_lowercase)-1)
        password += string.ascii_lowercase[index]

    return password

if __name__ == "__main__":
    generate_password(8)
    generate_password(2)