# Задание 2. Перемещение в начало (move-to-front)
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "task1_unordered_list"))
from unordered_list import UnorderedList


def move_to_front(n, read=input):
    """Читает n строк, хранит их без повторов, новая строка - в начало."""
    lst = UnorderedList()
    for _ in range(n):
        s = read()
        # если строка уже есть, убираем её
        if lst.search(s):
            lst.remove(s)
        lst.add(s)
        print(lst)
    return lst


if __name__ == "__main__":
    n = int(input("Сколько строк: "))
    move_to_front(n, lambda: input("Строка: "))
