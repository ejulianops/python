# DO NOT CHANGE CLASS Book!
# Write your solution after the class!

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year

# -----------------------------
# Write your solution here
# -----------------------------

def older_book(book1: Book, book2: Book):

    older = []

    if book1.year < book2.year:
        older.append(book1)
    elif book2.year < book1.year:
        older.append(book2)
    else:
        older.append(book1)
        older.append(book2)


    if len(older) == 1:
        print(f"{older[0].name} is older, it was published in {older[0].year}")
    else:
        print(f"{older[0].name} and {older[1].name} were published in {older[1].year}")
        
if __name__ == "__main__":
    python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
    norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

    older_book(python, everest)
    older_book(python, norma)