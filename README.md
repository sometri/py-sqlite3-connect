# SQLite Python Demo

A small Python project demonstrating basic SQLite usage: creating a database, inserting records, and reading them back.

## Project Structure

```
sqlite/
├── main.py          # Insert a user into database.db
├── read_data.py     # Read and print all users from database.db
├── database.db      # SQLite database file
└── img/             # Screenshots of the code and output
```

## Requirements

- Python 3.x (the `sqlite3` module is part of the standard library, no extra install needed)

## Usage

Insert a new user:

```bash
python main.py
```

You will be prompted to enter a name; it is stored in the `users` table.

Read all users:

```bash
python read_data.py
```

This prints the contents of the `users` table in `database.db`.

## Database Schema

```sql
CREATE TABLE IF NOT EXISTS users (
    id   INTEGER PRIMARY KEY,
    name TEXT
);
```

## Notes

- All queries use parameterized statements (`?`) to prevent SQL injection.
- `database.db` is created automatically on first run.
