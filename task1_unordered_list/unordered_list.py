# Задание 1. Неупорядоченный связный список


class Node:
    """Узел списка: данные и ссылка на следующий узел."""

    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, new_data):
        self.data = new_data

    def setNext(self, new_next):
        self.next = new_next


class UnorderedList:
    """Неупорядоченный односвязный список."""

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        # вставка в начало
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.getData() == item:
                return True
            current = current.getNext()
        return False

    def remove(self, item):
        current = self.head
        previous = None
        while current is not None and current.getData() != item:
            previous = current
            current = current.getNext()
        if current is None:
            raise ValueError("элемента нет в списке")
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        # вставка в конец
        temp = Node(item)
        if self.head is None:
            self.head = temp
            return
        current = self.head
        while current.getNext() is not None:
            current = current.getNext()
        current.setNext(temp)

    def index(self, item):
        current = self.head
        pos = 0
        while current is not None:
            if current.getData() == item:
                return pos
            current = current.getNext()
            pos += 1
        raise ValueError("элемента нет в списке")

    def insert(self, pos, item):
        if pos == 0:
            self.add(item)
            return
        # ищем узел перед позицией pos
        previous = self.head
        for _ in range(pos - 1):
            previous = previous.getNext()
        temp = Node(item)
        temp.setNext(previous.getNext())
        previous.setNext(temp)

    def pop(self, pos=None):
        if self.head is None:
            raise IndexError("pop из пустого списка")
        if pos is None:
            pos = self.size() - 1
        current = self.head
        previous = None
        for _ in range(pos):
            previous = current
            current = current.getNext()
            if current is None:
                raise IndexError("неверная позиция")
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        return current.getData()

    def __str__(self):
        items = []
        current = self.head
        while current is not None:
            items.append(repr(current.getData()))
            current = current.getNext()
        return "[" + ", ".join(items) + "]"

    def slice(self, start, stop):
        # копия элементов с start до stop (stop не входит)
        result = UnorderedList()
        tail = None
        current = self.head
        pos = 0
        while current is not None and pos < stop:
            if pos >= start:
                temp = Node(current.getData())
                if tail is None:
                    result.head = temp
                else:
                    tail.setNext(temp)
                tail = temp
            current = current.getNext()
            pos += 1
        return result


if __name__ == "__main__":
    lst = UnorderedList()
    for x in [1, 2, 3]:
        lst.append(x)
    print("append 1, 2, 3:", lst)
    lst.insert(1, 10)
    print("insert(1, 10):", lst)
    print("index(3):", lst.index(3))
    print("pop():", lst.pop(), "->", lst)
    print("pop(0):", lst.pop(0), "->", lst)
    lst.append(4)
    lst.append(5)
    print("append 4, 5:", lst)
    print("slice(1, 3):", lst.slice(1, 3))
    print("size:", lst.size())
