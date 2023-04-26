# Task 1

class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError


class Cat(Animal):
    def talk(self):
        print("Meow-meow")


class Dog(Animal):
    def talk(self):
        print("Gav-Gav")


my_animals = [Cat("Murka"), Dog("Tobby"), Cat("Pushok"), Dog("Lessy")]
for animal in my_animals:
    animal.talk()

# Task 2


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __str__(self):
        return f"{self.name}, {self.country}, {self.birthday}"

    def __repr__(self):
        return f"Author ({self.name}, {self.country}, {self.birthday})"


class Book:
    counter_books = 0

    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        return f"{self.name}, {self.year}, {self.author}"

    def __repr__(self):
        return f"Book ({self.name}, {self.year}, {self.author})"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: Author):
        book = Book(name, year, author)
        self.books.append(book)
        self.authors.append(book)
        Book.counter_books += 1
        return book

    def group_by_author(self, author: Author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year: int):
        return [book for book in self.books if book.year == year]

    def __str__(self):
        return f"Library: {self.name}"

    def __repr__(self):
        return f"Library: {self.name}"


library = Library("test")
author1 = Author("Pupkin", "USA", 1234)
author2 = Author("Petrov", "USSR", 1990)
author3 = Author("Ivanov", "SSSR", 1990)
library.new_book("Your life", 1991, "Petrov")
library.new_book("Your life2", 1991, "Ivanov")
library.new_book("Your life3", 1992, "Ivanov")
library.new_book("My life", 4321, "Pupkin")
print(library.group_by_author("Ivanov"))
print(library.group_by_year(1991))
print(library.new_book("My life", 4321, "Pupkin"))
print(Book.counter_books)
print(repr(library))
print(repr(author2))
print(str(author3))

# Task 3


class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, number):
        numerator = (self.numerator * number.denominator) + (self.denominator * number.numerator)
        denominator = self.denominator * number.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, number):
        numerator = (self.numerator * number.denominator) - (self.denominator * number.numerator)
        denominator = self.denominator * number.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, number):
        numerator = self.numerator * number.numerator
        denominator = self.denominator * number.denominator
        return Fraction(numerator, denominator)

    def __truediv__(self, number):
        numerator = self.numerator * number.denominator
        denominator = self.denominator * number.numerator
        return Fraction(numerator, denominator)

    def __eq__(self, number):
        return self.numerator * number.denominator == number.numerator * self.denominator

    def __lt__(self, number):
        return self.numerator * number.denominator < number.numerator * self.denominator

    def __gt__(self, number):
        return self.numerator * number.denominator > number.numerator * self.denominator


number_1 = Fraction(5, 10)
number_2 = Fraction(5, 20)
print(number_1 + number_2)
print(number_1 - number_2)
print(number_1 * number_2)
print(number_1 / number_2)
print(number_1 == number_2)
print(number_1 < number_2)
print(number_1 > number_2)