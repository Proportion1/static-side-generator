import unittest

from textnode import TextNode, TextType
from leafnode import LeafNode
from main import text_node_to_html_node

class test_text_node_to_html_node(unittest.TestCase):
    def test_text_node_to_html_node(self):
        text_node = TextNode("This is a leaf node", TextType.BOLD, None)
        leaf_node = text_node_to_html_node(text_node)
        #print(leaf_node)
        self.assertEqual(leaf_node, LeafNode("b", 'This is a leaf node', {}))

    def test_italic_node(self):
        text_node = TextNode("This is a leaf node", TextType.ITALIC, None)
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node.tag, "i")

    def test_code_node(self):
        text_node = TextNode("This is a leaf node", TextType.CODE, None)
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node.tag, "code")