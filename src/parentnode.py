from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        print(self.tag)
        if self.tag == None:
            raise ValueError("Object requires tag")
        if self.children == None:
            raise ValueError("Object requires children")
        string = f"<{self.tag}>"
        for item in self.children:
            string += item.to_html()
        return string + f"</{self.tag}>"