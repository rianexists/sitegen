import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def testToHTML(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()  # Call the method inside the context manager
    
    def testPropsToHTML(self):
        node = HTMLNode(props={
            "href": "https://www.google.com", 
            "target": "_blank",
        })
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

if __name__ == "__main__":
    unittest.main()