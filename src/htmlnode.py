
class HTMLNode:
    def __init__(self, tag: str | None = None, value: str | None = None, children=None, props: dict | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        
        attributes = ""
        for key in self.props:
            current_attr = f" {key}=\"{self.props[key]}\""
            attributes = attributes + current_attr
        return attributes

    def __repr__(self):
        return f"HTMLNode(\ntag={self.tag}\nvalue={self.value}\nchildren={self.children}\nprops={self.props}\n)"

# Node with no children
class LeafNode(HTMLNode):
    def __init__(self, value: str, tag: str | None = None, props: dict | None = None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        if self.tag:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return self.value
    
# Node with children
class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict | None = None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        children_html = ""
        for nodes in self.children:
            children_html = children_html + nodes.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
        
