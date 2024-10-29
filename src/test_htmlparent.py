import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_init(self):
        node = ParentNode("p", [LeafNode("b", "Bold text")])
        self.assertEqual(node.tag, "p")
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.children[0].tag, "b")
        self.assertEqual(node.children[0].value, "Bold text")

    def test_init_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("b", "Bold text")])

    def test_init_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("p", [])

    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html_nested(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                ParentNode(
                    "span",
                    [
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                    ],
                ),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b><span>Normal text<i>italic text</i></span>Normal text</p>",
        )

    def test_to_html_with_props(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            props={"class": "my-class", "id": "my-id"},
        )
        self.assertEqual(
            node.to_html(),
            '<p class="my-class" id="my-id"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>',
        )

if __name__ == "__main__":
    unittest.main()
