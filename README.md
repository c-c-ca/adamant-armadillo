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