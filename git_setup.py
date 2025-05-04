#!/usr/bin/env python3
"""
Git Repository Setup Script

This script automates the process of:
1. Initializing a Git repository
2. Creating a Python-specific .gitignore file
3. Making an initial commit
4. Publishing the repository to GitHub

Works on both Windows and Mac OS.
"""

import os
import platform
import subprocess
import sys
from pathlib import Path


def run_command(command, description=None):
    """Run a shell command and print its output."""
    if description:
        print(f"\n{description}...")

    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if result.stdout.strip():
            print(result.stdout.strip())
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        if e.stderr:
            print(f"Details: {e.stderr.strip()}")
        return False, e.stderr


def check_git_installed():
    """Check if Git is installed."""
    return run_command("git --version", "Checking Git installation")[0]


def initialize_git_repo():
    """Initialize a new Git repository."""
    return run_command("git init", "Initializing Git repository")[0]


def create_python_gitignore():
    """Create a Python .gitignore file with common Python patterns."""
    gitignore_content = """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
Pipfile.lock

# poetry
poetry.lock

# pdm
.pdm.toml
__pypackages__/

# PEP 582
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# VS Code settings
.vscode/
"""

    try:
        with open(".gitignore", "w") as f:
            f.write(gitignore_content)
        print("Created .gitignore file with Python patterns")
        return True
    except Exception as e:
        print(f"Error creating .gitignore: {e}")
        return False


def make_initial_commit():
    """Add all files and make an initial commit."""
    success1, _ = run_command("git add .", "Adding files to Git")
    if not success1:
        return False

    success2, _ = run_command(
        'git commit -m "Initial commit"', "Creating initial commit"
    )
    return success2


def setup_github_remote(repo_name=None):
    """Set up GitHub remote repository."""
    if not repo_name:
        # Use current folder name as repository name if not specified
        repo_name = os.path.basename(os.getcwd())
        repo_name = (
            input(f"Enter GitHub repository name (default: {repo_name}): ") or repo_name
        )

    # Check if user has GitHub CLI installed
    success, output = run_command("gh --version", "Checking for GitHub CLI")

    if success:
        print("\nUsing GitHub CLI to create and push to repository...")
        # GitHub CLI is available, use it for a smoother experience
        return run_command(
            f"gh repo create {repo_name} --source=. --public --push",
            "Creating and pushing to GitHub repository",
        )[0]
    else:
        # Manual GitHub setup
        print("\nGitHub CLI not found. Setting up GitHub manually...")
        print("Please create a new repository on GitHub first:")
        print(f"1. Go to https://github.com/new")
        print(f"2. Name your repository: {repo_name}")
        print("3. Do NOT initialize with README, license, or gitignore")
        print("4. Click 'Create repository'")

        input("\nPress Enter after you've created the repository...")

        # Get GitHub username
        github_username = input("Enter your GitHub username: ")

        # Set up the remote and push
        remote_url = f"https://github.com/{github_username}/{repo_name}.git"
        success1, _ = run_command(
            f"git remote add origin {remote_url}", "Setting up GitHub remote"
        )
        if not success1:
            return False

        success2, _ = run_command(
            "git push -u origin main || git push -u origin master", "Pushing to GitHub"
        )
        return success2


def main():
    """Main function to run the script."""
    print("=" * 60)
    print("Git Repository Setup Script")
    print("=" * 60)

    # Check if Git is installed
    if not check_git_installed():
        print("Git is not installed. Please install Git and try again.")
        sys.exit(1)

    # Initialize Git repo
    if not initialize_git_repo():
        print("Failed to initialize Git repository. Exiting.")
        sys.exit(1)

    # Create .gitignore for Python
    if not create_python_gitignore():
        print("Failed to create .gitignore. Exiting.")
        sys.exit(1)

    # Make initial commit
    if not make_initial_commit():
        print("Failed to make initial commit. Exiting.")
        sys.exit(1)

    # Ask if user wants to publish to GitHub
    publish = input(
        "\nDo you want to publish this repository to GitHub? (y/n): "
    ).lower()
    if publish == "y" or publish == "yes":
        # Setup GitHub remote and push
        if not setup_github_remote():
            print("Failed to publish to GitHub.")
            print("You can manually push this repository later.")
    else:
        print("\nRepository initialized locally. You can push to GitHub later.")

    print("\nSetup complete!")
    print("\nUseful Git commands:")
    print("  git status                 - Check repository status")
    print("  git add <file>             - Stage specific files")
    print("  git add .                  - Stage all changes")
    print('  git commit -m "message"    - Commit with a message')
    print("  git push                   - Push to remote repository")
    print("  git pull                   - Pull from remote repository")


if __name__ == "__main__":
    main()
