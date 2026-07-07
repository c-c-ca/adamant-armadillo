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