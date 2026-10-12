# Guide: Push Any Project to GitHub

This guide works for **any GitHub account** (`<your-github-username>`), **any project name**
(`<your-project-name>`), and **any repository** — whether it is **public** or **private**.

Replace the placeholders as you go:

- `<your-github-username>` — your GitHub username, e.g. `sometri`
- `<your-project-name>` — the repo name, e.g. `py-sqlite3-connect`
- `<your-email@example.com>` — the email tied to your GitHub account

Run all commands from the project folder (e.g. `D:\py\sqlite`).

---

## Step 1 — Initialize git

```bash
git init
```

## Step 2 — Set your identity (only needed once per machine)

```bash
git config --global user.name "<your-github-username>"
git config --global user.email "<your-email@example.com>"
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

## Step 6 — Create the repository on GitHub

### Option A — Public repository

Anyone can see it, anyone can clone it (read-only). Good for open source.

**On the website:** GitHub → **New repository** → name it `<your-project-name>` →
visibility **Public** → **Create repository** (do *not* add a README, since you already have one).

**Or with GitHub CLI:**

```bash
gh repo create <your-project-name> --public --source=. --push
```

### Option B — Private repository

Only you (and anyone you invite) can see it. Good for personal or work projects.

**On the website:** GitHub → **New repository** → name it `<your-project-name>` →
visibility **Private** → **Create repository** (do *not* add a README).

**Or with GitHub CLI:**

```bash
gh repo create <your-project-name> --private --source=. --push
```

## Step 7 — Connect your local repo to GitHub

Use the URL for the repo you created in Step 6 — the same command works for
public and private repos:

```bash
git remote add origin https://github.com/<your-github-username>/<your-project-name>.git
```

If the repo already has commits on GitHub (e.g. a README created on the website), pull first:

```bash
git pull origin main --allow-unrelated-histories
```

## Step 8 — Push

```bash
git push -u origin main
```

---

## Changing visibility later

You can switch a repo between public and private at any time:

GitHub → your repo → **Settings** → **General** → scroll to **Danger Zone** →
**Change repository visibility** → **Change visibility** → choose **Public** or **Private**.

> Note: changing a *private* repo to *public* exposes its entire commit history.

---

## Authentication

When git asks for a username/password, use:

- **Username:** your GitHub username (`<your-github-username>`)
- **Password:** a **Personal Access Token** (NOT your account password)
  - Create one at: GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
  - Give it the `repo` scope (this scope covers **both public and private** repositories).

## Optional: using GitHub CLI from scratch

The [GitHub CLI](https://cli.github.com/) (`gh`) lets you create the repo, connect it,
and push it in a single command — no need to touch the website. This works for **any**
account, project name, and repo, public or private.

### 1. Install the CLI

Run this in a **Windows terminal** — open **PowerShell** or **Command Prompt**
(press `Win`, type `powershell` or `cmd`, and hit Enter). `winget` ships with
Windows 10/11, so no extra setup is needed. If you are already in a shell and get a
"command not found" error, launch PowerShell instead.

```bash
winget install GitHub.cli
```

> If `winget` itself is missing, install **App Installer** from the Microsoft Store,
> or download the CLI directly from https://cli.github.com/.

By default this installs `gh.exe` to:

```
C:\Program Files\GitHub CLI\gh.exe
```

(The `winget` package uses the official MSI, so it always lands under `Program Files\GitHub CLI`.)

Close and reopen your terminal afterwards so the `gh` command is added to your `PATH`.
Verify the install:

```bash
gh --version
```

If `gh` is not found afterwards, either reopen the terminal or call it by its full path:

```bash
"C:\Program Files\GitHub CLI\gh.exe" --version
```

### 2. Log in

```bash
gh auth login
```

Answer the prompts:

- **What account do you want to log into?** → `GitHub.com`
- **What is your preferred protocol?** → `HTTPS`
- **Authenticate Git with your GitHub credentials?** → `Yes`
- **How would you like to authenticate?** → `Login with a web browser`
  (or paste a Personal Access Token if you prefer)

Check who you are logged in as:

```bash
gh auth status
```

### 3. Go to the project folder

```bash
cd D:\py\sqlite
```

### 4. Create the repo and push in one step

`--source=.` uses the current folder as the repo, and `--push` pushes the existing
commit immediately. Pick the visibility you want:

```bash
# Public repo
gh repo create <your-project-name> --public --source=. --push

# Private repo
gh repo create <your-project-name> --private --source=. --push
```

`gh repo create` also runs `git remote add origin ...` for you, so you can skip
Step 7 in this guide.

### 5. Useful follow-up commands

```bash
gh repo view --web              # open the repo in your browser
gh repo edit --visibility private   # switch an existing repo to private (or public)
gh repo edit --visibility public    # switch an existing repo to public
```

> Tip: add `--description "Short summary"` to `gh repo create` to set the repo
> description, and `--license mit` to add a license file automatically.

---

## Day-to-day workflow after setup

```bash
git add .
git commit -m "Describe your change"
git push
```
