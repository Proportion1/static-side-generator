import unittest
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link
from textnode import TextNode, TextType

class TestSplitNodesImageandlink(unittest.TestCase):
    pass
    def test_split_nodes_image(self):
        node_with_2_images = TextNode("this is some text ![this is a image description](https://i.imgur.com/aKaOqIh.gif) heres some more words after. ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT,)
        node_with_1_image_and_text_after = TextNode("this is some text ![this is a image description](https://i.imgur.com/aKaOqIh.gif) heres some more words after. ", TextType.TEXT,)
        node_with_1_image = TextNode("this is some text ![this is a image description](https://i.imgur.com/aKaOqIh.gif)", TextType.TEXT,)
        split_nodes_2_images = split_nodes_image([node_with_2_images])
        split_nodes_1_image_and_text_after = split_nodes_image([node_with_1_image_and_text_after])
        split_nodes_1_image = split_nodes_image([node_with_1_image])
        #print(split_nodes_2_images)
        self.assertEqual(split_nodes_1_image_and_text_after, [TextNode("this is some text " , TextType.TEXT), TextNode("this is a image description", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"), TextNode(" heres some more words after. ", TextType.TEXT)])
        self.assertEqual(split_nodes_1_image, [TextNode("this is some text " , TextType.TEXT), TextNode("this is a image description", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif")])
        self.assertEqual(split_nodes_2_images, [TextNode("this is some text " , TextType.TEXT), TextNode("this is a image description", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"), TextNode(" heres some more words after. ", TextType.TEXT), TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")])
        
    def test_split_nodes_link(self):
        node_with_1_link = TextNode("this is some text [this is a link description](https://i.imgur.com/aKaOqIh.gif)", TextType.TEXT,)
        split_nodes_1_link = split_nodes_link([node_with_1_link])
        #print(split_nodes_1_link)