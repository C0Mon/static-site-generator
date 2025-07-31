import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_two(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(props=props)
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")

    def test_props_to_html_five(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
            "name": "google",
            "occupation": "search engine",
            "hobbies": "stealing data",
        }
        node = HTMLNode(props=props)
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\" name=\"google\" occupation=\"search engine\" hobbies=\"stealing data\"")
    
    def test_props_to_html_none(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode(tag="p", value="Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode(tag="a", value="Hello, world!")
        self.assertEqual(node.to_html(), "<a>Hello, world!</a>")

    def test_leaf_to_html_none(self):
        node = LeafNode(value="Haii")
        self.assertEqual(node.to_html(), "Haii")

    def test_leaf_to_html_empty(self):
        with self.assertRaises(TypeError):
            LeafNode()
