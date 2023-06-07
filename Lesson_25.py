# Task 1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def append(self, item):
        current = self.head
        new_node = Node(item)

        if current is None:
            self.head = new_node
        else:
            while current.next is not None:
                current = current.next
            current.next = new_node

    def index(self, item):
        current = self.head
        index = 0
        found = False

        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
                index += 1

        if found:
            return index
        else:
            raise ValueError(f"{item} is not in the list")

    def pop(self, pos=None):
        if self.is_empty():
            raise IndexError("pop from empty list")

        if pos is None:
            pos = self.size() - 1

        current = self.head
        previous = None
        index = 0

        while index < pos:
            previous = current
            current = current.next
            index += 1

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

        return current.data

    def insert(self, pos, item):
        if pos == 0:
            self.add(item)
        else:
            current = self.head
            previous = None
            index = 0

            while index < pos:
                previous = current
                current = current.next
                index += 1

            new_node = Node(item)
            previous.next = new_node
            new_node.next = current

    def slice(self, start, stop):
        if start >= stop:
            return UnorderedList()

        current = self.head
        index = 0

        while index < start:
            if current is None:
                raise IndexError("list index out of range")
            current = current.next
            index += 1

        sliced_list = UnorderedList()
        while index < stop:
            if current is None:
                raise IndexError("list index out of range")
            sliced_list.append(current.data)
            current = current.next
            index += 1

        return sliced_list

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count


my_list = UnorderedList()
my_list.add(1)
my_list.add(2)
my_list.append(3)
print(my_list.size())  # виведе: 3

print(my_list.index(2))  # виведе: 1

item = my_list.pop()
print(item)  # виведе: 3

my_list.insert(1, 4)
print(my_list.size())  # виведе: 3
print(my_list.pop(1))  # виведе: 4

sliced_list = my_list.slice(0, 2)
print(sliced_list.size())  # виведе: 1


# Task 2


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")

        popped_item = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped_item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")

        return self.top.data

    def get_size(self):
        return self.size


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())  # виведе: 3

item = stack.pop()
print(item)  # виведе: 3

print(stack.get_size())  # виведе: 2


# Task 3


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")

        dequeued_item = self.head.data
        self.head = self.head.next
        self.size -= 1

        if self.is_empty():
            self.tail = None

        return dequeued_item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")

        return self.head.data

    def get_size(self):
        return self.size


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.peek())  # виведе: 1

item = queue.dequeue()
print(item)  # виведе: 1

print(queue.get_size())  # виведе: 2
