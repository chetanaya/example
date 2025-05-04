#!/usr/bin/env python3
"""
Git Workflow Management Script

This script helps manage Git workflows with best practices:
1. Initializing a Git repository
2. Creating a Python-specific .gitignore file
3. Making commits with meaningful messages
4. Publishing the repository to GitHub
5. Supporting branch-based development
6. Checking login status and authentication

Works on both Windows and Mac OS.
"""

import os
import platform
import subprocess
import sys
import re
from pathlib import Path
from typing import Tuple, List, Optional, Dict


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


def check_github_cli_installed():
    """Check if GitHub CLI is installed."""
    return run_command("gh --version", "Checking for GitHub CLI")[0]


def check_github_logged_in():
    """Check if user is logged in to GitHub."""
    if check_github_cli_installed():
        # Try modern GitHub CLI command first
        success, output = run_command("gh auth status 2>/dev/null", None)
        if success and "Logged in to" in output:
            return True

        # Try alternative GitHub CLI commands if the first one fails
        # GitHub CLI might have different command structure in some versions
        success, output = run_command("gh api user 2>/dev/null", None)
        if success:
            return True

        # Try another alternative command
        success, output = run_command("gh user status 2>/dev/null", None)
        if success:
            return True

        print("GitHub CLI is installed but couldn't verify login status.")
        print(
            "This might be due to different GitHub CLI versions or authentication issues."
        )

    # Fall back to checking Git config as a backup method
    print("Checking Git configuration for user identity...")
    success, output = run_command("git config --get user.name", None)
    success2, output2 = run_command("git config --get user.email", None)
    return success and success2 and output.strip() and output2.strip()


def github_login():
    """Log in to GitHub."""
    if check_github_cli_installed():
        print("\nLogging in to GitHub using GitHub CLI...")
        return run_command("gh auth login", "GitHub authentication")[0]
    else:
        print("\nGitHub CLI not found. Setting up Git credentials manually...")
        username = input("Enter your GitHub username: ")
        email = input("Enter your GitHub email: ")

        success1, _ = run_command(
            f'git config --global user.name "{username}"', "Setting up Git username"
        )
        success2, _ = run_command(
            f'git config --global user.email "{email}"', "Setting up Git email"
        )

        print(
            "\nGit credentials configured. You'll need to authenticate with GitHub when pushing."
        )
        return success1 and success2


def is_git_repo():
    """Check if current directory is a Git repository."""
    return run_command("git rev-parse --is-inside-work-tree", None)[0]


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


def get_git_status() -> Tuple[List[str], List[str], List[str]]:
    """Get files that are modified, untracked, and staged."""
    success, output = run_command(
        "git status --porcelain", "Checking repository status"
    )
    if not success:
        return [], [], []

    modified = []
    untracked = []
    staged = []

    for line in output.strip().split("\n"):
        if not line:
            continue
        status = line[:2]
        file_path = line[3:]

        if status == "??":
            untracked.append(file_path)
        elif status == " M":
            modified.append(file_path)
        elif status in ["M ", "A "]:
            staged.append(file_path)
        elif status == "MM":
            # Both staged and unstaged changes
            modified.append(file_path)
            staged.append(file_path)

    return modified, untracked, staged


def get_current_branch() -> str:
    """Get the name of the current branch."""
    success, output = run_command("git rev-parse --abbrev-ref HEAD", None)
    return output.strip() if success else "unknown"


def create_branch(branch_name: str) -> bool:
    """Create and checkout a new branch."""
    return run_command(
        f"git checkout -b {branch_name}",
        f"Creating and switching to branch '{branch_name}'",
    )[0]


def checkout_branch(branch_name: str) -> bool:
    """Checkout an existing branch."""
    return run_command(
        f"git checkout {branch_name}", f"Switching to branch '{branch_name}'"
    )[0]


def list_branches() -> List[str]:
    """List all branches in the repository."""
    success, output = run_command("git branch", "Listing branches")
    if not success:
        return []

    branches = []
    for line in output.strip().split("\n"):
        if not line:
            continue
        if line.startswith("*"):
            # Current branch has an asterisk
            branches.append(line[2:])
        else:
            branches.append(line.strip())

    return branches


