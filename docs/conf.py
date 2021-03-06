import os
import sys

sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath(".."))
sys.path.insert(0, os.path.abspath("../"))

project = "pokelance"
copyright = "2022, sarthak-py"
author = "sarthak-py"

release = __import__("pokelance.__init__").__version__

extensions = [
    "myst_parser",
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.coverage",
]

templates_path = ["_templates"]

exclude_patterns = []
html_theme = "furo"  # "sphinx_rtd_theme"
html_static_path = []
source_suffix = [".rst", ".md"]
