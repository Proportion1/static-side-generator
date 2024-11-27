import unittest
from text_to_textnodes import text_to_textnodes

class Text_text_to_textnodes(unittest.TestCase):
    text = "This is **bold text** with **more bold text** and an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    node_list = text_to_textnodes(text)
    #print(node_list)