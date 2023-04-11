# Task 1

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.first_name} {self.last_name} and I’m {self.age} years old!")

arsen = Person("Arsentiy", "Blazheiev", 31)
arsen.talk()


# Task 2

class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        print(self.age * self.age_factor)

my_dog = Dog(14)
my_dog.human_age()


# Task 3

CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    ind = 0
    def __init__(self, chennel):
        self.chennel = chennel
    def first_channel(self):
        print(self.chennel[0])
        TVController.ind = 1
    def last_channel(self):
        print(self.chennel[-1])
        TVController.ind = 3
    def turn_channel(self, n):
        print(self.chennel[n-1])
        TVController.ind = n
    def next_channel(self):
        if TVController.ind != len(self.chennel):
            print(self.chennel[TVController.ind])
            TVController.ind += 1
        else:
            print(self.chennel[0])
            TVController.ind = 0
    def previous_channel(self):
        if TVController.ind != 0:
            print(self.chennel[TVController.ind-2])
            TVController.ind -= 1
        else:
            print(self.chennel[-1])
            TVController.ind = len(self.chennel-1)
    def current_channel(self):
        print(self.chennel[TVController.ind-1])
    def is_exist(self, x):
        if x in self.chennel or x < len(self.chennel)+1:
            print("Yes")
        else:
            print("No")

a = TVController(CHANNELS)
a.first_channel()
a.last_channel()
a.turn_channel(1)
a.next_channel()
a.previous_channel()
a.current_channel()
a.is_exist(4)
a.is_exist("BBC")
