from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode, TextType


def main():
  node = TextNode("bold text", TextType.BOLD)
  print(node)

  hnode = HTMLNode("img", None, None, {"src": "https://cool.image", "width": 300, "height": 200})
  print(hnode)

  lnode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
  print(lnode.to_html())

  print(ParentNode(
    "p",
    [
      LeafNode("b", "Bold text"),
      LeafNode(None, "Normal text"),
      LeafNode("i", "italic text"),
      LeafNode(None, "Normal text"),
    ],
  ).to_html())

  print(ParentNode(
    "p",
    [
      LeafNode(None, "Normal text"),
      ParentNode("span", [LeafNode("b", "grandchild")]),
      LeafNode("b", "Bold text"),
    ],
  ).to_html())


if __name__ == "__main__":
  main()
