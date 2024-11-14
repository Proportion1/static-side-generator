from textnode import TextNode
from textnode import TextType
from leafnode import LeafNode


def main():
    text_node = TextNode("words", TextType.BOLD, "www.derp.com")
    print(text_node)

def text_node_to_html_node(text_node: TextNode):
    #textnode - self, text, text_type, url=None
    #htmlnode - self, tag=None, value=None, children=None, props={}
    tag = None
    props = {}
    value = text_node.text
    match text_node.text_type:
        case TextType.NORMAL:
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

main()