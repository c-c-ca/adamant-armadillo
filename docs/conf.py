# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "adamant-armadillo"
copyright = "2026, Adam Carter"
author = "Adam Carter"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "multiproject",
    "sphinx.ext.autodoc",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

if os.environ.get("READTHEDOCS") == "True":
    from pathlib import Path
    from multiproject.utils import get_project

    PROJECT_ROOT = Path(__file__).resolve().parent.parent

    multiproject_projects = {
        "adamant_armadillo_core": {
            "path": PROJECT_ROOT / "libs" / "adamant-armadillo-core" / "docs",
        },
        "adamant_armadillo_domain": {
            "path": PROJECT_ROOT / "libs" / "adamant-armadillo-domain" / "docs",
        },
    }

    current_project = get_project(multiproject_projects)

    if current_project == "adamant_armadillo_core":
        language = "en"
        extensions += ["sphinx.ext.autodoc"]
        project = "Core Library Documentation"
    elif current_project == "adamant_armadillo_domain":
        language = "en"
        extensions += ["sphinx.ext.autodoc"]
        project = "Domain Library documentation"
