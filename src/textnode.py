from enum import Enum
from leafnode import LeafNode
from typing import List, Optional


class TextType(Enum):
  TEXT = "text"
  BOLD = "bold"
  ITALIC = "italic"
  CODE = "code"
  LINK = "link"
  IMAGE = "image"


class TextNode():
  def __init__(
    self,
    text: str,
    text_type: TextType,
    url: Optional[str] = None,
    alt_text: Optional[str] = None,
  ):
    self.text = text
    self.text_type = text_type
    self.url = url
    self.alt_text = alt_text

  def __eq__(self, other: "TextNode"):
    return (
      self.text == other.text and
      self.text_type == other.text_type and
      self.url == other.url and
      self.alt_text == other.alt_text
    )

  def __repr__(self):
    return f"TextNode({self.text}, {self.text_type.value}, {self.url}, {self.alt_text})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
  match text_node.text_type:
    case TextType.TEXT:
      return LeafNode(None, text_node.text)
    case TextType.BOLD:
      return LeafNode("b", text_node.text)
    case TextType.ITALIC:
      return LeafNode("i", text_node.text)
    case TextType.CODE:
      return LeafNode("code", text_node.text)
    case TextType.LINK:
      return LeafNode("a", text_node.text, {"href": text_node.url})
    case TextType.IMAGE:
      return LeafNode("img", "", {"src": text_node.url, "alt": text_node.alt_text})
    case _:
      raise Exception("invalid type for text_node")


def split_nodes_delimiter(
  old_nodes: List[TextNode],
  delimiter: str,
  text_type: TextType
) -> List[TextNode]:
  new_nodes: List[TextNode] = []

  for node in old_nodes:
    if node.text_type == TextType.TEXT:
      parts = node.text.split(delimiter)

      if len(parts) % 2 == 0:
        raise Exception("invalid markdown syntax")

      for idx, part in enumerate(parts):
        if part == "": continue

        if idx % 2 == 0:
          new_nodes.append(TextNode(part, TextType.TEXT))
        else:
          new_nodes.append(TextNode(part, text_type))
    else:
      new_nodes.append(node)

  return new_nodes
