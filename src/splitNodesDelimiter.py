from textnode import TextNode, TextType
from typing import List


def split_nodes_delimiter(old_nodes: List[TextNode], delimiter, text_type):
    node_list = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT or node.text.count(delimiter) == 0:
            node_list.append(node)
        elif node.text.count(delimiter) % 2 == 0:
            remaining_text = node.text
            while delimiter in remaining_text:
                first_delim = remaining_text.find(delimiter)
                second_delim = remaining_text.find(delimiter, first_delim + 1)
                node_list.append(TextNode(remaining_text[:first_delim], TextType.TEXT))
                node_list.append(TextNode(remaining_text[first_delim + len(delimiter):second_delim], text_type))
                remaining_text = remaining_text[second_delim + len(delimiter):]
            if(len(remaining_text) > 0):
                node_list.append(TextNode(remaining_text, TextType.TEXT))
            
        else:
            raise Exception("invalid markdown syntax")
        
    return node_list


