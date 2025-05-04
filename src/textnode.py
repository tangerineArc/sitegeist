from enum import Enum
from leafnode import LeafNode
from typing import List, Optional
from utils import extract_markdown_images, extract_markdown_links


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
  ):
    self.text = text
    self.text_type = text_type
    self.url = url

  def __eq__(self, other: "TextNode"):
    return (
      self.text == other.text and
      self.text_type == other.text_type and
      self.url == other.url
    )

  def __repr__(self):
    return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


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
      return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
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


def split_nodes_image(old_nodes: List[TextNode]) -> List[TextNode]:
  new_nodes: List[TextNode] = []

  for node in old_nodes:
    text = node.text

    if node.text_type == TextType.TEXT:
      images = extract_markdown_images(text)

      for image_alt, image_link in images:
        parts = text.split(f"![{image_alt}]({image_link})", 1)

        text = parts[1]
        new_nodes.append(TextNode(parts[0], TextType.TEXT))
        new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))

      if text:
        new_nodes.append(TextNode(text, TextType.TEXT))
    else:
      new_nodes.append(node)

  return new_nodes


def split_nodes_link(old_nodes: List[TextNode]) -> List[TextNode]:
  new_nodes: List[TextNode] = []

  for node in old_nodes:
    text = node.text

    if node.text_type == TextType.TEXT:
      links = extract_markdown_links(text)

      for link_text, link_ref in links:
        parts = text.split(f"[{link_text}]({link_ref})", 1)

        text = parts[1]
        new_nodes.append(TextNode(parts[0], TextType.TEXT))
        new_nodes.append(TextNode(link_text, TextType.LINK, link_ref))

      if text:
        new_nodes.append(TextNode(text, TextType.TEXT))
    else:
      new_nodes.append(node)

  return new_nodes


def text_to_textnodes(text: str) -> List[TextNode]:
  text_node = TextNode(text, TextType.TEXT)

  nodes1 = split_nodes_delimiter([text_node], "**", TextType.BOLD)
  nodes2 = split_nodes_delimiter(nodes1, "_", TextType.ITALIC)
  nodes3 = split_nodes_delimiter(nodes2, "`", TextType.CODE)

  nodes4 = split_nodes_link(nodes3)
  nodes5 = split_nodes_image(nodes4)

  return nodes5
