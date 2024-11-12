from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value,  props={}):
        self.children = None
        super().__init__(tag, value, self.children, props) 
        

    def to_html(self):
        if self.value == None:
            raise ValueError("value can't be None")
        elif self.tag == None:
            return f'{self.value}'
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'