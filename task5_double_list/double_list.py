# Задание 5. Двухсвязный список


class DNode:
    """Узел: данные, ссылки на предыдущий и следующий узлы."""

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self, item):
        # возвращает узел с item или None
        current = self.head
        while current is not None:
            if current.data == item:
                return current
            current = current.next
        return None

    def addFront(self, item):
        node = DNode(item)
        node.next = self.head
        if self.head is None:
            self.tail = node
        else:
            self.head.prev = node
        self.head = node

    def addRear(self, item):
        node = DNode(item)
        node.prev = self.tail
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def removeFront(self):
        if self.head is None:
            raise IndexError("список пуст")
        node = self.head
        self.removeNode(node)
        return node.data

    def removeRear(self):
        if self.tail is None:
            raise IndexError("список пуст")
        node = self.tail
        self.removeNode(node)
        return node.data

    def insertBefore(self, node, item):
        if node is self.head:
            self.addFront(item)
            return
        new = DNode(item)
        new.prev = node.prev
        new.next = node
        node.prev.next = new
        node.prev = new

    def insertAfter(self, node, item):
        if node is self.tail:
            self.addRear(item)
            return
        new = DNode(item)
        new.prev = node
        new.next = node.next
        node.next.prev = new
        node.next = new

    def removeNode(self, node):
        # перекидываем ссылки соседей
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next
        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        node.prev = node.next = None

    def __str__(self):
        items = []
        current = self.head
        while current is not None:
            items.append(repr(current.data))
            current = current.next
        return "[" + ", ".join(items) + "]"

    def backward(self):
        # элементы с конца, для проверки ссылок prev
        items = []
        current = self.tail
        while current is not None:
            items.append(current.data)
            current = current.prev
        return items


if __name__ == "__main__":
    d = DoubleList()
    d.addRear(2)
    d.addRear(4)
    d.addFront(1)
    print("addFront/addRear:", d)
    node = d.search(4)
    d.insertBefore(node, 3)
    d.insertAfter(node, 5)
    print("insertBefore(4, 3), insertAfter(4, 5):", d)
    d.removeNode(d.search(3))
    print("removeNode(3):", d)
    print("removeFront:", d.removeFront(), "removeRear:", d.removeRear(),
          "->", d)
    print("size:", d.size(), "обратно:", d.backward())
