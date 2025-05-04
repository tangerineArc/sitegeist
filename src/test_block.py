import unittest
from block import block_to_block_type, BlockType, markdown_to_blocks, markdown_to_html_node


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

  def test_markdown_to_html_node1(self):
    md = "This is **bolded** paragraph\ntext in a p\ntag here\n\nThis is another paragraph with _italic_ text and `code` here\n\n"

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
      html,
      "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

  def test_markdown_to_html_node2(self):
    md = "```\nThis is text that _should_ remain\nthe **same** even with inline stuff\n```"

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
      html,
      "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )

  def test_markdown_to_html_node3(self):
    md = "> The quarterly results look great!\n> Revenue was off the chart.\n> Profits were higher than ever.\n> _Everything_ is going according to **plan**."

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(html, "<div><blockquote>The quarterly results look great! Revenue was off the chart. Profits were higher than ever. <i>Everything</i> is going according to <b>plan</b>.</blockquote></div>")

  def test_markdown_to_html_node4(self):
    md = "- cool thing\n- dog\n- cat\n- demo-dog"

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(html, "<div><ul><li>cool thing</li><li>dog</li><li>cat</li><li>demo-dog</li></ul></div>")

  def test_markdown_to_html_node5(self):
    md = "1. cool thing\n2. dog3\n3. cat and hay\n4. demo-dog"

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(html, "<div><ol><li>cool thing</li><li>dog3</li><li>cat and hay</li><li>demo-dog</li></ol></div>")


if __name__ == "__main__":
  unittest.main()
