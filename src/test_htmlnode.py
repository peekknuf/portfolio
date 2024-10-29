# test_htmlnode.py
import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="a", props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://example.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode(tag="p", value="Hello")
        self.assertEqual(repr(node), "HTMLNode(tag=p, value=Hello, children=0, props={})")

    def test_empty_node(self):
        node = HTMLNode()
        self.assertEqual(repr(node), "HTMLNode(tag=None, value=None, children=0, props={})")

if __name__ == "__main__":
    unittest.main()

