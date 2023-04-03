# Task 1

a = 1
b = (1, 2, 3)
c = "qwert"
def count_lv():
    x = 1
    y = (1, 2, 3)
    z = "qwerty"
    w = [1, 2, 3]
    print("qwerty")

print(count_lv.__code__.co_nlocals)

# Task 2

def year_taxes(year_salary, taxes):
    def year_salary(salary):
        return salary * 12 * taxes
    return year_salary
my_func = year_taxes(10000, 0.2)
print(my_func(10000))

# Task 3

def choose_func(nums: list, func1, func2):
    numbers = 0
    for num in nums:
        if num >= 0: numbers += 1
    if numbers == len(nums):
        return func1(nums)
    else:
        return func2(nums)


# Assertions
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]

print(choose_func(nums1, square_nums, remove_negatives))
print(choose_func(nums2, square_nums, remove_negatives))