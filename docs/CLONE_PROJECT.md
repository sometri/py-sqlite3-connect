# Guide: Clone This Project to Your Local PC

This guide shows how to copy (clone) this project from GitHub onto your own computer.
It works for **any GitHub account** (`<your-github-username>`), **any project name**
(`<your-project-name>`), and **any repository** — whether it is **public** or **private**.

Replace the placeholders as you go:

- `<your-github-username>` — the GitHub username that owns the repo, e.g. `octocat`
- `<your-project-name>` — the repo name, e.g. `py-sqlite3-connect`

---

## 1. What you need first

- **Git** installed on your PC.
  - Check if you already have it:

    ```bash
    git --version
    ```

  - If not, install it with winget from **PowerShell** or **Command Prompt**:

    ```bash
    winget install Git.Git
    ```

    Or download it from https://git-scm.com/downloads.

- For a **private** repo, you must be logged in / authorized (see Step 3).

---

## 2. Pick a folder for your projects

Open a terminal (PowerShell, Command Prompt, or Git Bash) and go to a place where you
keep your code, for example:

```bash
cd D:\py
```

---

## 3. Clone the repository

The clone command is the same for public and private repos — the only difference is
that private repos require authentication.

### Option A — Public repository

Anyone can clone it with no login:

```bash
git clone https://github.com/<your-github-username>/<your-project-name>.git
```

### Option B — Private repository

Only you (or invited collaborators) can clone it. Git will ask for credentials:

- **Username:** your GitHub username (`<your-github-username>`)
- **Password:** a **Personal Access Token** (NOT your account password)
  - Create one at: GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
  - Give it the `repo` scope.

```bash
git clone https://github.com/<your-github-username>/<your-project-name>.git
```

> Tip: save the token so you don't retype it — use Git Credential Manager (bundled with
> Git for Windows) or the GitHub CLI (`gh auth login`), which handles auth for you.

### Get the exact URL

On GitHub, open the repo, click the green **Code** button, and copy the **HTTPS** URL.
That gives you the exact `https://github.com/<owner>/<repo>.git` link to use above.

---

## 4. Go into the cloned folder

```bash
cd <your-project-name>
```

Everything from the repo is now on your PC.

---

## 5. (Optional) Keep it up to date

Later, to pull the latest changes from GitHub:

```bash
git pull
```

---

## Cloning with GitHub CLI (alternative)

If you have the GitHub CLI installed and logged in (`gh auth login`), you can clone
with a shorter command, and it handles private-repo auth automatically:

```bash
gh repo clone <your-github-username>/<your-project-name>
```

---

## Common issues

| Problem | Fix |
| --- | --- |
| `git: command not found` | Install Git (Step 1) and reopen the terminal. |
| `Repository not found` on a private repo | Sign in, or use a Personal Access Token with the `repo` scope. |
| `Authentication failed` | Use a **token**, not your account password. |
| `Support for password authentication was removed` | Same as above — use a token or `gh auth login`. |
| Wrong branch / missing files | You are on the default branch (`main`); run `git checkout main` if needed. |
