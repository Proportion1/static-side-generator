import unittest
from main import markdown_to_blocks



class test_markdown_to_blocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        markdown = """# This is a heading


This is a paragraph of text. It has some **bold** and *italic* words inside of it.



* This is the first list item in a list block
* This is a list item
* This is another list item"""

        markdown2 = """Block 1

Block 2

Block 3"""

        blocks = markdown_to_blocks(markdown)
        blocks2 = markdown_to_blocks(markdown2)
        #print(blocks)
        self.assertEqual(blocks, ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item'])
        self.assertEqual(blocks2, ['Block 1', 'Block 2', 'Block 3'])