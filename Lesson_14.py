# Task 1

from functools import wraps
def logger(func):
    @wraps(func)
    def wrapper(*args):
        print(f"{func} called with {args}")
    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

add(4, 5)
square_all(2, 4, 5, 10)


# Task 2

from functools import wraps
def stop_words(words: list):
    def wrapper(func):
        @wraps(func)
        def inner(name):
            massage = func(name)
            for word in words:
                massage = massage.replace(word, "*")
            return massage
        return inner
    return wrapper

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

# assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
print(create_slogan("Steve"))


# Task 3

def arg_rules(type_: type, max_length: int, contains: list):
    def decor(func):
        def res(name):
            error_list = []
            if len(str(name)) > max_length:
                error_list.append(f"{name} is longer then {max_length}")
            if type(name) != type_:
                error_list.append(f"Type {name} is not {type_}")
            result = 0
            for i in contains:
                if i in str(name):
                    result += 1
            if result != len(contains):
                error_list.append(f"{name} is not in {contains}")
            if error_list:
                print(*error_list, sep="\n")
                return False
            return func(name)
        return res
    return decor

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

print(create_slogan('johndoe'))
print(create_slogan('SSdhdththhfdhtttH05'))
print(create_slogan(2365463735674567))
print(create_slogan("1414@1405"))
