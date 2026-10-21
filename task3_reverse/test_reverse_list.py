import unittest

from reverse_list import from_list, reverse_iter, reverse_rec, to_list


class TestReverse(unittest.TestCase):
    def check(self, func):
        self.assertIsNone(func(None))
        self.assertEqual(to_list(func(from_list([1]))), [1])
        self.assertEqual(to_list(func(from_list([1, 2]))), [2, 1])
        self.assertEqual(to_list(func(from_list([1, 2, 3, 4]))), [4, 3, 2, 1])

    def test_iter(self):
        self.check(reverse_iter)

    def test_rec(self):
        self.check(reverse_rec)

    def test_old_head_is_last(self):
        # бывший первый узел стал последним
        head = from_list([1, 2, 3])
        new_head = reverse_iter(head)
        self.assertIsNone(head.getNext())
        self.assertEqual(new_head.getData(), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
