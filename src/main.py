from block import markdown_to_html_node
import os
import shutil
from utils import extract_title


def main():
  source_path = os.path.join("static")
  destination_path = os.path.join("public")

  if os.path.exists(destination_path):
    shutil.rmtree(destination_path)

  os.mkdir(destination_path)

  copy_files(source_path, destination_path)

  input_file_path = os.path.join("content", "index.md")
  template_file_path = os.path.join("template.html")
  output_file_path = os.path.join(destination_path, "index.html")

  generate_page(input_file_path, template_file_path, output_file_path)


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


def generate_page(from_path: str, template_path: str, dest_path: str):
  print(f"Generating page from {from_path} to {dest_path} using {template_path}...")

  with open(from_path, "r") as md_file:
    markdown = md_file.read()

  with open(template_path, "r") as template_file:
    template = template_file.read()

  html = markdown_to_html_node(markdown).to_html()
  page_title = extract_title(markdown)

  template = template.replace("{{ Title }}", page_title)
  template = template.replace("{{ Content }}", html)

  with open(dest_path, "w") as html_file:
    html_file.write(template)


if __name__ == "__main__":
  main()
