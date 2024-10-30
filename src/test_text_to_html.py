import unittest
from htmlnode import TextType, text_node_to_html_node

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_node_to_html_node_text(self):
        text_node = TextType.TEXT
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "text")

    def test_text_node_to_html_node_leaf(self):
        text_node = TextType.LEAF
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "leaf")

    def test_text_node_to_html_node_html(self):
        text_node = TextType.HTML
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "html")
        self.assertEqual(html_node.value, "html")

    def test_text_node_to_html_node_invalid_text_node(self):
        with self.assertRaises(ValueError):
            text_node_to_html_node("Invalid text node")

if __name__ == "__main__":
    unittest.main()
