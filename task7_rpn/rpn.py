# Задание 7. Калькулятор обратной польской записи
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "task4_stack_queue_deque"))
from structures import Stack

ERROR = "выражение составлено некорректно"


def do_math(op, a, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    return a / b  # ZeroDivisionError ловим выше


def to_number(token):
    # число или None
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return None


def evaluate(expr):
    """Возвращает результат или строку с ошибкой."""
    stack = Stack()
    for token in expr.split():
        if token in "+-*/" and len(token) == 1:
            if stack.size() < 2:
                return ERROR  # не хватает операндов
            b = stack.pop()
            a = stack.pop()
            try:
                stack.push(do_math(token, a, b))
            except ZeroDivisionError:
                return ERROR
        else:
            num = to_number(token)
            if num is None:
                return ERROR  # неизвестный символ
            stack.push(num)
    if stack.size() != 1:
        return ERROR  # пусто или лишние числа
    result = stack.pop()
    # 4.0 -> 4
    if isinstance(result, float) and result.is_integer():
        result = int(result)
    return result


if __name__ == "__main__":
    expr = input("Выражение: ")
    print("Результат:", evaluate(expr))
