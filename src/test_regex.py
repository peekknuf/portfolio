import unittest
from reg import extract_markdown_images, extract_markdown_links

class TestMarkdownExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(result, expected)

    def test_extract_markdown_images_no_images(self):
        text = "This is a text with no images."
        result = extract_markdown_images(text)
        expected = []
        self.assertEqual(result, expected)

    def test_extract_markdown_images_empty_alt_text(self):
        text = "This is text with an image without alt text ![](https://i.imgur.com/noAlt.png)"
        result = extract_markdown_images(text)
        expected = [("", "https://i.imgur.com/noAlt.png")]
        self.assertEqual(result, expected)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(result, expected)

    def test_extract_markdown_links_no_links(self):
        text = "This is a text with no links."
        result = extract_markdown_links(text)
        expected = []
        self.assertEqual(result, expected)

    def test_extract_markdown_links_empty_anchor_text(self):
        text = "This is text with a link without anchor text [](https://www.noAnchor.com)"
        result = extract_markdown_links(text)
        expected = [("", "https://www.noAnchor.com")]
        self.assertEqual(result, expected)

    def test_extract_both_images_and_links(self):
        text = "Text with an image ![example](https://example.com/image.png) and a link [example](https://example.com)"
        images_result = extract_markdown_images(text)
        links_result = extract_markdown_links(text)
        images_expected = [("example", "https://example.com/image.png")]
        links_expected = [("example", "https://example.com")]
        self.assertEqual(images_result, images_expected)
        self.assertEqual(links_result, links_expected)

if __name__ == "__main__":
    unittest.main()
