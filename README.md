# HW_all_maktab-78

A personal **Python bootcamp portfolio repo**.

This repository collects my bootcamp homework folders (`HWK1` ➜ `HWK13`, `HWK21`, `HWK22`), a couple of larger practice projects (like a small “File Store” database project and a CLI password generator), plus the PDFs/resources that accompanied the course.

It’s organized as a **monorepo of small, mostly independent exercises**. Most folders can be run on their own (often as standalone scripts). A few folders contain full mini-projects with external dependencies (Flask/MongoDB/PostgreSQL).

---

## Table of contents

- [What’s inside](#whats-inside)
- [Quickstart (general)](#quickstart-general)
- [Folder-by-folder guide](#folder-by-folder-guide)
  - [Homework folders](#homework-folders)
  - [Projects](#projects)
  - [Other folders](#other-folders)
- [Running the main projects](#running-the-main-projects)
  - [`HWK22/` — Transactions aggregation API (Flask + MongoDB)](#hwk22--transactions-aggregation-api-flask--mongodb)
  - [`M78__FileStore/` — File Store (PostgreSQL, simple ORM-ish models)](#m78__filestore--file-store-postgresql-simple-orm-ish-models)
  - [`password_gen_v1/` — CLI password generator](#password_gen_v1--cli-password-generator)
- [Notes & assumptions](#notes--assumptions)

---

## What’s inside

High level categories:

- **`HWK_GL/`**: “Guide Line” PDFs (weekly PDF instructions / lecture notes).
- **`HWK1/` … `HWK13/`**: weekly homework exercises, usually simple scripts (`.py`) and sometimes HTML/CSS/Bootstrap.
- **`HWK21/`**: document-based homework submissions (`.docx`).
- **`HWK22/`**: a more complete backend assignment: **Flask REST API + MongoDB aggregation + caching**, plus an HTML frontend template.
- **`M78__FileStore/`**: a PostgreSQL-backed “file store” training project with models, a router/menu system, and DB utilities.
- **`password_gen/`, `password_gen_v1/`**: password generator attempts/iterations.
- **`psyc/`**: experiments around `psycopg2`/PostgreSQL (includes a local venv folder).

---

## Quickstart (general)

Most of the homework scripts are plain Python and can be executed directly.

### Prerequisites

- Python 3.x installed and available on PATH
- Recommended: a virtual environment per project

### Typical run pattern

From repo root:

```powershell
python .\HWK1\excersizes\Practice1.py
```

(Exact filenames differ by homework; see the [Folder-by-folder guide](#folder-by-folder-guide).)

---

## Folder-by-folder guide

### Homework folders

These are the bootcamp homework drops. Most contain:

- `excersizes/`: runnable scripts (and sometimes assets like JSON/images)
- `refrences/`: PDF lecture notes/resources (and sometimes a Persian “منابع.docx” list)

> Note: some folders also contain local `venv/` directories or `__pycache__/` from development.

#### `HWK1/`
Intro Python practice scripts:
- `excersizes/Practice1.py`, `practice2.py` … `practice5.py`
- also contains a submitted archive: `Ramin_yazdani_hw1_maktab78.rar`

#### `HWK2/`
Python exercises: `EX_1.py` … `EX_6.py`.

#### `HWK3/`
Python exercises including multi-part problems (`ex3-1.py`, `ex3-2.py`).

#### `HWK4/` ➜ `HWK9/`
Homework folders are present (repo view may be truncated). Each follows a similar pattern with `excersizes/` + `refrences/`.

#### `HWK10/`
Exercises `ex1.py`, `ex2.py`, `ex3.py` and an `ex4/` folder. Also includes `log_cache.txt`.

#### `HWK11/`
Exercises `ex1.py` … `ex5.py`.

Contains `requirements.txt`, but it appears to be **non-UTF8 / corrupted** in the current repo snapshot, so you may need to regenerate dependencies from imports.

#### `HWK12/`
Mix of Python + JSON + simple frontend:
- JSON inputs like `asghar.json`, `ex4_JSON_time.json`
- scripts `ex1.py` … `ex4.py`
- `ex5.html`
- image asset(s)

#### `HWK13/`
Frontend-focused homework:
- `ex1.index.html`
- `bootstrap/` folder and image assets

#### `HWK21/`
Document submissions:
- `hw21.docx`
- `hw21_edited.docx`

#### `HWK22/`
A complete mini-project. See [Running the main projects](#hwk22--transactions-aggregation-api-flask--mongodb).

### Projects

#### `M78__FileStore/`
A database-backed project that looks like a training “File Store” application:

- `main.py`: demo runner that creates a DB manager and inserts/reads several model records
- `configs.py`: PostgreSQL connection settings and app info
- `routes.py`: menu/router definition (CLI navigation)
- folders like `users/`, `file/`, `comment/`, `order_cart/`, `order_item/`, `core/`

> `requirements.txt` exists but is empty in this snapshot.

#### `password_gen_v1/`
A CLI password generator (argparse-based) that supports:

- choosing a character set (`--words`)
- optional prefix/start words (`--testWords`)
- different generation modes (`-L`, `+L`, `/L`)
- logging to `password.log`

See [password_gen_v1 — CLI password generator](#password_gen_v1--cli-password-generator).

#### `password_gen/`
An earlier folder/iteration of password generator work (structure suggests experimentation).

#### `psyc/`
PostgreSQL/psycopg2 practice. Contains `psyc/database_psycopg2/` and appears to include a checked-in virtual environment.

### Other folders

#### `HWK_GL/`
Course guideline PDFs:
- `GL-W4.pdf`, `GL-W6.pdf`, `GL-W7.pdf`, `GL-W8.pdf`

---

## Running the main projects

### `HWK22/` — Transactions aggregation API (Flask + MongoDB)

**What it is**

`HWK22/app.py` starts a Flask app that:

- serves a homepage at `/` via `templates/home.html`
- exposes REST endpoints:
  - `GET/POST /transaction/` — runs an aggregation query and returns the latest computed data
  - `GET /merchants/` — returns distinct merchant ids from Mongo

Under the hood it uses:

- `core/model_query_aggregate/aggregate_query.py` — builds MongoDB aggregation pipelines (year/month/day/week grouping, sorting, currency conversion)
- `core/utils/initial_model.py` — initializes MongoDB client/collections, and tries to restore a BSON dump when the DB isn’t found

**Important behavior to know**

- On import, `core/utils/initial_model.py` attempts to connect to MongoDB and, if needed, restore from a file named **`transaction.bson`** in the *current working directory*.
- It expects MongoDB tools (`mongorestore`) to be available on PATH if restore is needed.
- It uses two databases: `transactions_test` and `transactions_test_cache`.

**How to run**

1. Ensure MongoDB is running locally.
2. From repo root, run the Flask app:

```powershell
python .\HWK22\app.py
```

Then open:

- http://127.0.0.1:5000/ for the UI
- http://127.0.0.1:5000/transaction/ for API (GET)
- http://127.0.0.1:5000/merchants/ for merchant list

**Request parameters**

`POST /transaction/` accepts form-like arguments (via `flask_restful.reqparse`) including:

- `user`: merchant id (string)
- `sort`: `"1"` or `"-1"`
- `currency`: `rial` or `toman`
- `time_type`: `none`, `year`, `month`, `week`, `day`
- `start_time`, `end_time`: accepts either `YYYY` or a dash-separated time like `YYYY-MM-DD-h-m-s-ms` (the code converts `-` to `,` internally)

---

### `M78__FileStore/` — File Store (PostgreSQL, simple ORM-ish models)

**What it is**

A small project showing:

- basic modeling (`users`, `file`, `comment`, `order_cart`, `order_item` packages)
- a `DBManager` in `core/managers.py` (used by `main.py`) for CRUD-like operations
- a CLI router/menu structure in `core/router.py` with a `routes.py` definition

**Database configuration**

Connection settings live in `M78__FileStore/configs.py`:

- host: `localhost`
- port: `5432`
- user: `postgres`

> Password is stored in that file in this repo. If you’re cloning publicly or sharing, consider rotating/removing credentials.

**How to run**

`main.py` demonstrates inserting and reading models.

```powershell
python .\M78__FileStore\main.py
```

You’ll need:

- a running PostgreSQL server
- a database named `test` (as used by `DBManager("test")`)

---

### `password_gen_v1/` — CLI password generator

**What it is**

A command-line tool in `password_gen_v1/program.py` that generates passwords based on:

- a set of allowed characters (letters/digits and `!@#$%^&*()`) or user-selected `--words`
- optional initial prefix characters (`--testWords`)
- generation mode:
  - `-L` → generate a single random password (default)
  - `+L` → generate *all* permutations (can blow up quickly)
  - `/L N` → generate `N` unique random passwords

It logs to `password_gen_v1/password.log`.

**How to run (examples)**

From repo root:

```powershell
python .\password_gen_v1\program.py -l 8 12
python .\password_gen_v1\program.py -w a b c 1 2 3 -l 6 10 /L 5
python .\password_gen_v1\program.py -t R a m i n -l 10 12
```

> `password_gen_v1/requirements.txt` appears to be encoded oddly in this snapshot; the script itself only uses the Python standard library.

---

## Notes & assumptions

- **This repo is intentionally heterogeneous.** Many folders are one-off homework scripts; they don’t share a unified dependency setup.
- **Some `requirements.txt` files appear corrupted or empty** (`HWK11/requirements.txt`, `password_gen_v1/requirements.txt`, `M78__FileStore/requirements.txt`). If you want reproducible installs, the best next step is to rebuild requirements per project by inspecting imports.
- Some folders include local `venv/` directories that were committed during the bootcamp.
- `HWK22`’s Mongo restore logic looks for `transaction.bson` in the process working directory. If the dump lives elsewhere, run the app from the directory that contains the BSON file or copy it next to where you execute.

---

### License

No explicit license file is present in the root. If you plan to share this publicly, consider adding one (MIT/Apache-2.0 are common for learning repos).
