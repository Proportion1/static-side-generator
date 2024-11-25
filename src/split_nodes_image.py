from textnode import TextNode, TextType
from typing import List
from main import extract_markdown_images

def split_nodes_image(old_nodes: List[TextNode]):
    node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
        else:
            # Use the extract function
            images = extract_markdown_images(node.text)
            remaining_text = node.text

            # Check if there are images
            if images:
                for image in images:
                    # Split the text around the image markdown
                    parts = remaining_text.split(f"![{image[0]}]({image[1]})", 1)
                    
                    # Create a TextNode for text before the markdown (if any)
                    if parts[0]:
                        node_list.append(TextNode(parts[0], TextType.TEXT))
                    
                    # Create a TextNode for the image itself
                    node_list.append(TextNode(image[0], TextType.IMAGE, image[1]))

                    # Remaining text after this image
                    remaining_text = parts[1]

                # Any text left after the last image
                if remaining_text:
                    node_list.append(TextNode(remaining_text, TextType.TEXT))
            else:
                node_list.append(node)

    return node_list