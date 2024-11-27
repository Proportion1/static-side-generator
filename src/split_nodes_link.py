from textnode import TextNode, TextType
from main import extract_markdown_links
from typing import List

def split_nodes_link(old_nodes: List[TextNode]):
    node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
        else:
            # Use the extract function
            links = extract_markdown_links(node.text)
            remaining_text = node.text

            # Check if there are links
            if links:
                for link in links:
                    # Split the text around the link markdown
                    parts = remaining_text.split(f"[{link[0]}]({link[1]})", 1)

                    # Create a TextNode for text before the markdown (if any)
                    if parts[0]:
                        node_list.append(TextNode(parts[0], TextType.TEXT))
                    
                    # Create a TextNode for the image itself
                    node_list.append(TextNode(link[0], TextType.LINK, link[1]))

                    # Remaining text after this image
                    remaining_text = parts[1]

                # Any text left after the last image
                if remaining_text:
                    node_list.append(TextNode(remaining_text, TextType.TEXT))
            else:
                node_list.append(node)

    return node_list

