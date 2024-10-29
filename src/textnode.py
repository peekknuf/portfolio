from enum import Enum

class TextType(Enum):
    HTML = "html"
    LEAF = "leaf"
    TEXT = "text"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type.value  # Using the .value attribute from the TextType enum
        self.url = url  # Defaults to None if nothing is passed

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return (self.text == other.text and
                    self.text_type == other.text_type and
                    self.url == other.url)
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

