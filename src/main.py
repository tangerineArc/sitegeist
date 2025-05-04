import os
import shutil


def main():
  generate_public_contents()


def generate_public_contents():
  source_path = os.path.join("static")
  destination_path = os.path.join("public")

  if os.path.exists(destination_path):
    shutil.rmtree(destination_path)

  os.mkdir(destination_path)

  copy_files(source_path, destination_path)


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


if __name__ == "__main__":
  main()
