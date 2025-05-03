from typing import Dict, List


class HTMLNode():
  def __init__(
    self,
    tag = "",
    value = "",
    children: List = [],
    props: Dict[str, str] = {}
  ):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self) -> None:
    raise NotImplementedError

  def props_to_html(self) -> str:
    attributes: List[str] = []

    for key in self.props:
      attributes.append(f"{key}=\"{self.props[key]}\"")

    return " ".join(attributes)

  def __repr__(self) -> str:
    return f"HTMLNode({self.tag}, {self.value or '""'}, {self.children}, {self.props})"
