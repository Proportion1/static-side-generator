from textnode import TextNode
from textnode import TextType

def main():
    text_node = TextNode("words", TextType.BOLD, "www.derp.com")
    print(text_node)

main()