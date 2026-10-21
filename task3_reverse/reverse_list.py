# Задание 3. Разворот односвязного списка
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "task1_unordered_list"))
from unordered_list import Node


def reverse_iter(head):
    """Итеративный разворот. Возвращает новый первый узел."""
    previous = None
    current = head
    while current is not None:
        nxt = current.getNext()
        current.setNext(previous)
        previous = current
        current = nxt
    return previous


def reverse_rec(head):
    """Рекурсивный разворот. Возвращает новый первый узел."""
    if head is None or head.getNext() is None:
        return head
    new_head = reverse_rec(head.getNext())
    # следующий узел теперь указывает на текущий
    head.getNext().setNext(head)
    head.setNext(None)
    return new_head


def from_list(items):
    # строит цепочку узлов из списка Python
    head = None
    for x in reversed(items):
        node = Node(x)
        node.setNext(head)
        head = node
    return head


def to_list(head):
    # переводит цепочку узлов в список Python
    items = []
    while head is not None:
        items.append(head.getData())
        head = head.getNext()
    return items


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print("Исходный:", data)
    print("Итеративно:", to_list(reverse_iter(from_list(data))))
    print("Рекурсивно:", to_list(reverse_rec(from_list(data))))
