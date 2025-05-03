import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
  def test_props_to_html1(self):
    node = HTMLNode("a", "boot-dev", None, {"href": "https://boot.dev"})
    self.assertEqual(node.props_to_html(), "href=\"https://boot.dev\"")

  def test_props_to_html2(self):
    node = HTMLNode("p", "boot-dev", None, {})
    self.assertEqual(node.props_to_html(), "")

  def test_props_to_html2(self):
    node = HTMLNode("img", None, None, {"src": "https://cool.image", "width": 300, "height": 200})
    self.assertEqual(node.props_to_html(), "src=\"https://cool.image\" width=\"300\" height=\"200\"")

if __name__ == "__main__":
  unittest.main()
