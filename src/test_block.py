import unittest
from block import block_to_block_type, BlockType, markdown_to_blocks


class TestHTMLNode(unittest.TestCase):
  def test_markdown_to_blocks1(self):
    blocks = markdown_to_blocks(
      "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and _italic_ words inside of it.\n\n- This is the first list item in a list block\n- This is a list item\n- This is another list item"
    )

    self.assertListEqual([
      "# This is a heading",
      "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
      "- This is the first list item in a list block\n- This is a list item\n- This is another list item",
    ], blocks)

  def test_markdown_to_blocks2(self):
    blocks = markdown_to_blocks(
      "This is **bolded** paragraph\n\n\n\nThis is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line\n\n- This is a list\n- with items"
    )
    self.assertEqual([
      "This is **bolded** paragraph",
      "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
      "- This is a list\n- with items",
    ], blocks)

  def test_block_to_block_type1(self):
    block_type = block_to_block_type(
      "1. First item\n2. Second item\n3. Third item"
    )
    self.assertEqual(block_type, BlockType.ORDERED_LIST)

  def test_block_to_block_type2(self):
    block_type = block_to_block_type(
      "### This is a third level heading"
    )
    self.assertEqual(block_type, BlockType.HEADING)

  def test_block_to_block_type3(self):
    block_type = block_to_block_type(
      "> This is cool shit\n> No, this is bad\n> It makes sense ig"
    )
    self.assertEqual(block_type, BlockType.QUOTE)

  def test_block_to_block_type4(self):
    block_type = block_to_block_type(
      "Random normal good old paragraph for normies.\n Nothing cool is going on here"
    )
    self.assertEqual(block_type, BlockType.PARAGRAPH)

  def test_block_to_block_type5(self):
    block_type = block_to_block_type(
      "- Dog\n- Cat\n- Demogorgon"
    )
    self.assertEqual(block_type, BlockType.UNORDERED_LIST)

  def test_block_to_block_type6(self):
    block_type = block_to_block_type(
      "```\nCauses the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as many repetitions as possible.\n```"
    )
    self.assertEqual(block_type, BlockType.CODE)


if __name__ == "__main__":
  unittest.main()
