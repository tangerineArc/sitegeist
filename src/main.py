from textnode import TextNode, TextType


def main():
  node = TextNode("bold text", TextType.BOLD)
  print(node)


if __name__ == "__main__":
  main()
