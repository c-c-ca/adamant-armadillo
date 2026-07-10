# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
from pathlib import Path

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "adamant-armadillo"
copyright = "2026, Adam Carter"
author = "Adam Carter"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "multiproject",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

PROJECT_ROOT = Path(__file__).resolve().parent.parent

multiproject_projects = {
    "adamant_armadillo_core": {
        "path": str(PROJECT_ROOT / "libs" / "adamant-armadillo-core" / "docs"),
        "use_config_file": True,
    },
    "adamant_armadillo_domain": {
        "path": str(PROJECT_ROOT / "libs" / "adamant-armadillo-domain"/ "docs"),
        "use_config_file": True,
    },
}
