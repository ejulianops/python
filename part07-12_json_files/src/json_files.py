import json

def print_persons(filename: str):

    with open(filename) as my_file:
        data = my_file.read()

    people = json.loads(data)

    for person in people:

        hobbies_list = ''
        for hobby in person['hobbies']:
            hobbies_list += f"{hobby}, "
        hobbies_list = hobbies_list[:-2]

        print(f"{person['name']} {person['age']} years ({hobbies_list})")

