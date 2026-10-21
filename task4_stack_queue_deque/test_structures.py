import unittest

from structures import Deque, Queue, Stack


class TestStack(unittest.TestCase):
    def test_empty(self):
        s = Stack()
        self.assertTrue(s.isEmpty())
        self.assertEqual(s.size(), 0)
        with self.assertRaises(IndexError):
            s.pop()
        with self.assertRaises(IndexError):
            s.peek()

    def test_lifo(self):
        s = Stack()
        for x in [1, 2, 3]:
            s.push(x)
        self.assertEqual(s.size(), 3)
        self.assertEqual(s.peek(), 3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertTrue(s.isEmpty())


class TestQueue(unittest.TestCase):
    def test_empty(self):
        q = Queue()
        self.assertTrue(q.isEmpty())
        self.assertEqual(q.size(), 0)
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_fifo(self):
        q = Queue()
        for x in [1, 2, 3]:
            q.enqueue(x)
        self.assertEqual(q.size(), 3)
        self.assertEqual(q.dequeue(), 1)
        q.enqueue(4)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 4)
        self.assertTrue(q.isEmpty())


class TestDeque(unittest.TestCase):
    def test_empty(self):
        d = Deque()
        self.assertTrue(d.isEmpty())
        self.assertEqual(d.size(), 0)
        with self.assertRaises(IndexError):
            d.removeFront()
        with self.assertRaises(IndexError):
            d.removeRear()

    def test_both_ends(self):
        d = Deque()
        d.addRear(2)
        d.addFront(1)
        d.addRear(3)
        self.assertEqual(d.size(), 3)
        self.assertEqual(d.removeFront(), 1)
        self.assertEqual(d.removeRear(), 3)
        self.assertEqual(d.removeRear(), 2)
        self.assertTrue(d.isEmpty())

    def test_like_stack(self):
        # с одного конца дек работает как стек
        d = Deque()
        d.addFront("a")
        d.addFront("b")
        self.assertEqual(d.removeFront(), "b")
        self.assertEqual(d.removeFront(), "a")


if __name__ == "__main__":
    unittest.main(verbosity=2)
