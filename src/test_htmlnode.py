import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_two(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(props=props)
        self.assertEqual(
            node.props_to_html(), 
            " href=\"https://www.google.com\" target=\"_blank\""
        )

    def test_props_to_html_five(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
            "name": "google",
            "occupation": "search engine",
            "hobbies": "stealing data",
        }
        node = HTMLNode(props=props)
        self.assertEqual(
            node.props_to_html(), 
            " href=\"https://www.google.com\" target=\"_blank\" name=\"google\" occupation=\"search engine\" hobbies=\"stealing data\""
        )
    
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

    def test_leaf_empty(self):
        with self.assertRaises(TypeError):
            LeafNode()

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode(tag="b", value="Bold text"),
                LeafNode(value="Normal text"),
                LeafNode(tag="i", value="italic text"),
                LeafNode(value="Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(), 
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode(tag="b", value="grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_no_children(self):
        with self.assertRaises(TypeError):
            ParentNode("div")
    
    def test_no_tag(self):
        child_node = LeafNode("span", "child")
        with self.assertRaises(TypeError):
            ParentNode(children=[child_node])
    
