# Задание 4. Стек, очередь и дек на основе связного списка
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "task1_unordered_list"))
from unordered_list import UnorderedList


class Stack:
    """Стек: вершина - начало списка."""

    def __init__(self):
        self.items = UnorderedList()

    def isEmpty(self):
        return self.items.isEmpty()

    def push(self, item):
        self.items.add(item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        if self.items.isEmpty():
            raise IndexError("стек пуст")
        return self.items.head.getData()

    def size(self):
        return self.items.size()


class Queue:
    """Очередь: вставка в начало списка, выход с конца (как в лекции)."""

    def __init__(self):
        self.items = UnorderedList()

    def isEmpty(self):
        return self.items.isEmpty()

    def enqueue(self, item):
        self.items.add(item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return self.items.size()


class Deque:
    """Дек: начало дека - начало списка."""

    def __init__(self):
        self.items = UnorderedList()

    def isEmpty(self):
        return self.items.isEmpty()

    def addFront(self, item):
        self.items.add(item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def size(self):
        return self.items.size()


if __name__ == "__main__":
    s = Stack()
    for x in [1, 2, 3]:
        s.push(x)
    print("Стек: peek =", s.peek(), "pop =", s.pop(), "size =", s.size())

    q = Queue()
    for x in [1, 2, 3]:
        q.enqueue(x)
    print("Очередь: dequeue =", q.dequeue(), "size =", q.size())

    d = Deque()
    d.addFront(2)
    d.addFront(1)
    d.addRear(3)
    print("Дек:", d.items, "removeFront =", d.removeFront(),
          "removeRear =", d.removeRear())
