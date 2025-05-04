import re
from typing import List, Tuple


def extract_markdown_images(text: str) -> List[Tuple[str]]:
  pattern = r"!\[(.*?)\]\((.+?)\)"
  return re.findall(pattern, text)


def extract_markdown_links(text: str) -> List[Tuple[str]]:
  pattern = r"(?<!\!)\[(.+?)\]\((.+?)\)"
  return re.findall(pattern, text)


def extract_title(markdown: str) -> str:
  res: List[str] = re.findall(r"^# (.*)$", markdown, flags = re.MULTILINE)
  if not res:
    raise ValueError("there must be at least one primary header")
  return res[0]
