from block import markdown_to_html_node
import os
import shutil
import sys
from utils import extract_title


def main():
  if len(sys.argv) == 1:
    basepath = "/"
  elif len(sys.argv) == 2:
    basepath = sys.argv[1]

  source_path = os.path.join("static")
  destination_path = os.path.join("docs")

  if os.path.exists(destination_path):
    shutil.rmtree(destination_path)

  os.mkdir(destination_path)

  copy_files(source_path, destination_path)

  input_file_path = os.path.join("content")
  template_file_path = os.path.join("template.html")

  generate_pages_recursive(basepath, input_file_path, template_file_path, destination_path)


def copy_files(source: str, dest: str):
  items = os.listdir(source)
  for item in items:
    source_item_path = os.path.join(source, item)
    dest_item_path = os.path.join(dest, item)

    if os.path.isfile(source_item_path):
      shutil.copy(source_item_path, dest)
    else:
      if not os.path.exists(dest_item_path):
        os.mkdir(dest_item_path)

      copy_files(source_item_path, dest_item_path)


def generate_page(
  basepath: str,
  from_path: str,
  template_path: str,
  dest_path: str
):
  print(f"Generating page from {from_path} to {dest_path} using {template_path}...")

  with open(from_path, "r") as md_file:
    markdown = md_file.read()

  with open(template_path, "r") as template_file:
    template = template_file.read()

  html = markdown_to_html_node(markdown).to_html()
  page_title = extract_title(markdown)

  template = template.replace("{{ Title }}", page_title)
  template = template.replace("{{ Content }}", html)
  template = template.replace("href=\"/", f"href=\"{basepath}")
  template = template.replace("src=\"/", f"src=\"{basepath}")

  with open(dest_path, "w") as html_file:
    html_file.write(template)


def generate_pages_recursive(
  basepath: str,
  dir_path_content: str,
  template_path: str,
  dest_dir_path: str
):
  items = os.listdir(dir_path_content)
  for item in items:
    source_item_path = os.path.join(dir_path_content, item)
    dest_item_path = os.path.join(dest_dir_path, item)

    if os.path.isfile(source_item_path):
      generate_page(basepath, source_item_path, template_path, dest_item_path.replace(".md", ".html"))
    else:
      if not os.path.exists(dest_item_path):
        os.mkdir(dest_item_path)

      generate_pages_recursive(basepath, source_item_path, template_path, dest_item_path)


if __name__ == "__main__":
  main()
