import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p","This is a leaf node", None)
        node2 = LeafNode("p","This is a leaf node", None)
        
        self.assertEqual(node, node2)

    def test_to_html(self):
        node = LeafNode("p","This is a leaf node", None)
        self.assertEqual(node.to_html(), "<p>This is a leaf node</p>")

    def test_to_html_link(self):
        node = LeafNode("a", "Link Test", {"href": "www.google.com"})
        #print(node.props_to_html())
        #print(node.to_html())

    def test_props_rendering(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected = '<a href="https://www.google.com">Click me!</a>'
        #print(node.to_html())
        self.assertEqual(node.to_html(), expected)

    #def test_no_value(self):
    #    node = LeafNode()





if __name__ == "__main__":
    unittest.main()