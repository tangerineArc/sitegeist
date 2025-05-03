from textnode import TextNode, TextType
from htmlnode import HTMLNode


def main():
  node = TextNode("bold text", TextType.BOLD)
  print(node)

  hnode = HTMLNode("img", "", [], {"src": "https://cool.image", "width": 300, "height": 200})
  print(hnode)


if __name__ == "__main__":
  main()
