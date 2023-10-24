import os
import sys

sys.path.insert(0, os.path.abspath("../.."))
project = 'PhotoApp'
copyright = '2023, Revuka Oleksandr, Artem Ivanina, Oleksandr Shevchenko, Evgeny Kulyk'
author = 'Revuka Oleksandr, Artem Ivanina, Oleksandr Shevchenko, Evgeny Kulyk'
release = '0.1'

extensions = ["sphinx.ext.autodoc"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


html_theme = "classic"
html_static_path = ["_static"]
