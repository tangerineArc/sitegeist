import unittest
from textnode import TextNode, text_node_to_html_node, TextType


class TestTextNode(unittest.TestCase):
  def test_eq1(self):
    node1 = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertEqual(node1, node2)

  def test_eq2(self):
    node1 = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a different text node", TextType.BOLD)
    self.assertNotEqual(node1, node2)

  def test_eq3(self):
    node1 = TextNode("This is a text node", TextType.ITALIC)
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertNotEqual(node1, node2)

  def test_eq4(self):
    node1 = TextNode("This is a text node", TextType.LINK, "https://tangerine.me")
    node2 = TextNode("This is a text node", TextType.CODE)
    self.assertNotEqual(node1, node2)

  def test_text1(self):
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")

  def test_text2(self):
    node = TextNode("This is a bold text node", TextType.BOLD)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "b")
    self.assertEqual(html_node.value, "This is a bold text node")

  def test_text3(self):
    node = TextNode("", TextType.IMAGE, "https://cool-image.com", "cool image")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "img")
    self.assertEqual(html_node.value, "")
    self.assertEqual(html_node.to_html(), "<img src=\"https://cool-image.com\" alt=\"cool image\">")


if __name__ == "__main__":
  unittest.main()
