from textnode import TextNode, TextType

def main():
    node = TextNode("This is a text node", TextType.BOLD, "boot.dev")
    print(node.__repr__())

main()