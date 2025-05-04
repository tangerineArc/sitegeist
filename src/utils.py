import re
from typing import List, Tuple


def extract_markdown_images(text: str) -> List[Tuple[str]]:
  pattern = r"!\[(.*?)\]\((.+?)\)"
  return re.findall(pattern, text)


def extract_markdown_links(text: str) -> List[Tuple[str]]:
  pattern = r"[^!]\[(.*?)\]\((.+?)\)"
  return re.findall(pattern, text)
