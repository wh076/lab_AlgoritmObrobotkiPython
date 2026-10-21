import io
import unittest
from contextlib import redirect_stdout

from move_to_front import move_to_front


def run(lines):
    # подменяем ввод списком строк
    it = iter(lines)
    out = io.StringIO()
    with redirect_stdout(out):
        lst = move_to_front(len(lines), lambda: next(it))
    return lst, out.getvalue().splitlines()


class TestMoveToFront(unittest.TestCase):
    def test_no_repeats(self):
        lst, out = run(["a", "b", "c"])
        self.assertEqual(str(lst), "['c', 'b', 'a']")
        self.assertEqual(out, ["['a']", "['b', 'a']", "['c', 'b', 'a']"])

    def test_repeat_moves_to_front(self):
        lst, out = run(["a", "b", "c", "a"])
        self.assertEqual(str(lst), "['a', 'c', 'b']")
        self.assertEqual(lst.size(), 3)

    def test_same_string(self):
        lst, out = run(["x", "x", "x"])
        self.assertEqual(out, ["['x']"] * 3)

    def test_zero(self):
        lst, out = run([])
        self.assertTrue(lst.isEmpty())
        self.assertEqual(out, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
