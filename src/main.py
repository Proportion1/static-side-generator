from textnode import TextNode
from textnode import TextType
from leafnode import LeafNode
from splitNodesDelimiter import split_nodes_delimiter
import re



def main():
    #text_node = TextNode("running main", TextType.BOLD, "www.derp.com")
    #print(text_node)
    pass

def text_node_to_html_node(text_node: TextNode):
    #textnode - self, text, text_type, url=None
    #htmlnode - self, tag=None, value=None, children=None, props={}
    tag = None
    props = {}
    value = text_node.text
    match text_node.text_type:
        case TextType.TEXT:
            tag = None
        case TextType.BOLD:
            tag = "b"
        case TextType.ITALIC:
            tag = "i"
        case TextType.CODE:
            tag = "code"
        case TextType.LINK:
            tag = "a"
            props["href"] = text_node.url
        case TextType.IMAGE:
            tag = "img"
            value = ""
            props["src"] = text_node.url
            props["alt"] = text_node.text
        case _:
            raise Exception("selection not found")

    return LeafNode(tag, value, props)

def extract_markdown_images(text):
    result = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return result

def extract_markdown_links(text):
    result = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return result

def text_to_textnodes(text):
    pass

main()