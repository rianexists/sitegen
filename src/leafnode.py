from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("Object requires value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html().rstrip()}>{self.value}</{self.tag}>"