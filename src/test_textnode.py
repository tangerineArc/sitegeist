import unittest
from textnode import split_nodes_delimiter, TextNode, text_node_to_html_node, TextType


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

  def test_split1(self):
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertEqual(new_nodes, [
      TextNode("This is text with a ", TextType.TEXT),
      TextNode("code block", TextType.CODE),
      TextNode(" word", TextType.TEXT),
    ])

  def test_split2(self):
    node1 = TextNode("This is text with a `code block` word", TextType.TEXT)
    node2 = TextNode("code block", TextType.CODE)
    node3 = TextNode("`code` and `block`", TextType.TEXT)
    node4 = TextNode("_code_ and _block_", TextType.TEXT)
    node5 = TextNode("_code_", TextType.ITALIC)

    new_nodes = split_nodes_delimiter([node1, node2, node3, node4, node5], "`", TextType.CODE)
    self.assertEqual(new_nodes, [
      TextNode("This is text with a ", TextType.TEXT),
      TextNode("code block", TextType.CODE),
      TextNode(" word", TextType.TEXT),
      TextNode("code block", TextType.CODE),
      TextNode("code", TextType.CODE),
      TextNode(" and ", TextType.TEXT),
      TextNode("block", TextType.CODE),
      TextNode("_code_ and _block_", TextType.TEXT),
      TextNode("_code_", TextType.ITALIC),
    ])

  def test_split3(self):
    nodes1 = [TextNode("This is **bold _cool_ text** with a `code block` word", TextType.TEXT)]

    nodes2 = split_nodes_delimiter(nodes1, "`", TextType.CODE)
    self.assertEqual(nodes2, [
      TextNode("This is **bold _cool_ text** with a ", TextType.TEXT),
      TextNode("code block", TextType.CODE),
      TextNode(" word", TextType.TEXT)
    ])

    nodes3 = split_nodes_delimiter(nodes2, "**", TextType.BOLD)
    self.assertEqual(nodes3, [
      TextNode("This is ", TextType.TEXT),
      TextNode("bold _cool_ text", TextType.BOLD),
      TextNode(" with a ", TextType.TEXT),
      TextNode("code block", TextType.CODE),
      TextNode(" word", TextType.TEXT)
    ])

    nodes4 = split_nodes_delimiter(nodes3, "_", TextType.ITALIC)
    self.assertEqual(nodes4, [
      TextNode("This is ", TextType.TEXT),
      TextNode("bold _cool_ text", TextType.BOLD),
      TextNode(" with a ", TextType.TEXT),
      TextNode("code block", TextType.CODE),
      TextNode(" word", TextType.TEXT)
    ])


if __name__ == "__main__":
  unittest.main()
