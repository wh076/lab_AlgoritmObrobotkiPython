import unittest

from double_list import DoubleList


def make(items):
    d = DoubleList()
    for x in items:
        d.addRear(x)
    return d


class TestDoubleList(unittest.TestCase):
    def check(self, d, items):
        # проверяем ссылки в обе стороны
        self.assertEqual(str(d), str(items))
        self.assertEqual(d.backward(), items[::-1])

    def test_empty(self):
        d = DoubleList()
        self.assertTrue(d.isEmpty())
        self.assertEqual(d.size(), 0)
        self.assertIsNone(d.search(1))
        with self.assertRaises(IndexError):
            d.removeFront()
        with self.assertRaises(IndexError):
            d.removeRear()

    def test_add_front_rear(self):
        d = DoubleList()
        d.addFront(2)
        d.addFront(1)
        d.addRear(3)
        self.check(d, [1, 2, 3])
        self.assertEqual(d.size(), 3)
        self.assertFalse(d.isEmpty())

    def test_search(self):
        d = make([1, 2, 3])
        self.assertEqual(d.search(2).data, 2)
        self.assertIsNone(d.search(7))

    def test_remove_front_rear(self):
        d = make([1, 2, 3])
        self.assertEqual(d.removeFront(), 1)
        self.assertEqual(d.removeRear(), 3)
        self.check(d, [2])
        self.assertEqual(d.removeRear(), 2)
        self.assertTrue(d.isEmpty())
        self.assertIsNone(d.tail)

    def test_insert_before(self):
        d = make([2, 4])
        d.insertBefore(d.search(2), 1)
        d.insertBefore(d.search(4), 3)
        self.check(d, [1, 2, 3, 4])

    def test_insert_after(self):
        d = make([1, 3])
        d.insertAfter(d.search(1), 2)
        d.insertAfter(d.search(3), 4)
        self.check(d, [1, 2, 3, 4])

    def test_remove_node(self):
        d = make([1, 2, 3, 4])
        d.removeNode(d.search(2))
        self.check(d, [1, 3, 4])
        d.removeNode(d.search(1))
        self.check(d, [3, 4])
        d.removeNode(d.search(4))
        self.check(d, [3])
        d.removeNode(d.search(3))
        self.check(d, [])
        self.assertTrue(d.isEmpty())


if __name__ == "__main__":
    unittest.main(verbosity=2)
