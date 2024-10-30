import unittest
from htmlnode import TextType,LeafNode, TextNode, split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_inline_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType("code"))
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType("code")),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(result, expected)
    
    def test_bold_text(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType("bold"))
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType("bold")),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)
    
    def test_italic_text(self):
        node = TextNode("An *italic* example", TextType.TEXT)
        result = split_nodes_delimiter([node], "*", TextType("italic"))
        expected = [
            TextNode("An ", TextType.TEXT),
            TextNode("italic", TextType("italic")),
            TextNode(" example", TextType.TEXT),
        ]
        self.assertEqual(result, expected)
    
    def test_multiple_delimiters(self):
        node = TextNode("Text with *italic* and `code`", TextType.TEXT)
        result = split_nodes_delimiter([node], "*", TextType("italic"))
        result = split_nodes_delimiter(result, "`", TextType("code"))
        expected = [
            TextNode("Text with ", TextType.TEXT),
            TextNode("italic", TextType("italic")),
            TextNode(" and ", TextType.TEXT),
            TextNode("code", TextType("code")),
        ]
        self.assertEqual(result, expected)
    
    def test_no_delimiter(self):
        node = TextNode("No special formatting", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType("code"))
        expected = [TextNode("No special formatting", TextType.TEXT)]
        self.assertEqual(result, expected)

    def test_empty_string(self):
        node = TextNode("", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType("code"))
        expected = [TextNode("", TextType.TEXT)]
        self.assertEqual(result, expected)

    def test_no_text_nodes(self):
        # Non-TextNode instances should remain unaffected
        leaf_node = LeafNode("span", "Some value", {"class": "example"})
        result = split_nodes_delimiter([leaf_node], "*", TextType("italic"))
        expected = [leaf_node]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()