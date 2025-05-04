import unittest
from utils import extract_markdown_images, extract_markdown_links, extract_title


class TestHTMLNode(unittest.TestCase):
  def test_images1(self):
    matches = extract_markdown_images(
      "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

  def test_images2(self):
    matches = extract_markdown_images(
      "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    )
    self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)

  def test_links1(self):
    matches = extract_markdown_links(
      "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    )
    self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

  def test_links2(self):
    matches = extract_markdown_links(
      "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    )
    self.assertListEqual([], matches)

  def test_extract_title1(self):
    matches = extract_title("# Hello")
    self.assertEqual("Hello", matches)

  def test_extract_title2(self):
    matches = extract_title("# Tolkien Fan Club\n\n![JRR Tolkien sitting](/images/tolkien.png)\n\nHere's the deal, **I like Tolkien**.")
    self.assertEqual("Tolkien Fan Club", matches)

  def test_extract_title3(self):
    matches = extract_title("Tolkien Fan Club\n\n![JRR Tolkien sitting](/images/tolkien.png)\n\n# Here's the deal, **I like Tolkien**.")
    self.assertEqual("Here's the deal, **I like Tolkien**.", matches)

  def test_extract_title4(self):
    with self.assertRaises(ValueError):
      extract_title("Tolkien Fan Club\n\n![JRR Tolkien sitting](/images/tolkien.png)\n\nOkay # Here's the deal, **I like Tolkien**.")

if __name__ == "__main__":
  unittest.main()
