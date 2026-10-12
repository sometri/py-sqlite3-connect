# Guide: Push This Project to GitHub

Target repository: https://github.com/sometri/py-sqlite3-connect

This project is **not yet a git repository**, so follow every step below in order.
Run all commands from the project folder (`D:\py\sqlite`).

---

## Step 1 — Initialize git

```bash
git init
```

## Step 2 — Set your identity (only needed once per machine)

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

## Step 3 — Stage the files you want to publish

```bash
git add README.md main.py read_data.py img
```

> `database.db` is intentionally left out. Add it with `git add database.db` only if you really want the binary DB file in the repo.

## Step 4 — Create the first commit

```bash
git commit -m "Initial commit"
```

## Step 5 — Rename the branch to `main`

```bash
git branch -M main
```

## Step 6 — Connect your local repo to GitHub

```bash
git remote add origin https://github.com/sometri/py-sqlite3-connect.git
```

If the repo already has commits on GitHub (e.g. a README created on the website), pull first:

```bash
git pull origin main --allow-unrelated-histories
```

## Step 7 — Push

```bash
git push -u origin main
```

---

## Authentication

When git asks for a username/password, use:

- **Username:** your GitHub username (`sometri`)
- **Password:** a **Personal Access Token** (NOT your account password)
  - Create one at: GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
  - Give it the `repo` scope.

## Optional: using GitHub CLI instead

```bash
winget install GitHub.cli
gh auth login
cd D:\py\sqlite
gh repo create py-sqlite3-connect --public --source=. --push
```

---

## Day-to-day workflow after setup

```bash
git add .
git commit -m "Describe your change"
git push
```
