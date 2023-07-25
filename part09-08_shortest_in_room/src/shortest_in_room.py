# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"There are {len(self.persons)} in the room, and their combined height is x cm"

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        if len(self.persons) == 0:
            return True
        else:
            return False    

    def print_contents(self):
        combined_height = 0
        for person in self.persons:
            combined_height += person.height
        print(f"There are {len(self.persons)} persons in the room, and their combined height is {combined_height} cm")
        for person in self.persons:
            print(f"{person} ({person.height} cm)")

    def shortest(self):
        shortest_person = None
        if len(self.persons) == 0:
            return shortest_person
        else:
            shortest_person = self.persons[0]
            for person in self.persons:
                if person.height < shortest_person.height:
                    shortest_person = person
            return shortest_person

    def remove_shortest(self):
        shortest_person = self.shortest()
        if shortest_person != None:
            self.persons.remove(shortest_person)
        return shortest_person 

if __name__ == "__main__":

    print("\n--- Part 1 ---\n")
    room = Room()
    print("Is the room empty?", room.is_empty())
    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Ally", 166))
    room.add(Person("Nina", 162))
    room.add(Person("Dorothy", 155))
    print("Is the room empty?", room.is_empty())
    room.print_contents()

    print("\n--- Part 2 ---\n")
    room = Room()
    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())
    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    print()
    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())
    print()
    room.print_contents()

    print("\n--- Part 3 ---\n")
    room = Room()
    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()
    print()
    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")
    print()
    room.print_contents()