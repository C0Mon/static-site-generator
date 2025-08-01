import unittest

from textnode import TextNode, TextType, text_node_to_html_node

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

class TestTextNodeConversion(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
    
    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, { "href": "https://google.com" })

    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "https://google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props, 
            { 
                "src": "https://google.com",
                "alt": "This is an image node",
            }
        )

if __name__ == "__main__":
    unittest.main()