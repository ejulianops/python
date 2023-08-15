# WRITE YOUR SOLUTION HERE:

# Please write a function named lengths(lists: list) which takes a list containing lists of integers as its argument. 
# The function should return a new list, containing the lengths of the lists within the argument list.

# The function should use a list comprehension to achieve this. 
# The maximum length of the function is two lines of code, including the header line beginning with the def keyword.

def lengths(lists: list):
    return [len(list) for list in lists]

if __name__ == "__main__":
    lists = [[1,2,3,4,5], [324, -1, 31, 7],[]]
    print(lengths(lists))