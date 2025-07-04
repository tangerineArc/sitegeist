import unittest
from textnode import split_nodes_delimiter, split_nodes_image,split_nodes_link, TextNode, text_node_to_html_node, text_to_textnodes, TextType


class TestTextNode(unittest.TestCase):
  def test_eq1(self):
    node1 = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertEqual(node1, node2)

  def test_eq2(self):
    node1 = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a different text node", TextType.BOLD)
    self.assertNotEqual(node1, node2)

  def test_eq3(self):
    node1 = TextNode("This is a text node", TextType.ITALIC)
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertNotEqual(node1, node2)

  def test_eq4(self):
    node1 = TextNode("This is a text node", TextType.LINK, "https://tangerine.me")
    node2 = TextNode("This is a text node", TextType.CODE)
    self.assertNotEqual(node1, node2)

  def test_text1(self):
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")

  def test_text2(self):
    node = TextNode("This is a bold text node", TextType.BOLD)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "b")
    self.assertEqual(html_node.value, "This is a bold text node")

  def test_text3(self):
    node = TextNode("cool image", TextType.IMAGE, "https://cool-image.com")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "img")
    self.assertEqual(html_node.value, "")
    self.assertEqual(html_node.to_html(), "<img src=\"https://cool-image.com\" alt=\"cool image\">")

  def test_split1(self):
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertEqual(new_nodes, [
      TextNode("This is text with a ", TextType.TEXT),
      TextNode("code block", TextType.CODE),
      TextNode(" word", TextType.TEXT),
    ])

  def test_split2(self):
    node1 = TextNode("This is text with a `code block` word", TextType.TEXT)
    node2 = TextNode("code block", TextType.CODE)
    node3 = TextNode("`code` and `block`", TextType.TEXT)
    node4 = TextNode("_code_ and _block_", TextType.TEXT)
    node5 = TextNode("_code_", TextType.ITALIC)

    new_nodes = split_nodes_delimiter([node1, node2, node3, node4, node5], "`", TextType.CODE)
    self.assertEqual(new_nodes, [
      TextNode("This is text with a ", TextType.TEXT),
      TextNode("code block", TextType.CODE),
      TextNode(" word", TextType.TEXT),
      TextNode("code block", TextType.CODE),
      TextNode("code", TextType.CODE),
      TextNode(" and ", TextType.TEXT),
      TextNode("block", TextType.CODE),
      TextNode("_code_ and _block_", TextType.TEXT),
      TextNode("_code_", TextType.ITALIC),
    ])

  def test_split3(self):
    nodes1 = [TextNode("This is **bold _cool_ text** with a `code block` word", TextType.TEXT)]

    nodes2 = split_nodes_delimiter(nodes1, "`", TextType.CODE)
    self.assertEqual(nodes2, [
      TextNode("This is **bold _cool_ text** with a ", TextType.TEXT),
      TextNode("code block", TextType.CODE),
      TextNode(" word", TextType.TEXT)
    ])

    nodes3 = split_nodes_delimiter(nodes2, "**", TextType.BOLD)
    self.assertEqual(nodes3, [
      TextNode("This is ", TextType.TEXT),
      TextNode("bold _cool_ text", TextType.BOLD),
      TextNode(" with a ", TextType.TEXT),
      TextNode("code block", TextType.CODE),
      TextNode(" word", TextType.TEXT)
    ])

    nodes4 = split_nodes_delimiter(nodes3, "_", TextType.ITALIC)
    self.assertEqual(nodes4, [
      TextNode("This is ", TextType.TEXT),
      TextNode("bold _cool_ text", TextType.BOLD),
      TextNode(" with a ", TextType.TEXT),
      TextNode("code block", TextType.CODE),
      TextNode(" word", TextType.TEXT)
    ])

  def test_split_images(self):
    node = TextNode(
      "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png). That's it!",
      TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
      [
        TextNode("This is text with an ", TextType.TEXT),
        TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
        TextNode(" and another ", TextType.TEXT),
        TextNode(
          "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
        ),
        TextNode(". That's it!", TextType.TEXT)
      ],
      new_nodes,
    )

  def test_split_links(self):
    node = TextNode(
      "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
      TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
      [
        TextNode("This is text with a link ", TextType.TEXT),
        TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
        TextNode(" and ", TextType.TEXT),
        TextNode(
          "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
        ),
      ],
      new_nodes,
    )

  def test_text_to_nodes(self):
    new_nodes = text_to_textnodes(
      "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    )
    self.assertListEqual(
      [
        TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.TEXT),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev"),
      ],
      new_nodes,
    )


if __name__ == "__main__":
  unittest.main()
