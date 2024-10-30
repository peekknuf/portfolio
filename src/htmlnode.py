from enum import Enum
from split_nodes import split_nodes_image, split_nodes_link, split_nodes_delimiter

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def props_to_html(self):
        return ' '.join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return (f"HTMLNode(tag={self.tag}, value={self.value}, children={len(self.children)}, "
                f"props={self.props})")

    def to_html(self):
        raise NotImplementedError("to_html must be implemented by subclasses")

class TextType(Enum):
    HTML = "html"
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    IMAGE = "image"
    LINK = "link"
    


class TextNode:
    def __init__(self, text, text_type, url=None):
        if isinstance(text_type, TextType):
            self.text = text
            self.text_type = text_type.value 
            self.url = url
        else:
            raise ValueError("text_type must be an instance of TextType")

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return (self.text == other.text and
                    self.text_type == other.text_type and
                    self.url == other.url)
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value.")
        super().__init__(tag=tag, value=value, children=[], props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value to render.")
        if not self.tag:
            return self.value 
        else:
            props_html = self.props_to_html()
            return f"<{self.tag}{(' ' + props_html) if props_html else ''}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not tag:
            raise ValueError("ParentNode must have a tag.")
        if not children:
            raise ValueError("ParentNode must have children.")
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag to render.")
        if not self.children:
            raise ValueError("ParentNode must have children to render.")

        children_html = ''.join(child.to_html() for child in self.children)
        props_html = self.props_to_html()

        return f"<{self.tag}{(' ' + props_html) if props_html else ''}>{children_html}</{self.tag}>"


def text_node_to_html_node(text_node) -> LeafNode:
    if isinstance(text_node, TextType):
        if text_node == TextType.TEXT:
            return LeafNode(None, text_node.value)
        elif text_node == TextType.LEAF:
            return LeafNode(None, text_node.value)
        elif text_node == TextType.HTML:
            return LeafNode("html", text_node.value)
        else:
            raise ValueError("Unsupported TextType")
    else:
        raise ValueError("Invalid text node")
    
def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    return nodes
    
    



