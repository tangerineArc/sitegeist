from enum import Enum
import re
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

  lines = list(map(
    lambda line: line.strip(), markdown_block.split("\n")
  ))

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
