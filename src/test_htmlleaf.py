# test_htmlnode.py
import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_leafnode_no_tag(self):
        node = LeafNode(tag=None, value="Some raw text")
        self.assertEqual(node.to_html(), "Some raw text")

    def test_leafnode_with_tag(self):
        node = LeafNode(tag="p", value="This is a paragraph.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")

    def test_leafnode_with_tag_and_props(self):
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leafnode_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode(tag="p", value=None)

if __name__ == "__main__":
    unittest.main()
