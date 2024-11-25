import unittest
from splitNodesDelimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_one_set_of_delimiters(self):
        node = [TextNode("this has `code` in it", TextType.TEXT)]
        node_list = split_nodes_delimiter(node, "`", TextType.CODE)
        self.assertEqual(len(node_list), 3)
        self.assertEqual(node_list[0].text, "this has ")
        self.assertEqual(node_list[0].text_type, TextType.TEXT)
        self.assertEqual(node_list[1].text, "code")
        self.assertEqual(node_list[1].text_type, TextType.CODE)
        self.assertEqual(node_list[2].text, " in it")
        self.assertEqual(node_list[2].text_type, TextType.TEXT)


if __name__ == "__main__":
    unittest.main()
        