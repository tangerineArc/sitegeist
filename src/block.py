from enum import Enum
from htmlnode import HTMLNode
from parentnode import ParentNode
import re
from textnode import TextNode, text_node_to_html_node, text_to_textnodes, TextType
from typing import List


class BlockType(Enum):
  PARAGRAPH = "paragraph"
  HEADING = "heading"
  CODE = "code"
  QUOTE = "quote"
  UNORDERED_LIST = "unordered_list"
  ORDERED_LIST = "ordered_list"


def block_to_block_type(markdown_block: str) -> BlockType:
  if (
    markdown_block.startswith("```") and
    markdown_block.endswith("```")
  ):
    return BlockType.CODE

  if re.match(r"#{1,6} ", markdown_block):
    return BlockType.HEADING

  lines = list(filter(lambda line: line, map(
    lambda line: line.strip(), markdown_block.split("\n")
  )))

  quotes = unordered_lists = ordered_lists = 0
  for line in lines:
    if line.startswith("> "):
      quotes += 1
    elif line.startswith("- "):
      unordered_lists += 1
    elif re.match(r"\d+\. ", line):
      ordered_lists += 1

  num_lines = len(lines)
  if num_lines == quotes:
    return BlockType.QUOTE
  if num_lines == unordered_lists:
    return BlockType.UNORDERED_LIST
  if num_lines == ordered_lists:
    return BlockType.ORDERED_LIST

  return BlockType.PARAGRAPH


def markdown_to_blocks(markdown: str) -> List[str]:
  return list(filter(
    lambda block: block,
    map(lambda block: block.strip(), markdown.split("\n\n"))
  ))


def markdown_to_html_node(markdown: str) -> HTMLNode:
  markdown_blocks = markdown_to_blocks(markdown)

  parent_nodes: List[ParentNode] = []
  for markdown_block in markdown_blocks:
    block_type = block_to_block_type(markdown_block)

    match block_type:
      case BlockType.HEADING:
        marker, text = markdown_block.split(" ", 1)

        text_nodes = text_to_textnodes(text)
        leaf_nodes = list(map(text_node_to_html_node, text_nodes))

        parent_nodes.append(ParentNode(f"h{len(marker)}", leaf_nodes))

      case BlockType.CODE:
        text = re.sub(r"^```", "", markdown_block)
        text = re.sub(r"```$", "", text)
        text = text.lstrip()

        text_node = TextNode(text, TextType.CODE)
        leaf_node = text_node_to_html_node(text_node)

        parent_nodes.append(ParentNode("pre", [leaf_node]))

      case BlockType.QUOTE:
        text = re.sub(r"^> ", "", markdown_block, flags = re.MULTILINE)
        text = " ".join(text.split("\n"))

        text_nodes = text_to_textnodes(text)
        leaf_nodes = list(map(text_node_to_html_node, text_nodes))

        parent_nodes.append(ParentNode("blockquote", leaf_nodes))

      case BlockType.UNORDERED_LIST:
        text = re.sub(r"^- ", "", markdown_block, flags = re.MULTILINE)

        list_item_nodes = list(map(
          lambda line: ParentNode("li", list(map(
            text_node_to_html_node, text_to_textnodes(line)
          ))),
          text.split("\n")
        ))

        parent_nodes.append(ParentNode("ul", list_item_nodes))

      case BlockType.ORDERED_LIST:
        text = re.sub(r"^\d+\. ", "", markdown_block, flags = re.MULTILINE)

        list_item_nodes = list(map(
          lambda line: ParentNode("li", list(map(
            text_node_to_html_node, text_to_textnodes(line)
          ))),
          text.split("\n")
        ))

        parent_nodes.append(ParentNode("ol", list_item_nodes))

      case BlockType.PARAGRAPH:
        text_nodes = text_to_textnodes(" ".join(
          markdown_block.split("\n")
        ))
        leaf_nodes = list(map(text_node_to_html_node, text_nodes))

        parent_nodes.append(ParentNode("p", leaf_nodes))

  return ParentNode("div", parent_nodes)
