import unittest 

from htmlnode import LeafNode

class TestHtmlNode(unittest.TestCase):
    # def test_none(self):
    #     node = LeafNode()
    #     expected = "LeafNode(None, None, None)"
    #     self.assertEqual(node.__repr__(),expected)

    # def test_to_html_error(self):
    #     node = LeafNode()
    #     self.assertRaises(ValueError,node.to_html)

    def test_to_html_text(self):
        node = LeafNode(value="some text")
        self.assertEqual("some text",node.to_html())
        
    def test_to_html(self):
        test_dic = {"href": "https://www.google.com"}
        node = LeafNode(tag="a",value="Click me!",props=test_dic)
        self.assertEqual(node.to_html(),'<a href="https://www.google.com">Click me!</a>')

    def test_no_attributes(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(),"<p>This is a paragraph of text.</p>")

if __name__ == "__main__":
    unittest.main()
    