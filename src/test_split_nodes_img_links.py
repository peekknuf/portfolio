import unittest
from htmlnode import TextNode, TextType
from split_nodes import split_nodes_image, split_nodes_link


class TestNodeSplitting(unittest.TestCase):
    def test_split_nodes_link_basic(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and some text after",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is text with a link ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT.value)
        self.assertEqual(new_nodes[1].text, "to boot dev")
        self.assertEqual(new_nodes[1].text_type, TextType.HTML.value)  # Note: LINK is "html"
        self.assertEqual(new_nodes[1].url, "https://www.boot.dev")
        self.assertEqual(new_nodes[2].text, " and some text after")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT.value)

    def test_split_nodes_link_multiple(self):
        node = TextNode(
            "Links: [first](https://first.com) and [second](https://second.com)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        
        self.assertEqual(new_nodes[0].text, "Links: ")
        self.assertEqual(new_nodes[1].text, "first")
        self.assertEqual(new_nodes[1].url, "https://first.com")
        self.assertEqual(new_nodes[2].text, " and ")
        self.assertEqual(new_nodes[3].text, "second")
        self.assertEqual(new_nodes[3].url, "https://second.com")

    def test_split_nodes_link_no_links(self):
        node = TextNode("Plain text without links", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "Plain text without links")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT.value)

    def test_split_nodes_link_empty_text(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT.value)

    def test_split_nodes_image_basic(self):
        node = TextNode(
            "Text with image ![alt text](https://example.com/image.jpg) after",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "Text with image ")
        self.assertEqual(new_nodes[1].text, "alt text")
        self.assertEqual(new_nodes[1].text_type, TextType.IMAGE.value)
        self.assertEqual(new_nodes[1].url, "https://example.com/image.jpg")
        self.assertEqual(new_nodes[2].text, " after")

    def test_split_nodes_image_multiple(self):
        node = TextNode(
            "![first](https://first.jpg) middle ![second](https://second.jpg)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        
        self.assertEqual(new_nodes[0].url, "https://first.jpg")
        self.assertEqual(new_nodes[1].text, " middle ")
        self.assertEqual(new_nodes[2].text, "second")
        self.assertEqual(new_nodes[2].url, "https://second.jpg")

    def test_split_nodes_image_no_images(self):
        node = TextNode("Just text no images", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "Just text no images")

    def test_split_nodes_image_with_link(self):
        node = TextNode(
            "Here's a link with ![image](https://img.com) inside [it](https://link.com)",
            TextType.TEXT
        )
        # First split images
        nodes_after_images = split_nodes_image([node])
        # Then split links
        final_nodes = []
        for n in nodes_after_images:
            if n.text_type == TextType.TEXT.value:
                final_nodes.extend(split_nodes_link([n]))
            else:
                final_nodes.append(n)
        
        self.assertEqual(len(final_nodes), 5)
        self.assertEqual(final_nodes[0].text, "Here's a link with ")
        self.assertEqual(final_nodes[1].text, "image")
        self.assertEqual(final_nodes[1].text_type, TextType.IMAGE.value)
        self.assertEqual(final_nodes[2].text, " inside ")
        self.assertEqual(final_nodes[3].text, "it")
        self.assertEqual(final_nodes[3].text_type, TextType.HTML.value)

    def test_split_nodes_edge_cases(self):
        # Test empty nodes list
        self.assertEqual(split_nodes_link([]), [])
        self.assertEqual(split_nodes_image([]), [])
        
        # Test non-text node types
        link_node = TextNode("existing link", TextType.HTML, "https://example.com")
        self.assertEqual(split_nodes_link([link_node]), [link_node])
        self.assertEqual(split_nodes_image([link_node]), [link_node])

    def test_split_nodes_consecutive_elements(self):
        node = TextNode(
            "[link1](https://one.com)[link2](https://two.com)![img](https://img.com)",
            TextType.TEXT.value
        )
        nodes = split_nodes_link([node])
        
        self.assertEqual(nodes[0].text, "link1")
        self.assertEqual(nodes[0].url, "https://one.com")
        self.assertEqual(nodes[1].text, "link2")
        self.assertEqual(nodes[1].url, "https://two.com")

if __name__ == '__main__':
    unittest.main()