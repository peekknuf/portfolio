
import re

def extract_markdown_images(text):
    image_pattern = r'!\[([^\]]*)\]\((https?://[^\)]+)\)'
    return re.findall(image_pattern, text)

def extract_markdown_links(text):
    link_pattern = r'(?<!\!)\[(.*?)\]\((https?://[^\)]+)\)'
    return re.findall(link_pattern, text)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    from htmlnode import TextType, TextNode
    new_nodes = []
    
    for node in old_nodes:
        if isinstance(node, TextNode) and node.text_type == TextType.TEXT.value:
            parts = node.text.split(delimiter)
            if len(parts) == 1 and not parts[0]: 
                new_nodes.append(TextNode("", TextType.TEXT))
            else:
                for i, part in enumerate(parts):
                    if i % 2 == 0:
                        if part:
                            new_nodes.append(TextNode(part, TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(part, text_type))
        else:
            new_nodes.append(node)
    
    return new_nodes



def split_nodes_image(old_nodes):
    from htmlnode import TextType, TextNode
    new_nodes = []
    
    for node in old_nodes:
        if isinstance(node, TextNode) and node.text_type == TextType.TEXT.value:
            text = node.text
            images = extract_markdown_images(text)
            
            if not images:
                new_nodes.append(node)
                continue
                
            current_position = 0
            for alt_text, url in images:
                image_pattern = f"![{alt_text}]({url})"
                pattern_index = text.find(image_pattern, current_position)
                
                if pattern_index > current_position:
                    new_nodes.append(TextNode(text[current_position:pattern_index], TextType.TEXT))
                
                new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
                current_position = pattern_index + len(image_pattern)
            
            if current_position < len(text):
                new_nodes.append(TextNode(text[current_position:], TextType.TEXT))
        else:
            new_nodes.append(node)
    
    return new_nodes

def split_nodes_link(old_nodes):
    from htmlnode import TextType, TextNode
    new_nodes = []
    
    for node in old_nodes:
        if isinstance(node, TextNode) and node.text_type == TextType.TEXT.value:
            text = node.text
            links = extract_markdown_links(text)
            
            if not links:
                new_nodes.append(node)
                continue
                
            current_position = 0
            for link_text, url in links:
                link_pattern = f"[{link_text}]({url})"
                pattern_index = text.find(link_pattern, current_position)

                if pattern_index > current_position:
                    new_nodes.append(TextNode(text[current_position:pattern_index], TextType.TEXT))
                
                new_nodes.append(TextNode(link_text, TextType.LINK, url))
                current_position = pattern_index + len(link_pattern)
            
            if current_position < len(text):
                new_nodes.append(TextNode(text[current_position:], TextType.TEXT))
        else:
            new_nodes.append(node)
    
    return new_nodes