def generate_commit_message_template() -> str:
    """Generate a template for a good commit message."""
    return """# Write a concise and meaningful commit message (50 chars or less)
# 
# More detailed explanation, if necessary. Keep line length to 72 chars.
# Explain what and why, not how.
#
# - Bullet points are okay
#
# Related issue: (if applicable)
#
# Co-authored-by: Name <email> (if applicable)
"""


def make_initial_commit():
    """Add all files and make an initial commit."""
    success1, _ = run_command("git add .", "Adding files to Git")
    if not success1:
        return False

    success2, _ = run_command(
        'git commit -m "Initial commit"', "Creating initial commit"
    )
    return success2


def choose_files_to_add() -> List[str]:
    """Let user choose which files to add."""
    modified, untracked, staged = get_git_status()
    all_files = modified + untracked

    if not all_files:
        print("No changes detected.")
        return []

    print("\nChanges detected:")

    if modified:
        print("\nModified files:")
        for i, file in enumerate(modified):
            print(f"  {i + 1}. {file}")

    if untracked:
        print("\nUntracked files:")
        for i, file in enumerate(untracked, start=len(modified) + 1):
            print(f"  {i}. {file}")

    print(
        "\nChoose files to add (comma-separated numbers, 'a' for all, or 'q' to cancel):"
    )
    choice = input("> ").strip().lower()

    if choice == "q":
        return []
    elif choice == "a":
        return all_files
    else:
        try:
            indices = [int(x.strip()) - 1 for x in choice.split(",") if x.strip()]
            return [all_files[i] for i in indices if 0 <= i < len(all_files)]
        except (ValueError, IndexError):
            print("Invalid selection. No files selected.")
            return []


def commit_changes(files=None):
    """Add selected files and commit changes with a meaningful message."""
    if files is None:
        files = choose_files_to_add()

    if not files:
        print("No files selected for commit.")
        return False

    # Add selected files
    for file in files:
        success, _ = run_command(f'git add "{file}"', f"Adding {file}")
        if not success:
            print(f"Failed to add {file}")
            return False

    # Create temporary file for commit message
    import tempfile

    commit_msg_file = tempfile.NamedTemporaryFile(mode="w+", delete=False)
    commit_msg_file.write(generate_commit_message_template())
    commit_msg_file.close()

    # Open editor for commit message
    editor = os.environ.get(
        "EDITOR", "nano" if platform.system() != "Windows" else "notepad"
    )
    run_command(f"{editor} {commit_msg_file.name}", "Opening editor for commit message")

    # Read commit message
    with open(commit_msg_file.name, "r") as f:
        commit_msg_lines = [line for line in f.readlines() if not line.startswith("#")]

    commit_msg = "".join(commit_msg_lines).strip()
    if not commit_msg:
        print("Commit message is empty. Commit canceled.")
        os.unlink(commit_msg_file.name)
        return False

    # Make the commit
    success, _ = run_command(f'git commit -m "{commit_msg}"', "Committing changes")
    os.unlink(commit_msg_file.name)
    return success


def has_remote() -> bool:
    """Check if the repository has a remote set up."""
    success, output = run_command("git remote -v", None)
    return success and bool(output.strip())


