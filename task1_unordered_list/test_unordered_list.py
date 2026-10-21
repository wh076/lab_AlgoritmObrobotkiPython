import unittest

from unordered_list import UnorderedList


def make(items):
    # создаёт список из обычного списка Python
    lst = UnorderedList()
    for x in items:
        lst.append(x)
    return lst


class TestBase(unittest.TestCase):
    def test_empty(self):
        lst = UnorderedList()
        self.assertTrue(lst.isEmpty())
        self.assertEqual(lst.size(), 0)
        self.assertFalse(lst.search(1))

    def test_add_search_remove(self):
        lst = UnorderedList()
        lst.add(1)
        lst.add(2)
        self.assertEqual(str(lst), "[2, 1]")
        self.assertTrue(lst.search(1))
        lst.remove(2)
        self.assertEqual(str(lst), "[1]")
        with self.assertRaises(ValueError):
            lst.remove(5)


class TestAppend(unittest.TestCase):
    def test_append_empty(self):
        lst = UnorderedList()
        lst.append(1)
        self.assertEqual(str(lst), "[1]")

    def test_append_end(self):
        lst = make([1, 2])
        lst.append(3)
        self.assertEqual(str(lst), "[1, 2, 3]")


class TestIndex(unittest.TestCase):
    def test_index(self):
        lst = make([5, 6, 7])
        self.assertEqual(lst.index(5), 0)
        self.assertEqual(lst.index(6), 1)
        self.assertEqual(lst.index(7), 2)

    def test_index_missing(self):
        with self.assertRaises(ValueError):
            make([1]).index(9)


class TestInsert(unittest.TestCase):
    def test_insert_empty(self):
        lst = UnorderedList()
        lst.insert(0, 1)
        self.assertEqual(str(lst), "[1]")

    def test_insert_start_middle_end(self):
        lst = make([2, 4])
        lst.insert(0, 1)
        lst.insert(2, 3)
        lst.insert(4, 5)
        self.assertEqual(str(lst), "[1, 2, 3, 4, 5]")


class TestPop(unittest.TestCase):
    def test_pop_empty(self):
        with self.assertRaises(IndexError):
            UnorderedList().pop()

    def test_pop_last(self):
        lst = make([1, 2, 3])
        self.assertEqual(lst.pop(), 3)
        self.assertEqual(str(lst), "[1, 2]")

    def test_pop_one(self):
        lst = make([1])
        self.assertEqual(lst.pop(), 1)
        self.assertTrue(lst.isEmpty())

    def test_pop_pos(self):
        lst = make([1, 2, 3, 4])
        self.assertEqual(lst.pop(0), 1)
        self.assertEqual(lst.pop(1), 3)
        self.assertEqual(lst.pop(1), 4)
        self.assertEqual(str(lst), "[2]")

    def test_pop_bad_pos(self):
        with self.assertRaises(IndexError):
            make([1, 2]).pop(5)


class TestStr(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(UnorderedList()), "[]")
        self.assertEqual(str(make([1, 2, 3])), "[1, 2, 3]")
        self.assertEqual(str(make(["a", "b"])), "['a', 'b']")


class TestSlice(unittest.TestCase):
    def test_slice_middle(self):
        lst = make([0, 1, 2, 3, 4])
        self.assertEqual(str(lst.slice(1, 4)), "[1, 2, 3]")

    def test_slice_start_end(self):
        lst = make([0, 1, 2, 3, 4])
        self.assertEqual(str(lst.slice(0, 2)), "[0, 1]")
        self.assertEqual(str(lst.slice(3, 5)), "[3, 4]")

    def test_slice_empty(self):
        self.assertEqual(str(UnorderedList().slice(0, 3)), "[]")
        self.assertEqual(str(make([1, 2]).slice(1, 1)), "[]")

    def test_slice_is_copy(self):
        lst = make([1, 2, 3])
        part = lst.slice(0, 2)
        part.append(9)
        self.assertEqual(str(lst), "[1, 2, 3]")


if __name__ == "__main__":
    unittest.main(verbosity=2)
