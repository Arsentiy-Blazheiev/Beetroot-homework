# Task 1

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Teacher(Person):
    def __init__(self, first_name, last_name, age, experience, salary):
        super().__init__(first_name, last_name, age)
        self.experience = experience
        self.salary = salary

    def hello_teacher(self):
        print(
            f"Hello, my name is {self.last_name} {self.first_name}.\n"
            f"I am {self.age} years old.\n"
            f"My teaching experience is {self.experience} years.\n"
            f"And my salary is {self.salary} UAH."
        )


class Student(Person):
    def __init__(self, first_name, last_name, age, form_of_education, cost_of_education):
        super().__init__(first_name, last_name, age)
        self.form_of_education = form_of_education
        self.cost_of_education = cost_of_education

    def hello_student(self):
        print(
            f"Hello, my name is {self.last_name} {self.first_name}.\n"
            f"I am {self.age} years old.\n"
            f"My form of education is {self.form_of_education}.\n"
            f"And the cost of education is {self.cost_of_education} UAH."
        )


person1 = Teacher("Ivan", "Ivanov", 45, 15, 10000)
person1.hello_teacher()
person2 = Student("Maksim", "Maksimov", 20, "daytime", 20000)
person2.hello_student()


# Task 2

class Mathematician:

    def square_nums(self, my_list):
        squaring = []
        for num in my_list:
            squaring.append(num ** 2)
        print(squaring)

    def remove_positives(self, my_list2):
        positives = []
        for num in my_list2:
            if num < 0:
                positives.append(num)
        print(positives)

    def filter_leaps(self, my_yaers):
        leap_years = []
        for year in my_yaers:
            if year % 4 == 0:
                leap_years.append(year)
        print(leap_years)


my_list = [7, 11, 5, 4]
my_list2 = [26, -11, -8, 13, -90]
my_years = [2001, 1884, 1995, 2003, 2020]

m = Mathematician()

m.square_nums(my_list)
m.remove_positives(my_list2)
m.filter_leaps(my_years)

# assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
# assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
# assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]


# Task 3

class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.product_list = []
        self.income = 0
        self.info = ()

    def add(self, product, amount):
        self.product_list.append({product.name: [amount, product.type, product.price * 1.3]})
        print(self.product_list)

    def set_discount(self, identifier, percent, identifier_type='name'):
        for i in self.product_list:
            if identifier in i:
                i[identifier][2] *= (100-percent)/100
        print(self.product_list)

    def sell_product(self, product_name, sell_amount):
        for i in self.product_list:
            if product_name in i:
                if sell_amount < i[product_name][0]:
                    i[product_name][0] -= sell_amount
                    self.income += sell_amount * i[product_name][2]
                else:
                    raise ValueError("You don't have enough product to sell.")
                return
            # raise ValueError("Try again.")

    def get_income(self):
        print(self.income)
        return self.income

    def get_all_products(self):
        print(self.product_list)
        return self.product_list

    def get_product_info(self, product_name):
        for i in self.product_list:
            if product_name in i:
                self.info = (product_name, i[product_name][0])
                print(self.info)
                return self.info


p = Product("Sport", "Football T-Shirt", 100)
p2 = Product("Food", "Ramen", 1.5)
store = ProductStore()
store.add(p, 10)
store.add(p2, 300)
store.set_discount("Ramen", 50)
store.sell_product("Ramen", 10)
store.sell_product("Football T-Shirt", 5)  # Test
store.get_income()
store.get_all_products()
assert store.get_product_info("Ramen") == ("Ramen", 290)


# Task 4

class CustomException(Exception):

    def __init__(self, msg):
        self.msg = msg
        self.my_file()

    def my_file(self):
        with open("logs.txt", "a") as logs:
            logs.write(f"{self.__class__.__name__}: {self.msg}")

# try:
#     raise CustomException("Test CustomException")
# except CustomException as i:
#     print(i.msg)