def setup_github_remote(repo_name=None):
    """Set up GitHub remote repository."""
    if not repo_name:
        # Use current folder name as repository name if not specified
        repo_name = os.path.basename(os.getcwd())
        repo_name = (
            input(f"Enter GitHub repository name (default: {repo_name}): ") or repo_name
        )

    # Check if user has GitHub CLI installed
    if check_github_cli_installed():
        print("\nUsing GitHub CLI to create and push to repository...")
        visibility = input(
            "Should the repository be public or private? (public/private): "
        ).lower()
        if visibility not in ["public", "private"]:
            visibility = "public"

        return run_command(
            f"gh repo create {repo_name} --source=. --{visibility} --push",
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


def push_changes():
    """Push changes to remote repository following best practices."""
    current_branch = get_current_branch()

    if current_branch in ["main", "master"]:
        print("\n⚠️ BEST PRACTICE WARNING ⚠️")
        print("You're about to push directly to the main branch.")
        print(
            "It's generally better to work in feature branches and use pull requests."
        )
        choice = input("Continue with direct push to main? (y/n): ").lower()
        if choice != "y":
            print("Push cancelled.")
            return False

    if has_remote():
        # Check if branch exists on remote
        success, output = run_command(
            f"git ls-remote --heads origin {current_branch}", None
        )
        branch_exists = current_branch in output

        if branch_exists:
            return run_command(
                f"git push origin {current_branch}", f"Pushing to {current_branch}"
            )[0]
        else:
            return run_command(
                f"git push -u origin {current_branch}",
                f"Pushing and setting upstream for {current_branch}",
            )[0]
    else:
        print("No remote repository configured. Please set up a remote first.")
        return False


def setup_new_repository():
    """Set up a new Git repository from scratch."""
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
        # Check if logged in
        if not check_github_logged_in():
            print("You need to log in to GitHub first.")
            if not github_login():
                print("Failed to log in to GitHub. You can publish manually later.")
                return

        # Setup GitHub remote and push
        if not setup_github_remote():
            print("Failed to publish to GitHub.")
            print("You can manually push this repository later.")
    else:
        print("\nRepository initialized locally. You can push to GitHub later.")


def manage_existing_repository():
    """Manage an existing Git repository with best practices."""
    # Check current branch and status
    current_branch = get_current_branch()
    modified, untracked, staged = get_git_status()

    print(f"\nCurrent branch: {current_branch}")

    if not modified and not untracked and not staged:
        print("No changes detected. Working directory is clean.")

        # Offer to create a new branch for new work
        if current_branch in ["main", "master"]:
            create_new = input(
                "\nFollowing best practices, would you like to create a new feature branch for your work? (y/n): "
            ).lower()

            if create_new == "y":
                branch_name = input(
                    "Enter new branch name (e.g., 'feature/add-login'): "
                )
                if branch_name and create_branch(branch_name):
                    print(f"Switched to new branch '{branch_name}'")

        return

    # Have changes, ask what to do
    print("\nWhat would you like to do?")
    print("1. Commit changes")
    print("2. Create a new branch and commit changes")
    print("3. View detailed status")
    print("4. Push changes to remote")
    print("5. Exit")

    choice = input("\nEnter choice (1-5): ")

    if choice == "1":
        commit_changes()
    elif choice == "2":
        branch_name = input("Enter new branch name: ")
        if branch_name and create_branch(branch_name):
            print(f"Switched to new branch '{branch_name}'")
            commit_changes()
    elif choice == "3":
        run_command("git status", "Detailed status")
    elif choice == "4":
        push_changes()
    else:
        print("Exiting without changes.")


def show_git_tips():
    """Show helpful Git tips and best practices."""
    print("\n📝 Git Best Practices:")
    print("  • Write meaningful commit messages that describe WHY, not just WHAT")
    print("  • Commit early, commit often - make small, focused commits")
    print("  • Use feature branches for new work (never work directly on main)")
    print("  • Pull before you push to avoid merge conflicts")
    print("  • Use pull requests for code reviews")

    print("\n🛠️ Useful Git commands:")
    print("  git status                 - Check repository status")
    print("  git add <file>             - Stage specific files")
    print("  git add .                  - Stage all changes")
    print('  git commit -m "message"    - Commit with a message')
    print("  git checkout -b branch     - Create and switch to a new branch")
    print("  git push                   - Push to remote repository")
    print("  git pull                   - Pull from remote repository")
    print("  git log --oneline          - View commit history")


def main():
    """Main function to run the script."""
    print("=" * 60)
    print("Git Workflow Management Script")
    print("=" * 60)

    # Check if Git is installed
    if not check_git_installed():
        print("Git is not installed. Please install Git and try again.")
        sys.exit(1)

    # Determine if we're in an existing repo or need to set up a new one
    in_git_repo = is_git_repo()

    if not in_git_repo:
        print("No Git repository detected in the current directory.")
        initialize = input(
            "Would you like to initialize a new Git repository here? (y/n): "
        ).lower()
        if initialize == "y" or initialize == "yes":
            setup_new_repository()
        else:
            print("Exiting without changes.")
            sys.exit(0)
    else:
        # Check if logged in to GitHub
        if not check_github_logged_in():
            print("\nYou're not logged in to GitHub.")
            login = input("Would you like to log in now? (y/n): ").lower()
            if login == "y" or login == "yes":
                github_login()

        # Manage existing repository
        manage_existing_repository()

    # Show Git tips
    show_git_tips()
    print("\nDone!")


if __name__ == "__main__":
    main()
