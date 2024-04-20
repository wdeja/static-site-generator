import unittest 

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_none(self):
        node = HTMLNode()
        expected = "HTMLNode(None, None, None, None)"
        self.assertEqual(node.__repr__(),expected)

    def test_props_to_html(self):
        test_dic = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(props=test_dic)
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_to_html(self):
        node = HTMLNode()
        self.assertRaises(NotImplementedError,node.to_html)

    def test_props_to_html_empty(self): 
        test_dic = {}
        node = HTMLNode(props=test_dic)
        self.assertEqual(node.props_to_html(), "")


if __name__ == "__main__":
    unittest.main()
    