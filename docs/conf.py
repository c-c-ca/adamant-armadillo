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
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CORE_LIB_ROOT =  PROJECT_ROOT / "libs" / "adamant-armadillo-core"
DOMAIN_LIB_ROOT = PROJECT_ROOT / "libs" / "adamant-armadillo-domain"

multiproject_projects = {
    "adamant_armadillo_core": {
        "path": PROJECT_ROOT / "libs" / "adamant-armadillo-core" / "docs",
        "use_config_file": True,
    },
    "adamant_armadillo_domain": {
        "path": PROJECT_ROOT / "libs" / "adamant-armadillo-domain"/ "docs",
        "use_config_file": True,
    },
}
