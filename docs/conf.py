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
    "sphinx.ext.autodoc",
    "sphinx_collections",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

collections = {
    "adamant_armadillo_core": {
        "driver": "symlink",
        "source": "../libs/adamant-armadillo-core/docs/",
    },
    "adamant_armadillo_domain": {
        "driver": "symlink",
        "source": "../libs/adamant-armadillo-domain/docs/",
    },
}

if os.environ.get("READTHEDOCS") == "True":
    from pathlib import Path

    PROJECT_ROOT = Path(__file__).parent.parent
    CORE_LIB_ROOT = PROJECT_ROOT / "lib" / "adamant-armadillo-core" / "src" / "adamant_armadillo_core"
    DOMAIN_LIB_ROOT = PROJECT_ROOT / "lib" / "adamant-armadillo-domain" / "src" / "adamant_armadillo_domain"

    def run_apidoc(_):
        from sphinx.ext import apidoc

        apidoc.main(
            [
                "--force",
                "--implicit-namespaces",
                "--module-first",
                "--separate",
                "-o",
                str(PROJECT_ROOT / "docs" / "reference"),
                str(CORE_LIB_ROOT),
            ]
        )

        apidoc.main(
            [
                "--force",
                "--implicit-namespaces",
                "--module-first",
                "--separate",
                "-o",
                str(PROJECT_ROOT / "docs" / "reference"),
                str(DOMAIN_LIB_ROOT),
            ]
        )

    def setup(app):
        app.connect("builder-inited", run_apidoc)
