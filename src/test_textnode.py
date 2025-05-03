import unittest
from textnode import TextNode, TextType


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


if __name__ == "__main__":
  unittest.main()
