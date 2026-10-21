import os
import unittest

from html_check import check_file, check_html

FOLDER = os.path.dirname(os.path.abspath(__file__))


class TestHtmlCheck(unittest.TestCase):
    def test_example_file(self):
        self.assertTrue(check_file(os.path.join(FOLDER, "example.html")))

    def test_bad_file(self):
        self.assertFalse(check_file(os.path.join(FOLDER, "bad_example.html")))

    def test_simple_ok(self):
        self.assertTrue(check_html("<html><body><p>текст</p></body></html>"))
        self.assertTrue(check_html(""))

    def test_attributes(self):
        html = '<div class="a" id="b"><a href="x.html">ссылка</a></div>'
        self.assertTrue(check_html(html))

    def test_void_tags(self):
        html = '<p>a<br>b<br/><img src="1.png"><hr><input type="t"></p>'
        self.assertTrue(check_html(html))

    def test_case(self):
        self.assertTrue(check_html("<DIV><p></P></div>"))

    def test_not_closed(self):
        self.assertFalse(check_html("<html><body></html>"))

    def test_extra_close(self):
        self.assertFalse(check_html("<p></p></div>"))

    def test_wrong_order(self):
        self.assertFalse(check_html("<b><i>текст</b></i>"))

    def test_comment_ignored(self):
        self.assertTrue(check_html("<p><!-- <div> --></p>"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
