#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand="Adidas", size=9, cobble =""):
        self.brand = brand
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self.__size = value
            self.condition = "New"

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
        


           