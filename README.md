# Installation

## Prerequisites
Go, Python and make should be installed.
_**leaks-report.json**_ should be added in .gitignore

## Windows
1. Copy file windows/pre-commit and pre-commit.py into {{PROJECT}}.git/hooks/pre-commit
2. For first time run powershell in admin mode
3. After first commit gitleaks will be installed

## Linux, Unix
1. Copy file unix/pre-commit and pre-commit.py into {{PROJECT}}.git/hooks/pre-commit
2. Make commit (after first commit gitleaks will be installed)

## Disabling
To disable gitleaks pre-commit hook run
```
git config --bool hooks.gitleaks false
```