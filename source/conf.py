# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Actuarial Package for Excel'
copyright = '2022, Corentin LEFEVRE'
author = 'Corentin LEFEVRE'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_panels' # `pip install sphinx-panels` (https://sphinx-panels.readthedocs.io/en/latest/#)
]

# Set the default role for text in back quotes like `text`.
default_role = 'py:obj' # refers to a Python object like a variable name

# Define global substitution available in all rst files
rst_prolog = """
.. |0| replace:: ⓿
.. |1| replace:: ❶
.. |2| replace:: ❷
.. |3| replace:: ❸
.. |4| replace:: ❹
.. |5| replace:: ❺
.. |6| replace:: ❻
.. |7| replace:: ❼
.. |8| replace:: ❽
.. |9| replace:: ❾

.. |none| replace:: `!`
.. |V| replace:: :opticon:`check,text-success`
.. |X| replace:: :opticon:`x,text-danger`

.. role:: subtitle
    :class: subtitle
"""

# If true, the current module name will be prepended to all description
add_module_names = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'css/custom.css', # load custom css file
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css' # load FontAwesome CSS (https://cdnjs.com/libraries/font-awesome)
]