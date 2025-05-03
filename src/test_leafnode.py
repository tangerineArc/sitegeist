from leafnode import LeafNode
import unittest


class TestHTMLNode(unittest.TestCase):
  def test_to_html1(self):
    node = LeafNode("p", "This is a paragraph of text.")
    self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

  def test_to_html2(self):
    node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

  def test_to_html3(self):
    node = LeafNode(None, "Plain text")
    self.assertEqual(node.to_html(), "Plain text")

  def test_to_html4(self):
    node = LeafNode(None, None)
    self.assertRaises(ValueError)

if __name__ == "__main__":
  unittest.main()
