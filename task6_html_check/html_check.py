# Задание 6. Проверка парности тегов HTML с помощью стека
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "task4_stack_queue_deque"))
from structures import Stack

# одиночные теги, их не закрывают
VOID_TAGS = {"br", "img", "meta", "input", "hr", "link"}

# тег: <имя ...> или </имя>
TAG_RE = re.compile(r"<\s*(/?)\s*([a-zA-Z][a-zA-Z0-9]*)[^>]*?(/?)\s*>")
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)


def check_html(text):
    """True, если все теги закрыты в правильном порядке."""
    text = COMMENT_RE.sub("", text)
    stack = Stack()
    for m in TAG_RE.finditer(text):
        closing, self_closing = m.group(1), m.group(3)
        name = m.group(2).lower()
        if name in VOID_TAGS or self_closing:
            continue
        if not closing:
            stack.push(name)
        else:
            # закрывающий тег должен совпасть с вершиной стека
            if stack.isEmpty() or stack.pop() != name:
                return False
    return stack.isEmpty()


def check_file(path):
    with open(path, encoding="utf-8") as f:
        return check_html(f.read())


if __name__ == "__main__":
    folder = os.path.dirname(os.path.abspath(__file__))
    files = sys.argv[1:] or [os.path.join(folder, "example.html"),
                             os.path.join(folder, "bad_example.html")]
    for path in files:
        ok = check_file(path)
        msg = "теги парные" if ok else "ошибка в тегах"
        print(os.path.basename(path), "-", msg)
