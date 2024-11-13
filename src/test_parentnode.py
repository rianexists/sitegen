import unittest

from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    def testNoTag(self):
        node = ParentNode("a", None)
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()