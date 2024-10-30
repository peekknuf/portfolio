import re

def extract_markdown_images(text):
    image_pattern = r'!\[([^\]]*)\]\((https?://[^\)]+)\)'
    return re.findall(image_pattern, text)

def extract_markdown_links(text):
    link_pattern = r'(?<!\!)\[(.*?)\]\((https?://[^\)]+)\)'
    return re.findall(link_pattern, text)
