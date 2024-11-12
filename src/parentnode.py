from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props={}):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode needs a tag")
        if self.children == None:
            raise ValueError("ParentNode Children can't be None")
        else:
            a = ""
            a += f"<{self.tag}>"
            for child in self.children:
                a += child.to_html()
            a += f"</{self.tag}>"
            return a



