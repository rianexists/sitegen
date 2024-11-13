class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Method not valid on parent class")
    
    def props_to_html(self):
        if self.props == None:
            return ""
        string = " "
        for item in self.props.items():
            string += f'{item[0]}="{item[1]}" '
        return string[:-1]

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"