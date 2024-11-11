import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("h1")
        node2 = HTMLNode("h1")
        self.assertEqual(node, node2)

    def test_props_to_html_no_props(self):
        node = HTMLNode()
        #print(node.props_to_html())
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_one_prop(self):
        node = HTMLNode("a",None, None, {"href": "https://google.com"})
        #print(node.props_to_html())
        self.assertEqual(node.props_to_html(), ' href="https://google.com"')


if __name__ == "__main__":
    unittest.main()
