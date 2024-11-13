import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("test", TextType.CODE)
        self.assertEqual(node, node2)
        self.assertEqual(node3.__repr__(), "TextNode(test, code, None)")

if __name__ == "__main__":
    unittest.main()