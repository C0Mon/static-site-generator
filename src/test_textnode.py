import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("Halloo", TextType.ITALIC)
        node2 = TextNode("Halloo", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("Halloo", TextType.ITALIC)
        node2 = TextNode("GoodByeeee", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_texttype(self):
        node = TextNode("Halloo", TextType.ITALIC)
        node2 = TextNode("GoodByeeee", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("Halloo", TextType.ITALIC, "https://google.com")
        node2 = TextNode("Halloo", TextType.ITALIC, "https://google.com")
        self.assertEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("Halloo", TextType.ITALIC, "https://bing.com")
        node2 = TextNode("Halloo", TextType.ITALIC, "https://google.com")
        self.assertNotEqual(node, node2)

    def test_one_url_none(self):
        node = TextNode("Halloo", TextType.ITALIC, "https://google.com")
        node2 = TextNode("Halloo", TextType.ITALIC)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()