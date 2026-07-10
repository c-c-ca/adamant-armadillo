# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "adamant-armadillo"
copyright = "2026, Adam Carter"
author = "Adam Carter"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.intersphinx",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

intersphinx_mapping = {
    "adamant-armadillo": (
        "https://adamant-armadillo.readthedocs.io/en/latest/",
        None,
    ),
    "adamant-armadillo-core": (
        "https://adamant-armadillo.readthedocs.io/projects/adamant-armadillo-core/en/latest/",
        None,
    ),
}

intersphinx_disabled_reftypes = ["*"]
