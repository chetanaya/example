# Git and GitHub CLI: Complete Guide

*Last Updated: May 4, 2025*

This document provides a comprehensive, step-by-step guide to using Git and GitHub CLI for effective version control management.

## Table of Contents
1. [Installation](#installation)
2. [Authentication](#authentication)
3. [Repository Setup](#repository-setup)
4. [Basic Git Operations](#basic-git-operations)
5. [Branching and Merging](#branching-and-merging)
6. [Remote Management](#remote-management)
7. [GitHub Specific Operations](#github-specific-operations)
8. [Advanced Topics](#advanced-topics)
9. [Best Practices](#best-practices)
10. [UV: Fast Python Package Manager](#uv-fast-python-package-manager)

## Installation

### Installing Git

**macOS:**
```bash
# Using Homebrew
brew install git

# Check installation
git --version
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install git
git --version
```

**Windows:**
1. Download from [git-scm.com](https://git-scm.com/download/win)
2. Run the installer with default options
3. Verify: `git --version` in Command Prompt or PowerShell

### Installing GitHub CLI

**macOS:**
```bash
brew install gh
```

**Linux:**
```bash
# For Ubuntu/Debian
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list
sudo apt update
sudo apt install gh
```

**Windows:**
```bash
winget install --id GitHub.cli
# or
scoop install gh
```

## Authentication

### Setting Up Git Identity
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Authenticating with GitHub CLI
```bash
gh auth login
```
This interactive command will:
1. Ask whether to use HTTPS or SSH (HTTPS is recommended for beginners)
2. Ask how you want to authenticate (browser is easiest)
3. Open your browser to complete authentication
4. Store credentials securely

### SSH Authentication (Alternative)
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Start the ssh-agent
eval "$(ssh-agent -s)"

# Add key to ssh-agent
ssh-add ~/.ssh/id_ed25519

# Copy public key to clipboard
pbcopy < ~/.ssh/id_ed25519.pub  # On macOS
cat ~/.ssh/id_ed25519.pub       # On Linux/Windows
```

Then add the key to your GitHub account:
1. Go to GitHub → Settings → SSH and GPG keys
2. Click "New SSH key"
3. Paste your key and save

### Credential Manager (HTTPS)
For HTTPS connections, use a credential manager:
```bash
# macOS (already configured with git)
git config --global credential.helper osxkeychain

# Windows (already included in Git for Windows)
git config --global credential.helper wincred

# Linux
git config --global credential.helper cache
```

## Repository Setup

### Initializing a New Repository
```bash
# Navigate to your project directory
cd your-project

# Initialize repository
git init
```

### Creating a .gitignore File
```bash
# Create a .gitignore file for your project type
# For Python projects:
curl https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore -o .gitignore
```

### Making the First Commit
```bash
# Stage all files
git add .

# Make initial commit
git commit -m "Initial commit"
```

### Publishing to GitHub

**Using GitHub CLI (recommended):**
```bash
# Create a new repository and push
gh repo create your-repo-name --public --source=. --push

# For private repositories:
gh repo create your-repo-name --private --source=. --push

# With more options:
gh repo create your-repo-name --description "Description of your project" --homepage "https://example.com" --private --source=. --push
```

**Using Git Commands:**
```bash
# Create repo on GitHub first, then:
git remote add origin https://github.com/username/your-repo-name.git
git branch -M main
git push -u origin main
```

## Basic Git Operations

### Checking Status
```bash
git status
```

### Staging Changes
```bash
# Stage specific file
git add filename.ext

# Stage all changes
git add .

# Stage portions of files interactively
git add -p
```

### Committing Changes
```bash
# Simple commit
git commit -m "Brief description of changes"

# Detailed commit message (opens editor)
git commit

# Stage and commit together (only for tracked files)
git commit -am "Brief description of changes"
```

### Viewing History
```bash
# See commit history
git log

# Compact view
git log --oneline

# Graphical view
git log --graph --oneline --decorate

# History for specific file
git log -- filename.ext

# Show changes in commit
git show <commit-hash>
```

### Viewing Changes
```bash
# Show unstaged changes
git diff

# Show staged changes
git diff --staged

# Compare branches
git diff branch1..branch2

# Show changes between commits
git diff <commit-hash-1>..<commit-hash-2>
```

## Branching and Merging

### Branch Management
```bash
# List all branches
git branch

# Create a new branch
git branch feature-name

# Switch to a branch
git checkout branch-name

# Create and switch in one command
git checkout -b new-branch-name

# Using the newer `switch` command
git switch branch-name
git switch -c new-branch-name  # Create and switch
```

### Merging
```bash
# First switch to the target branch (e.g., main)
git checkout main

# Then merge the feature branch into it
git merge feature-branch

# In case of conflicts, resolve them and then:
git add .
git commit
```

### Rebasing
```bash
# Rebase current branch on top of main
git checkout feature-branch
git rebase main

# Interactive rebase for cleaning up commits
git rebase -i HEAD~3  # Rebase last 3 commits
```

### Handling Merge Conflicts
1. Git will mark conflicts in files
2. Open conflicted files and look for `<<<<<<<`, `=======`, and `>>>>>>>`
3. Edit files to resolve conflicts
4. `git add` the resolved files
5. Complete the merge/rebase with `git commit` or `git rebase --continue`

## Remote Management

### Managing Remotes
```bash
# List all remotes
git remote -v

# Add a new remote
git remote add remote-name https://github.com/username/repo.git

# Change remote URL
git remote set-url origin new-url

# Remove a remote
git remote remove remote-name
```

### Fetching and Pulling
```bash
# Fetch updates from remote without merging
git fetch origin

# Pull updates from remote (fetch + merge)
git pull origin main

# Pull with rebase instead of merge
git pull --rebase origin main
```

### Pushing Changes
```bash
# Push to remote
git push origin branch-name

# Set upstream and push
git push -u origin branch-name

# Force push (use with caution!)
git push --force origin branch-name

# Force push safely
git push --force-with-lease origin branch-name
```

## GitHub Specific Operations

### Creating a Pull Request
```bash
# Using GitHub CLI
gh pr create --title "Feature title" --body "Description of changes"

# With options
gh pr create --base main --head feature-branch --reviewer username1,username2 --assignee username --label bug,enhancement
```

### Managing Pull Requests
```bash
# List pull requests
gh pr list

# Check out a pull request locally
gh pr checkout <pr-number>

# View pull request status
gh pr status

# Merge a pull request
gh pr merge <pr-number>

# With options (squash, delete branch)
gh pr merge <pr-number> --squash --delete-branch
```

### Working with Issues
```bash
# Create an issue
gh issue create --title "Issue title" --body "Issue description"

# List issues
gh issue list

# View issue
gh issue view <issue-number>

# Close issue
gh issue close <issue-number>

# Create a branch for an issue
gh issue develop <issue-number>
```

### Repository Management
```bash
# View repository info
gh repo view

# Clone your repository
gh repo clone repo-name

# Fork a repository
gh repo fork username/repo-name

# Archive a repository
gh repo archive repo-name --yes
```

## Advanced Topics

### Git Hooks
Git hooks are scripts that run automatically when certain events occur:
```bash
# Location of hooks
cd .git/hooks

# Example: Create a pre-commit hook
touch .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

### Git Submodules
```bash
# Add a submodule
git submodule add https://github.com/username/repo.git path/to/submodule

# Initialize and update submodules
git submodule update --init --recursive

# Update all submodules
git submodule update --remote
```

### Stashing Changes
```bash
# Stash current changes
git stash

# List stashes
git stash list

# Apply most recent stash
git stash apply

# Apply specific stash
git stash apply stash@{2}

# Remove most recent stash after applying
git stash pop

# Create named stash
git stash save "description of changes"

# Remove all stashes
git stash clear
```

### Rewriting History
```bash
# Change last commit
git commit --amend

# Squash commits
git rebase -i HEAD~3  # Interactive rebase last 3 commits

# Reset to commit (destructive)
git reset --hard <commit-hash>

# Undo a public commit (safe)
git revert <commit-hash>
```

### Git Worktrees
```bash
# Create a new worktree
git worktree add ../path-to-worktree branch-name

# List worktrees
git worktree list

# Remove a worktree
git worktree remove ../path-to-worktree
```

## Best Practices

### Commit Best Practices
1. **Make atomic commits**: Each commit should represent a single logical change
2. **Write meaningful commit messages**:
   - First line: 50 chars or less, concise summary
   - Leave a blank line after the summary
   - Body: Explain what and why, not how (72 chars per line)
3. **Commit often**: Smaller, focused commits are better than large changes

### Branching Model
1. **Main branch**: Always stable and deployable
2. **Feature branches**: Create for each new feature/bug
3. **Branch naming conventions**:
   - `feature/feature-name`
   - `bugfix/issue-description`
   - `hotfix/critical-issue`
   - `release/v1.0.0`

### Pull Request Guidelines
1. Keep PRs small and focused on a single issue/feature
2. Include tests and documentation updates
3. Explain the what, why, and how of your changes
4. Reference related issues using keywords ("Fixes #123")
5. Request reviews from appropriate team members

### Security Best Practices
1. Never commit sensitive data (passwords, API keys, etc.)
2. Use environment variables or secure storage solutions
3. Regularly rotate SSH/GPG keys
4. Use signed commits for verification:
   ```bash
   git config --global commit.gpgSign true
   ```

### Workflow Tips
1. Always pull before you start working
2. Rebase feature branches regularly to avoid big merge conflicts
3. Use tags for releases:
   ```bash
   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin v1.0.0
   ```
4. Set up CI/CD to automate testing and deployment

---

# UV: Fast Python Package Manager

*Added: May 4, 2025*

UV is a blazingly fast Python package installer and resolver written in Rust. It offers 10-100x speed improvements over traditional package managers like pip.

## Table of Contents
1. [Installation](#uv-installation)
2. [Project Management](#uv-project-management)
3. [Dependency Management](#uv-dependency-management)
4. [Tool Integration](#uv-tool-integration)
5. [Migration from pip/virtualenv](#migrating-to-uv)

<a name="uv-installation"></a>
## Installation

**macOS:**
```bash
# Using Homebrew (recommended)
brew install uv

# Or using curl
curl -LsSf https://astral.sh/uv/install.sh | sudo sh
```

**Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sudo sh
```

**Windows:**
```bash
# Using PowerShell (with admin privileges)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify installation:
```bash
uv version
```

<a name="uv-project-management"></a>
## Project Management

### Initializing a Project
```bash
# Create a new project
uv init project-name

# Initialize in current directory
uv init .
```

### Creating and Managing Virtual Environments
```bash
# Create a virtual environment
uv venv

# Activate the virtual environment
# On Unix/macOS:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

### Running Python Scripts
```bash
# Run a Python script in the project's environment
uv run script.py
```

<a name="uv-dependency-management"></a>
## Dependency Management

### Installing Packages
```bash
# Add a package to your project
uv add requests

# Add a specific version
uv add requests==2.28.1

# Add with constraints
uv add 'requests<3.0.0'

# Add with platform constraints
uv add 'requests; sys_platform="linux"'
```

### Managing Dependencies
```bash
# Install dependencies from requirements.txt
uv pip install -r requirements.txt

# Install a package in development mode
uv pip install -e .

# Remove a package and its dependencies
uv remove package-name
```

### Working with Dependency Groups
```bash
# Add a package to a specific group
uv add --group dev pytest

# Install only specific groups
uv pip install --group dev
```

<a name="uv-tool-integration"></a>
## Tool Integration

### Using Python Development Tools
```bash
# Run a tool without installing it in your environment
uv tool run black hello.py

# Using the shorter syntax
uvx black hello.py
```

### Managing Python Versions
```bash
# List installed Python versions
uv python list
```

<a name="migrating-to-uv"></a>
## Migrating from pip/virtualenv to UV

### Converting Existing Projects
```bash
# Generate requirements.txt from current environment
pip freeze > requirements.txt

# Initialize UV project
uv init .

# Install from requirements
uv pip install -r requirements.txt
```

### Command Equivalents

| pip/virtualenv Command | UV Equivalent |
|------------------------|---------------|
| `python -m venv .venv` | `uv venv` |
| `pip install package` | `uv add package` |
| `pip install -r requirements.txt` | `uv pip install -r requirements.txt` |
| `pip uninstall package` | `uv remove package` |

## Quick Reference

### Common UV Commands
```
# Project Management
uv init <name>                               # Create a new project
uv venv                                      # Create virtual environment

# Package Management
uv add <package>                             # Add a package
uv add <package>==<version>                  # Add specific version
uv remove <package>                          # Remove a package
uv pip install -r requirements.txt           # Install from requirements

# Tool Usage
uvx <tool> [args]                            # Run a tool without installing
uv tool run <tool> [args]                    # Same as above

# Running Python
uv run <script.py>                           # Run script in environment
```

---

For more detailed information, refer to the official documentation:
- [UV Documentation](https://github.com/astral-sh/uv)

---

## Quick Reference

### Common Git Commands Cheatsheet
```
# Setup
git config --global user.name "Name"           # Set username
git config --global user.email "email"         # Set email

# Initialization
git init                                       # Initialize repository
git clone <url>                                # Clone repository

# Basic Flow
git status                                     # Check status
git add <file>                                 # Stage file
git commit -m "message"                        # Commit changes
git push origin <branch>                       # Push to remote

# Branches
git branch                                     # List branches
git checkout -b <branch>                       # Create branch
git merge <branch>                             # Merge branch
git branch -d <branch>                         # Delete branch

# Updates
git fetch                                      # Fetch changes
git pull                                       # Pull changes
git remote -v                                  # List remotes
```

### Common GitHub CLI Commands
```
# Authentication
gh auth login                                  # Login to GitHub

# Repository
gh repo create <name> [flags]                  # Create repository
gh repo clone <repo>                           # Clone repository
gh repo view                                   # Show repository info

# Pull Requests
gh pr create                                   # Create PR
gh pr list                                     # List PRs
gh pr checkout <number>                        # Checkout PR
gh pr merge <number>                           # Merge PR

# Issues
gh issue create                                # Create issue
gh issue list                                  # List issues
gh issue close <number>                        # Close issue
```

---

For more detailed information, refer to the official documentation:
- [Git Documentation](https://git-scm.com/doc)
- [GitHub CLI Documentation](https://cli.github.com/manual/)