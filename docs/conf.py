import re
import sys
import os


project = "nextcord-ext-ipc"
copyright = "2021, nextcord"
author = "nextcord"

sys.path.insert(0, os.path.abspath(".."))

_version_regex = r"^version = ('|\")((?:[0-9]+\.)*[0-9]+(?:\.?([a-z]+)(?:\.?[0-9])?)?)\1$"

with open("../nextcord/ext/ipc/__init__.py") as stream:
    match = re.search(_version_regex, stream.read(), re.MULTILINE)

version = match.group(2)

if match.group(3) is not None:
    try:
        import subprocess

        process = subprocess.Popen(["git", "rev-list", "--count", "HEAD"], stdout=subprocess.PIPE)
        out, _ = process.communicate()
        if out:
            version += out.decode("utf-8").strip()

        process = subprocess.Popen(["git", "rev-parse", "--short", "HEAD"], stdout=subprocess.PIPE)
        out, _ = process.communicate()
        if out:
            version += "+g" + out.decode("utf-8").strip()
    except (Exception) as e:
        pass

release = version


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx_book_theme",
    "sphinxcontrib_trio",
]


autodoc_typehints = "none"

intersphinx_mapping = {
    "aiohttp": ("https://docs.aiohttp.org/en/stable/", None),
    "python": ("https://docs.python.org/3", None),
    "nextcord": ("https://docs.nextcord.dev/en/stable", None),
}

highlight_language = "python3"
html_theme = "sphinx_book_theme"
master_doc = "index"
pygments_style = "friendly"
source_suffix = ".rst"

html_title = "nextcord-ext-ipc"

html_theme_options = {
    "repository_url": "https://github.com/nextcord/nextcord-ext-ipc",
    "path_to_docs": "docs",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
}

html_static_path = ["_static"]


def uncached(directory, files):
    """Append last modified date to filenames in order to prevent caching old versions"""
    return [
        f'{directory}/{filename}?v={os.path.getmtime(os.path.join("_static", directory, filename))}'
        for filename in files
    ]


html_css_files = uncached("css", ["custom.css"])

html_js_files = uncached("js", ["darkreader.min.js", "toggleDarkMode.js"])
