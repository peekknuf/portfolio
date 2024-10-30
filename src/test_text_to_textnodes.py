import unittest
from htmlnode import TextType, text_to_textnodes,split_nodes_image, split_nodes_link


class TestTextToTextNodes(unittest.TestCase):
    
    def test_basic_functionality(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://example.com/img.png) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 10)
        
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT.value)
        
        self.assertEqual(nodes[1].text, "text")
        self.assertEqual(nodes[1].text_type, TextType.BOLD.value)
        
        self.assertEqual(nodes[2].text, " with an ")
        self.assertEqual(nodes[2].text_type, TextType.TEXT.value)
        
        self.assertEqual(nodes[3].text, "italic")
        self.assertEqual(nodes[3].text_type, TextType.ITALIC.value)
        
        self.assertEqual(nodes[4].text, " word and a ")
        self.assertEqual(nodes[4].text_type, TextType.TEXT.value)
        
        self.assertEqual(nodes[5].text, "code block")
        self.assertEqual(nodes[5].text_type, TextType.CODE.value)
        
        self.assertEqual(nodes[6].text, " and an ")
        self.assertEqual(nodes[6].text_type, TextType.TEXT.value)
        
        self.assertEqual(nodes[7].text, "image")
        self.assertEqual(nodes[7].text_type, TextType.IMAGE.value)
        self.assertEqual(nodes[7].url, "https://example.com/img.png")
        
        self.assertEqual(nodes[8].text, " and a ")
        self.assertEqual(nodes[8].text_type, TextType.TEXT.value)
        
        self.assertEqual(nodes[9].text, "link")
        self.assertEqual(nodes[9].text_type, TextType.LINK.value)
        self.assertEqual(nodes[9].url, "https://boot.dev")

    def test_empty_string(self):
        nodes = text_to_textnodes("")
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "")
        self.assertEqual(nodes[0].text_type, TextType.TEXT.value)

    def test_plain_text(self):
        text = "Hello, world!"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "Hello, world!")
        self.assertEqual(nodes[0].text_type, TextType.TEXT.value)

    def test_multiple_instances_of_same_type(self):
        text = "**bold** and **another bold**"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 4)
        self.assertEqual(nodes[0].text, "bold")
        self.assertEqual(nodes[0].text_type, TextType.BOLD.value)
        self.assertEqual(nodes[2].text, "another bold")
        self.assertEqual(nodes[2].text_type, TextType.BOLD.value)

    def test_nested_markdown(self):
        text = "**bold with *italic***"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "bold with ")
        self.assertEqual(nodes[0].text_type, TextType.BOLD.value)
        self.assertEqual(nodes[1].text, "italic")
        self.assertEqual(nodes[1].text_type, TextType.ITALIC.value)
        self.assertEqual(nodes[2].text, "")
        self.assertEqual(nodes[2].text_type, TextType.BOLD.value)

    def test_multiple_links_and_images(self):
        text = "[link1](url1) ![img1](img1) [link2](url2) ![img2](img2)"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 4)
        self.assertEqual(nodes[0].text_type, TextType.LINK.value)
        self.assertEqual(nodes[1].text_type, TextType.IMAGE.value)
        self.assertEqual(nodes[2].text_type, TextType.LINK.value)
        self.assertEqual(nodes[3].text_type, TextType.IMAGE.value)

    def test_code_blocks_with_special_characters(self):
        text = "`code with * and ** and [] and ![]()`"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "code with * and ** and [] and ![]()")
        self.assertEqual(nodes[0].text_type, TextType.CODE.value)

    def test_all_types_mixed_together(self):
        text = "`code` *italic* **bold** [link](url) ![image](img)"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 5)
        self.assertEqual(nodes[0].text_type, TextType.CODE.value)
        self.assertEqual(nodes[1].text_type, TextType.ITALIC.value)
        self.assertEqual(nodes[2].text_type, TextType.BOLD.value)
        self.assertEqual(nodes[3].text_type, TextType.LINK.value)
        self.assertEqual(nodes[4].text_type, TextType.IMAGE.value)

if __name__ == "__main__":
    unittest.main()
