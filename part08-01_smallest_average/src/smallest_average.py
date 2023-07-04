from math import inf

def smallest_average(*people: dict):

    smallest = people[0]
    smallest_sum = 0
    smallest_quantity = 0

    for value in smallest.values():
        if type(value) == int:
            smallest_sum += value
            smallest_quantity += 1
    smallest_average = smallest_sum / smallest_quantity

    for i in people:       
        person_sum = 0
        
        for value in i.values():
            if type(value) == int:
                person_sum += value
    
        person_average = person_sum / 3
        if person_average < smallest_average:
            smallest = i
            smallest_average = person_average

    return smallest

if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    person1 = {"name": "Anna", "result1": 1,"result2": 1,"result3": 1}
    person2 = {"name": "Anna", "result1": 2,"result2": 2,"result3": 2}
    person3 = {"name": "Anna", "result1": 3,"result2": 3,"result3": 3}

    person1 = {"name": "Anna", "result1": 9,"result2": 9,"result3": 9}
    person2 = {"name": "Anna", "result1": 7,"result2": 7,"result3": 7}
    person3 = {"name": "Anna", "result1": 8,"result2": 8,"result3": 8}

    print(smallest_average(person1, person2, person3))
