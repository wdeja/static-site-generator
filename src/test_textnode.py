import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    split_nodes_delimiter
)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text)
        self.assertEqual(node, node2)

    def test_false(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node2", text_type_bold)
        self.assertNotEqual(node, node2)
    
    def test_eq_url(self):
        node = TextNode("This is a text node", text_type_italic,"www.boot.dev")
        node2 = TextNode("This is a text node", text_type_italic,"www.boot.dev")
        self.assertEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", text_type_text,"www.boot.dev")
        self.assertEqual('TextNode(This is a text node, text, www.boot.dev)', node.__repr__())

    def test_split_nodes_delimeter(self):
        result = [
    TextNode("This is text with a ", text_type_text),
    TextNode("code block", text_type_code),
    TextNode(" word", text_type_text),
]
        node = TextNode("This is text with a `code block` word", text_type_text)
        self.assertEqual(split_nodes_delimiter([node], "`", text_type_code), result)

if __name__ == "__main__":
    unittest.main()
