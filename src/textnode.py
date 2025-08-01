from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT= "text"
    BOLD = "bold"
    ITALIC= "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text: str, text_type: str, url: str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if isinstance(other, TextNode):
            return (
                self.text == other.text and 
                self.text_type == other.text_type and 
                self.url == other.url
                )
        return False

    def __repr__(self):
        return(f"TextNode({self.text}, {self.text_type.value}, {self.url})")


def text_node_to_html_node(text_node: TextNode):
    match text_node.text_type.value:
        case "text":
            tag = None
        case "bold":
            tag = "b"
        case "italic":
            tag = "i"
        case "code":
            tag = "code"
        case "link":
            return LeafNode(text_node.text, "a", { "href": text_node.url })
        case "image":
            return LeafNode(
                "", 
                "img",
                {
                    "src": text_node.url,
                    "alt": text_node.text
                }
                )
        case _:
            raise Exception("Error: Unknown tag")
    return LeafNode(text_node.text, tag)