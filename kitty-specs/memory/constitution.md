# GharGPT Backend Constitution

## Project Overview

GharGPT Backend is a scalable backend platform built using Nx monorepo for managing multiple applications and shared libraries. It provides APIs and services for the GharGPT application, focusing on modularity, reusability, and efficient development workflows.

## Monorepo Structure

This project uses Nx (v22.3.3) as the monorepo foundation with an applications-first approach. The structure allows for:

- Shared code in `libs/` (when added)
- Isolated applications in `apps/`
- Centralized configuration and tooling
- Efficient caching and task orchestration

## Technologies and Frameworks

- **Build System**: Nx with JavaScript/TypeScript support
- **Python Plugin**: @nxlv/python for Python applications
- **Dependency Management**: npm for workspace, Poetry for Python apps
- **CI/CD**: Nx Cloud integration
- **Version Control**: Git with spec-kitty for spec-driven development

## Folder Structure

```
ghargpt-backend/
├── .claudeignore          # Claude AI ignore patterns
├── .editorconfig          # Editor configuration
├── .git/                  # Git repository
├── .github/               # GitHub workflows and templates
├── .gitignore             # Git ignore rules
├── .kittify/              # Spec-kitty configuration
├── .nx/                   # Nx workspace cache and config
├── .vscode/               # VS Code settings
├── README.md              # Project documentation
├── apps/                  # Application projects
│   └── api/               # FastAPI application
│       ├── api/           # Source code
│       │   ├── __init__.py
│       │   ├── main.py    # FastAPI app entry point
│       │   └── __pycache__/
│       ├── poetry.toml    # Poetry configuration
│       ├── project.json   # Nx project configuration
│       ├── pyproject.toml # Python project metadata and dependencies
│       ├── README.md      # App-specific documentation
│       └── tests/         # Test suite
│           ├── __init__.py
│           ├── conftest.py # Pytest configuration
│           └── test_hello.py # Example tests
├── docs/                  # Documentation
│   └── images/            # Documentation images
├── ghargpt-env/           # Python virtual environment
├── kitty-specs/           # Spec-driven development artifacts
│   ├── memory/            # Shared knowledge and constitutions
│   └── [feature]/         # Feature-specific specs and tasks
├── node_modules/          # npm dependencies
├── nx.json                # Nx workspace configuration
├── package.json           # Workspace package metadata
└── package-lock.json      # npm lockfile
```

## Applications (apps/)

- **api**: FastAPI-based REST API application
  - Framework: FastAPI with Uvicorn server
  - Dependencies: Poetry-managed Python packages
  - Database: MongoDB (via Motor async driver)
  - Configuration: Pydantic settings with python-dotenv
  - Testing: pytest with coverage and HTML reports
  - Linting: flake8
  - Building: Poetry build with Nx integration

## Libraries (libs/) - Future Expansion

The `libs/` directory is reserved for shared code that can be utilized across applications:

- Common utilities
- Shared data models
- Authentication modules
- Database abstractions
- API clients

## Development Workflow

- Use Nx commands for task execution (e.g., `nx serve api`)
- Spec-kitty for feature specification and development
- Poetry for Python dependency management within apps
- Git for version control with feature branches

## Key Configuration Files

- `nx.json`: Defines workspace-wide Nx settings, inputs, and Nx Cloud ID
- `package.json`: Workspace metadata and Nx dependencies
- `apps/api/project.json`: Application-specific Nx targets and executors
- `apps/api/pyproject.toml`: Python dependencies and build configuration

## Environment and Tooling

- Python 3.10-3.12 (via Poetry)
- Node.js (for Nx and npm scripts)
- Virtual environment: `ghargpt-env/`
- Spec-kitty v0.11.1 for spec-driven development
- Nx Cloud for distributed caching and CI performance

This constitution provides the foundational context for all feature specifications in `spec.md` files, ensuring consistent understanding of the project architecture and development practices.
