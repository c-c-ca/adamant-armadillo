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
    CORE_LIB_ROOT =  PROJECT_ROOT / "libs" / "adamant-armadillo-core"
    DOMAIN_LIB_ROOT = PROJECT_ROOT / "libs" / "adamant-armadillo-domain"

    multiproject_projects = {
        "adamant_armadillo_core": {
            "path": CORE_LIB_ROOT / "docs",
        },
        "adamant_armadillo_domain": {
            "path": DOMAIN_LIB_ROOT/ "docs",
        },
    }

    current_project = get_project(multiproject_projects)

    if current_project == "adamant_armadillo_core":
        language = "en"
        extensions += ["sphinx.ext.autodoc"]
        project = "Core Library Documentation"
        package_root = CORE_LIB_ROOT / "scr" / "adamant_armadillo_core"
    elif current_project == "adamant_armadillo_domain":
        language = "en"
        extensions += ["sphinx.ext.autodoc"]
        project = "Domain Library documentation"
        package_root = DOMAIN_LIB_ROOT / "scr" / "adamant_armadillo_domain"

    PACKAGE_ROOT = PROJECT_ROOT / "src" / current_project

    def run_apidoc(_):
        from sphinx.ext import apidoc
        apidoc.main([
            "--force",
            "--implicit-namespaces",
            "--module-first",
            "--separate",
            "-o",
            str(PROJECT_ROOT / "docs" / "reference"),
            str(package_root),
        ])

    def setup(app):
        app.connect('builder-inited', run_apidoc)