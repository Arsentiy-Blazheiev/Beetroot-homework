# Task 1


class Stack:
    def __init__(self):
        self.my_stack = []

    def push(self, value):
        self.my_stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.my_stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.my_stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.my_stack) == 0

    def size(self):
        return len(self.my_stack)


my_stack = Stack()


for item in [1, 2, 3, 4, 5]:
    my_stack.push(item)

while not my_stack.is_empty():
    print(my_stack.pop())

# Task 2


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def top(self):
        return self.items[-1]

    def is_balanced(self):
        stack = Stack()
        opening_brackets = '({['
        closing_brackets = ')}]'
        for char in self.items:
            if char in opening_brackets:
                stack.push(char)
            elif char in closing_brackets:
                if stack.is_empty():
                    return False
                if closing_brackets.index(char) != opening_brackets.index(stack.top()):
                    return False
                stack.pop()
        return stack.is_empty()


a = Stack()
a.push('(')
a.push(')')
a.push('1')
a.push('1')
a.push('1')
print(a.is_balanced())

# Task 3


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def get_from_stack(self, e):
        if e in self.items:
            self.items.reverse()
            index = self.items.index(e)
            self.items.reverse()
            return self.items.pop(len(self.items)-1-index)
        else:
            raise ValueError(f"{e} not found in stack")


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.get_from_stack(2))  # виведе 2
print(stack.get_from_stack(4))  # ValueError з повідомленням "4 not found in stack"

from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not bool(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

    def get_from_queue(self, e):
        try:
            self.items.remove(e)
            return e
        except ValueError:
            raise ValueError(f"Element {e} not found in queue")


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.get_from_queue(2))  # поверне 2
print(q.get_from_queue(5))  # ValueError з повідомленням "Element 5 not found in queue"
print(q.items)  # [1, 3, 4] в тому ж порядку
