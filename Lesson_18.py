# Task 1

import re


class Validator:
    def __init__(self, email):
        self.email = email
        self.validate()

    def validate(self):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$'
        if not re.match(email_regex, self.email):
            raise ValueError("Не вірний формат")


email_1 = Validator("qwerty@qwerty.com")
email_2 = Validator("qwerty.com")


# Task 2


class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_

        self.name = name

        self.company = company

        self.workers = []

    def __str__(self):
        return f'id_: {self.id}, name: {self.name}, company: {self.company}'

    def add_workers(self, worker):
        if isinstance(worker, Worker):
            self.workers.append({worker.name: {"id": worker.id, "company": worker.company}})

    def get_workers(self):
        return self.workers


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss

    @property
    def get_boss(self):
        return self.boss

    @get_boss.setter
    def get_boss(self, new_boss):
        if not isinstance(new_boss, Boss):
            raise ValueError("Не клас Boss")
        self.boss = new_boss

    def __str__(self):
        return f"id_: {self.id}, name: {self.name}, company: {self.company}, boss: {self.boss}"


boss1 = Boss(1, "Ivan", "MyCompany")
boss2 = Boss(2, "Petro", "NewCompany")

worker1 = Worker(1, "Jeck", "MyCompany", boss1)
worker2 = Worker(1, "John", "MyCompany", boss1)

print(worker1.get_boss)

worker1.get_boss = boss2
print(worker1.get_boss)

boss1.add_workers(worker1)
print(boss1.workers)

# Task 3


from functools import wraps


class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            my_func = func(*args, **kwargs)
            try:
                return int(my_func)
            except ValueError:
                return my_func
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            my_func = func(*args, **kwargs)
            try:
                return str(my_func)
            except ValueError:
                return my_func
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            my_func = func(*args, **kwargs)
            try:
                return float(my_func)
            except ValueError:
                return my_func
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            my_func = func(*args, **kwargs)
            return bool(my_func)
        return wrapper


@TypeDecorators.to_float
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25
assert do_something('True') is True
