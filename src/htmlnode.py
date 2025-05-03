from typing import Dict, List, Optional


class HTMLNode():
  def __init__(
    self,
    tag: Optional[str] = None,
    value: Optional[str] = None,
    children: Optional[List["HTMLNode"]] = None,
    props: Optional[Dict[str, str]] = None,
  ):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self) -> str:
    raise NotImplementedError

  def props_to_html(self) -> str:
    if not self.props: return ""

    attributes: List[str] = []

    for key in self.props:
      attributes.append(f"{key}=\"{self.props[key]}\"")

    return " ".join(attributes)

  def __repr__(self) -> str:
    return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
