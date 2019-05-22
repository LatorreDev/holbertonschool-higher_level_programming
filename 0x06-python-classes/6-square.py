#!/usr/bin/python3
class Square:

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print('#' * self.__size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif self.__position[0] < 0 or self.__position[1] < 0:
            raise IndexError("Out of Range")
        elif (type(self.__position[0]) is not int or
              type(self.__position[1] is not int)):
            raise TypeError("Must be an integer")
        else:
            self.__position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
