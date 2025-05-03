from htmlnode import HTMLNode
from typing import Dict, List, Optional


class ParentNode(HTMLNode):
  def __init__(
    self,
    tag: str,
    children: List[HTMLNode],
    props: Optional[Dict[str, str]] = None,
  ):
    super().__init__(tag, None, children, props)

  def to_html(self):
    if not self.tag:
      raise ValueError("all parent nodes must have a tag")

    if not self.children:
      raise ValueError("all parent nodes must have at least one child")

    inner_text = ""
    for child in self.children:
      inner_text += child.to_html()

    attributes = self.props_to_html()
    if attributes:
      return f"<{self.tag} {attributes}>{inner_text}</{self.tag}>"
    return f"<{self.tag}>{inner_text}</{self.tag}>"
