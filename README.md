# Sitegeist • Static Site Generator

Sitegeist is a fully custom, performance-first static site generator built from scratch in Python. Inspired by tools like Hugo and Jekyll, it turns your Markdown and HTML into a static website. Comes with zero runtime bloat and total control.

## Features

- A recursive node system to build HTML from markdown files
- Support for inline elements (like _emphasis_ and `code`) and full block-level Markdown
- Simple directory-based routing system to connect the webpages
- A final publishing step that builds your site structure from scratch


## Tech Stack

- **Python** - the programming language for non-programmers
- **No dependencies** – just the Python standard library :)
- **Markdown** - the internet’s favorite flavor of plain text
- **HTML** - the old bones of the modern web
- **CSS** - for custom themes

## Repo Structure

- `content/` - the site markdown files go here
- `docs/` - contains the generated HTML, CSS and assets
- `src/`
  - `main.py` - main driver code for generation of pages
  - `block.py` - type definition and conversion logic for block-level markdown
  - `textnode.py` - type definition and conversion logic for text and inline elements
  - `htmlnode.py` - superclass for HTML nodes
  - `parentnode.py` - class definition and logic for HTML parent node elements
  - `leafnode.py` - class definition and logic for HTML leaf node elements
  - `utils.py` - utilities for title, image and link extraction and parsing
  - `test_*.py` - corresponding `unittest` test files
- `static/` - the CSS styles and images go here
- `build.sh` - build the site for production
- `main.sh` - build and serve the site for dev
- `template.html` - HTML layout boilerplate
- `test.sh` - run the test suite for development

## Setup and Usage

### Prerequisites

- Python 3.10+ installed
- Access to a unix-like shell (e.g. zsh or bash)

### Steps

1. Clone this repository and navigate to it:

    ```bash
    git clone git@github.com:tangerineArc/sitegeist.git
    cd sitegeist
    ```

2. The repo comes with a pre-built site. Build and serve the site to ensure that everything works fine:

    ```bash
    chmod u+x main.sh
    ./main.sh
    ```
    The site would be available at `http://127.0.0.1:8888/`

    > You might get a `FileNotFoundError`. This is caused due to the absence of a `favicon.ico` file. Add a favicon to `static/` and restart the server if you want to get rid of this error.

3. To only build the site:

    ```bash
    chmod u+x build.sh
    ./build.sh
    ```

### How to use my own content?

1. Drop your markdown files in the content directory. You can create multiple nested directories within for routing, but each directory must contain exactly 1 markdown file. Each markdown file must be named `index.md`.

2. Drop any assets such as images or PDFs inside the `static/` directory. You can organize different filetypes in different directories inside `static` if you wish.

3. Also drop your CSS files in `static/` for styling and theming.

4. Ensure to keep your URLs in the markdown as well as `template.html` consistent with the directory structure.
