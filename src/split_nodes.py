from htmlnode import TextType, TextNode
from reg import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    """
    Split text nodes that contain markdown images into separate text and image nodes.
    """
    if not old_nodes:
        return []

    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode) or node.text_type != TextType.TEXT.value:
            new_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)
        if not images:
            new_nodes.append(node)
            continue

        current_pos = 0
        for alt_text, url in images:
            image_markdown = f"![{alt_text}]({url})"
            start_index = text.find(image_markdown, current_pos)
            
            # Add text before image if there is any
            if start_index > current_pos:
                new_nodes.append(TextNode(text[current_pos:start_index], TextType.TEXT))
            elif current_pos == 0 and start_index == 0:
                new_nodes.append(TextNode("", TextType.TEXT))
            
            # Add image node
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            
            current_pos = start_index + len(image_markdown)

        # Add remaining text if any exists
        if current_pos < len(text):
            remaining_text = text[current_pos:]
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
        elif len(images) > 0:  # Only add empty text at end if we processed at least one image
            new_nodes.append(TextNode("", TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    """
    Split text nodes that contain markdown links into separate text and link nodes.
    """
    if not old_nodes:
        return []

    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode) or node.text_type != TextType.TEXT.value:
            new_nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)
        if not links:
            new_nodes.append(node)
            continue

        current_pos = 0
        for anchor_text, url in links:
            link_markdown = f"[{anchor_text}]({url})"
            start_index = text.find(link_markdown, current_pos)
            
            # Add text before link if there is any
            if start_index > current_pos:
                new_nodes.append(TextNode(text[current_pos:start_index], TextType.TEXT))
            elif current_pos == 0 and start_index == 0:
                new_nodes.append(TextNode("", TextType.TEXT))
            
            # Add link node
            new_nodes.append(TextNode(anchor_text, TextType.HTML, url))
            
            current_pos = start_index + len(link_markdown)

        # Add remaining text if any exists
        if current_pos < len(text):
            remaining_text = text[current_pos:]
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
        elif len(links) > 0:  # Only add empty text at end if we processed at least one link
            new_nodes.append(TextNode("", TextType.TEXT))

    return new_nodes