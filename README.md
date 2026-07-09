# Adamant Armadillo

A starter Python project template used as a foundation for future projects.

## Project Initialization

This project uses [uv](https://github.com/astral-sh/uv) for Python package and dependency management.

### 1. Create the Workspace

Create the initial project directory:

```bash
uv init adamant-armadillo
cd adamant-armadillo
```

### 2. Create the Core Library

```bash
uv init --lib libs/adamant-armadillo-core
```

Add Development Dependencies for Testing

```bash
cd libs/adamant-armadillo-core
uv add --dev pytest
```

Verify the Test Setup

```bash
uv run pytest
```

### 3. Create the Domain Library

```bash
uv init --lib libs/adamant-armadillo-domain
cd libs/adamant-armadillo-domain
```

Add Development Dependencies for Testing

```bash
cd libs/adamant-armadillo-domain
uv add --dev pytest
```

Verify the Test Setup

```bash
uv run pytest
```

Add the core libarary as a dependency

```bash
uv add adamant-armadillo-core
```

## Resulting Project Structure

```
adamant-armadillo/
├── libs/
│   ├── adamant-armadillo-core/
│   │   ├── pyproject.toml
│   │   └── src/
│   │
│   └── adamant-armadillo-domain/
│       ├── pyproject.toml
│       └── src/
│
├── pyproject.toml
└── README.md
```

## Configure Code Formatting

This project uses **Black** to ensure consistent code formatting across all libraries.

### 1. Install Black

Install Black as a development dependency for each library:

```bash
cd libs/adamant-armadillo-core
uv add --dev black

cd ../adamant-armadillo-domain
uv add --dev black
```

### 2. Configure Black

Add a `[tool.black]` section to each library's `pyproject.toml` (or to the workspace root if you prefer a shared configuration).

### 3. Configure the IDE

Configure PyCharm to use **Black** as the project's formatter. This ensures that code formatted from within the IDE is consistent with the project's formatting rules.

### 4. Add a Pre-commit Hook

Configure a Git pre-commit hook to automatically verify that all Python code is properly formatted before commits are created.

### 5. Add Continuous Integration Checks

Create a GitHub Actions workflow that runs Black in check mode on every pull request and push.

```bash
uv tool run black --check --verbose */**/src */**/test
```

## Configure Static Type Checking

This project uses **mypy** to perform static type checking and catch type-related issues before runtime.

### 1. Install mypy

Install mypy as a development dependency for each library:

```bash
cd libs/adamant-armadillo-core
uv add --dev mypy

cd ../adamant-armadillo-domain
uv add --dev mypy
```

### 2. Configure mypy

Configure mypy by adding a `[tool.mypy]` section to each library's `pyproject.toml` (or to the workspace root if using a shared configuration).

### 3. Configure the IDE

Configure PyCharm to use **mypy** for on-demand or automatic type checking. This helps identify type errors during development and ensures consistency with the project's type checking rules.

### 4. Add a Pre-commit Hook

Configure a Git pre-commit hook to run mypy before commits are created, preventing type errors from being committed.

### 5. Add Continuous Integration Checks

Create a GitHub Actions workflow that runs mypy on every push and pull request.

```bash
uv run mypy .
```

## Configure Linting

This project uses **Ruff** to perform fast, comprehensive linting and enforce a consistent code quality standard across all libraries.

### 1. Install Ruff

Install Ruff as a development dependency for each library:

```bash
cd libs/adamant-armadillo-core
uv add --dev ruff

cd ../adamant-armadillo-domain
uv add --dev ruff
```

### 2. Configure Ruff

Configure Ruff by adding a `[tool.ruff]` section to each library's `pyproject.toml` (or to the workspace root if using a shared configuration). Define the linting rules, enabled checks, exclusions, and any project-specific settings.

### 3. Configure the IDE

Configure PyCharm to use **Ruff** for code inspections and linting. This provides immediate feedback while developing and helps ensure code adheres to the project's linting rules.

### 4. Add a Pre-commit Hook

Configure a Git pre-commit hook to run Ruff before commits are created, preventing linting issues from being committed.

### 5. Add Continuous Integration Checks

Create a GitHub Actions workflow that runs Ruff on every push and pull request.

Verify the project passes all linting checks by running:

```bash
uv tool run ruff check .
```

## Configure Testing

This project uses **pytest** for unit testing and **pytest-cov** to measure code coverage. Together, these tools help ensure the project's functionality is thoroughly tested and that new code maintains a high level of test coverage.

### 1. Install Testing Dependencies

Install the testing dependencies for each library:

```bash
cd libs/adamant-armadillo-core
uv add --dev pytest
uv add --dev pytest-cov

cd ../adamant-armadillo-domain
uv add --dev pytest
uv add --dev pytest-cov
```

### 2. Configure pytest

Configure pytest by adding a `[tool.pytest.ini_options]` section to each library's `pyproject.toml` (or to the workspace root if using a shared configuration). Define options such as test discovery paths, verbosity, and any project-specific settings.

### 3. Configure Coverage Reporting

Configure `pytest-cov` to measure code coverage and generate reports. Define the coverage targets and reporting options appropriate for the project.

### 4. Configure the IDE

Configure PyCharm to use **pytest** as the project's test runner. This allows tests to be executed and debugged directly from the IDE.

### 5. Add Continuous Integration Checks

Create a GitHub Actions workflow that executes the test suite and verifies code coverage on every push and pull request.

Run the test suite locally:

```bash
uv run pytest
```

Run the test suite with coverage reporting:

```bash
uv run pytest --cov=. --cov-report=term-missing
```

## Configure Documentation

This project uses **Sphinx** to generate API and project documentation. Each library maintains its own documentation, while the root project aggregates the documentation into a single site using **sphinx-collections**.

### 1. Install Sphinx

Install Sphinx for the root project:

```bash
uv add --group docs sphinx
```

Initialize the documentation project:

```bash
sphinx-quickstart docs
```

Verify that the documentation builds successfully:

```bash
sphinx-build -M html docs/ docs/_build/
```

---

## Configure Documentation for the Core Library

Navigate to the core library:

```bash
cd libs/adamant-armadillo-core
```

Install Sphinx:

```bash
uv add --group docs sphinx
```

Initialize the documentation project:

```bash
sphinx-quickstart docs
```

### Enable Automatic API Documentation

Update `docs/conf.py` to enable the `autodoc` extension:

```python
extensions = [
    "sphinx.ext.autodoc",
]
```

Generate the API reference:

```bash
sphinx-apidoc -o docs/reference/ src/adamant_armadillo_core/
```

Update `docs/index.rst`:

```rst
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   reference/modules
```

Verify the documentation builds successfully:

```bash
sphinx-build -M html docs/ docs/_build/
```

---

## Configure Documentation for the Domain Library

Navigate to the domain library:

```bash
cd ../adamant-armadillo-domain
```

Install Sphinx:

```bash
uv add --group docs sphinx
```

Initialize the documentation project:

```bash
sphinx-quickstart docs
```

### Enable Automatic API Documentation

Update `docs/conf.py`:

```python
extensions = [
    "sphinx.ext.autodoc",
]
```

Generate the API reference:

```bash
sphinx-apidoc -o docs/reference/ src/adamant_armadillo_domain/
```

Update `docs/index.rst`:

```rst
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   reference/modules
```

Verify the documentation builds successfully:

```bash
sphinx-build -M html docs/ docs/_build/
```

---

## Aggregate Documentation

Return to the workspace root:

```bash
cd ../..
```

Install **sphinx-collections**:

```bash
uv add --group docs sphinx-collections
```

Update the root `docs/conf.py`:

```python
extensions = [
    "sphinx.ext.autodoc",
    "sphinx_collections",
]

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
```

Update the root `docs/index.rst`:

```rst
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   _collections/adamant_armadillo_core/index
   _collections/adamant_armadillo_domain/index
```

Build the aggregated documentation:

```bash
sphinx-build -M html docs/ docs/_build/
```

---

## Preview the Documentation

Start a local web server from the workspace root:

```bash
py -m http.server -d docs/_build/html 9876
```

Open the documentation in your browser:

```text
http://localhost:9876
```
