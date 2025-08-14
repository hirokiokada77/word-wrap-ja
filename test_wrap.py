import unittest
from wrap import wrap_text


class TestWrapText(unittest.TestCase):
    def test_wrap_text_basic(self):
        input_text = "これはテストです。"
        max_width = 5
        expected_output = "これ\nは\nテスト\nです。"
        wrapped_text = wrap_text(input_text, max_width)
        self.assertEqual(wrapped_text, expected_output)

    def test_wrap_text_with_newline(self):
        input_text = "これはテストです。\n改行もテスト。"
        max_width = 20
        expected_output = "これはテストです。\n改行もテスト。"
        wrapped_text = wrap_text(input_text, max_width)
        self.assertEqual(wrapped_text, expected_output)

    def test_wrap_text_no_wrap_needed(self):
        input_text = "これは長い文章です。"
        max_width = 20
        expected_output = "これは長い文章です。"
        wrapped_text = wrap_text(input_text, max_width)
        self.assertEqual(wrapped_text, expected_output)

    def test_wrap_text_with_prohibited_chars(self):
        input_text = "、これはテストです。"
        max_width = 5
        expected_output = "、\nこれ\nは\nテスト\nです。"
        wrapped_text = wrap_text(input_text, max_width)
        self.assertEqual(wrapped_text, expected_output)

    def test_wrap_text_edge_case_empty(self):
        input_text = ""
        max_width = 5
        expected_output = ""
        wrapped_text = wrap_text(input_text, max_width)
        self.assertEqual(wrapped_text, expected_output)

    def test_wrap_text_edge_case_single_char(self):
        input_text = "あ"
        max_width = 1
        expected_output = "あ"
        wrapped_text = wrap_text(input_text, max_width)
        self.assertEqual(wrapped_text, expected_output)


if __name__ == "__main__":
    unittest.main()
