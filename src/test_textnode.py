import unittest
from htmlnode import TextNode, TextType

class TestTextNode(unittest.TestCase):

    def test_eq_same_properties(self):
        node1 = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node1, node2)

    def test_eq_different_text(self):
        node1 = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is another text node", TextType.TEXT)
        self.assertNotEqual(node1, node2)

    def test_eq_different_text_type(self):
        node1 = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.HTML)
        self.assertNotEqual(node1, node2)

    def test_eq_with_url(self):
        node1 = TextNode("This is a text node", TextType.TEXT, "https://example.com")
        node2 = TextNode("This is a text node", TextType.TEXT, "https://another.com")
        self.assertNotEqual(node1, node2)

    def test_eq_none_url(self):
        node1 = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT, None)
        self.assertEqual(node1, node2)

    def test_repr(self):
        node = TextNode("Sample text", TextType.LEAF, "https://sample.com")
        expected_repr = "TextNode(Sample text, leaf, https://sample.com)"
        self.assertEqual(repr(node), expected_repr)


if __name__ == "__main__":
    unittest.main()

