from leafnode import LeafNode
from parentnode import ParentNode
import unittest


class TestHTMLNode(unittest.TestCase):
  def test_to_html1(self):
    node = ParentNode(
      "p",
      [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
      ],
    )
    self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

  def test_to_html2(self):
    node = ParentNode("div", [LeafNode("span", "child")])
    self.assertEqual(node.to_html(), "<div><span>child</span></div>")

  def test_to_html3(self):
    node = ParentNode("div", [ParentNode("span", [LeafNode("b", "grandchild")])])
    self.assertEqual(node.to_html(), "<div><span><b>grandchild</b></span></div>")

  def test_to_html4(self):
    node = ParentNode("div", [ParentNode("a", [LeafNode("b", "grandchild")], {"href": "https://google.com"})], {"height": "auto"})
    self.assertEqual(node.to_html(), "<div height=\"auto\"><a href=\"https://google.com\"><b>grandchild</b></a></div>")


if __name__ == "__main__":
  unittest.main()
