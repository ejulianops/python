class Recording:
    def __init__(self, length: int):
        if length > 0:
            self.__length = length
        else:
            raise ValueError("Length must be bigger than zero")

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: int):
        if length > 0:
            self.__length = length
        else:
            raise ValueError("Length must be bigger than zero")

if __name__ == "__main__":
    the_wall = Recording(43)
    print(the_wall.length)
    the_wall.length = 44
    print(the_wall.length)
    negative_value_test = Recording(-1)
    print(negative_value_test.length)