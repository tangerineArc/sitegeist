from htmlnode import HTMLNode
from typing import Dict, Optional


class LeafNode(HTMLNode):
  def __init__(
    self,
    tag: Optional[str],
    value: str,
    props: Optional[Dict[str, str]] = None
  ):
    super().__init__(tag, value, None, props)

  def to_html(self) -> str:
    if self.value == None:
      raise ValueError("all leaf nodes must have a value")

    if not self.tag:
      return self.value

    attributes = self.props_to_html()

    if attributes and self.tag == "img":
      return f"<img {attributes}>"
    if attributes:
      return f"<{self.tag} {attributes}>{self.value}</{self.tag}>"
    if self.tag == "img":
      return f"<img>"

    return f"<{self.tag}>{self.value}</{self.tag}>"
