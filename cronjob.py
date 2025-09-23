#!/usr/bin/env python3
import os
import random
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)


def read_number():
    with open("commit.txt", "r") as f:
        return int(f.read().strip())


def write_number(num):
    with open("commit.txt", "w") as f:
        f.write(str(num))


def git_commit():
    subprocess.run(["git", "add", "commit.txt"])

    messages = [
        "chore: update dependency versions",
        "fix: correct typo in documentation",
        "refactor: simplify commit counter logic",
        "style: format code according to style guide",
        "ci: configure GitHub Actions workflow",
        "docs: improve README installation steps",
        "perf: reduce file IO operations",
        "build: bump version number",
        "test: add basic coverage for commit logic",
        "fix: handle missing commit.txt gracefully",
        "chore: add commit message templates",
        "ci: update Python version in workflow",
        "docs: add contributing guidelines",
        "refactor: rename variables for clarity",
        "fix: avoid crash on initial run",
        "style: unify code indentation",
        "perf: optimize script startup time",
        "chore: clean up unused imports",
        "docs: update license year",
        "fix: correct permissions for commit.txt",
        "ci: add workflow_dispatch trigger",
        "build: setup linting and formatting",
        "refactor: extract helper functions",
        "fix: guard against file read errors",
        "chore: update project metadata"
    ]

    commit_message = random.choice(messages)
    subprocess.run(["git", "commit", "-m", commit_message])


def git_push():
    result = subprocess.run(["git", "push"], capture_output=True, text=True)
    if result.returncode == 0:
        print("Changes pushed to GitHub successfully.")
    else:
        print("Error pushing to GitHub:")
        print(result.stderr)


def main():
    try:
        current_number = read_number()
        new_number = current_number + 1
        write_number(new_number)
        git_commit()
        git_push()
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)


if __name__ == "__main__":
    main()
