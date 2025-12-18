# Python Bootcamp - Maktab 78 Complete Portfolio

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-REST%20API-green.svg)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Database-brightgreen.svg)](https://www.mongodb.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue.svg)](https://www.postgresql.org/)

This repository contains a comprehensive collection of assignments, exercises, and projects completed during the **Maktab Sharif Python Bootcamp (Maktab 78)**. It showcases progression from Python fundamentals through advanced topics including OOP, database integration, web development, and software design patterns.

---

## 📚 Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Prerequisites & Setup](#prerequisites--setup)
- [Homework Assignments](#homework-assignments)
  - [HWK1: Python Fundamentals](#hwk1-python-fundamentals)
  - [HWK2: Functions & Functional Programming](#hwk2-functions--functional-programming)
  - [HWK3: Object-Oriented Programming Basics](#hwk3-object-oriented-programming-basics)
  - [HWK4: File Operations & Linux Terminal](#hwk4-file-operations--linux-terminal)
  - [HWK5: Design Patterns & System Processes](#hwk5-design-patterns--system-processes)
  - [HWK6: Abstract Classes & Matrix Operations](#hwk6-abstract-classes--matrix-operations)
  - [HWK7: Bash Scripting & Serialization](#hwk7-bash-scripting--serialization)
  - [HWK8: Data Serialization with Pickle](#hwk8-data-serialization-with-pickle)
  - [HWK9: Database Theory & PostgreSQL](#hwk9-database-theory--postgresql)
  - [HWK10: Context Managers & Database Operations](#hwk10-context-managers--database-operations)
  - [HWK11: Command-Line Arguments & Date/Time](#hwk11-command-line-arguments--datetime)
  - [HWK12: Exception Handling & Data Validation](#hwk12-exception-handling--data-validation)
  - [HWK13: Frontend Development (HTML/CSS/Bootstrap)](#hwk13-frontend-development-htmlcssbootstrap)
  - [HWK21: Documentation Exercises](#hwk21-documentation-exercises)
  - [HWK22: Flask REST API with MongoDB](#hwk22-flask-rest-api-with-mongodb)
  - [HWK_GL: Group Learning Materials](#hwk_gl-group-learning-materials)
- [Major Projects](#major-projects)
  - [M78__FileStore: PostgreSQL File Management System](#m78__filestore-postgresql-file-management-system)
  - [password_gen_v1: Advanced CLI Password Generator](#password_gen_v1-advanced-cli-password-generator)
  - [password_gen: Password Generator Project](#password_gen-password-generator-project)
  - [psyc: PostgreSQL Database Models](#psyc-postgresql-database-models)
- [Running the Projects](#running-the-projects)
- [Dependencies & Requirements](#dependencies--requirements)
- [Notes & Troubleshooting](#notes--troubleshooting)
- [License](#license)

---

## 🎯 Overview

This monorepo documents a complete journey through Python development, covering:

- **Core Python**: Data types, control flow, functions, comprehensions
- **Object-Oriented Programming**: Classes, inheritance, abstract base classes, design patterns
- **System Programming**: File I/O, serialization (pickle/dill), logging, command-line tools
- **Bash Scripting**: Shell scripts for automation and system management
- **Database Systems**: PostgreSQL (psycopg2), MongoDB (pymongo)
- **Web Development**: Flask REST APIs, HTML/CSS, Bootstrap
- **Software Design**: Singleton pattern, decorators, context managers
- **Data Validation**: Regular expressions, custom exceptions, type checking
- **Frontend Technologies**: HTML5, CSS3, Bootstrap 5

Each homework folder (`HWK*`) contains:
- `excersizes/` - Completed assignment solutions
- `refrences/` - Course materials, PDFs, and reference documents

---

## 📁 Repository Structure

```
.
├── HWK1/                    # Python basics (I/O, strings)
├── HWK2/                    # Functions, map, filter, zip
├── HWK3/                    # OOP basics, classes, properties
├── HWK4/                    # File operations, Linux commands
├── HWK5/                    # Design patterns, bash scripts
├── HWK6/                    # Abstract classes, matrix operations
├── HWK7/                    # Bash scripting, pickle/dill
├── HWK8/                    # Pickle serialization
├── HWK9/                    # Database theory (PostgreSQL)
├── HWK10/                   # Context managers, database ops
├── HWK11/                   # sys.argv, decorators, datetime
├── HWK12/                   # Exceptions, validation, JSON/HTML
├── HWK13/                   # HTML/CSS/Bootstrap frontend
├── HWK21/                   # Documentation exercises
├── HWK22/                   # Flask + MongoDB REST API
├── HWK_GL/                  # Group learning materials
├── M78__FileStore/          # PostgreSQL file storage system
├── password_gen/            # Password generator (v1)
├── password_gen_v1/         # Advanced password generator
└── psyc/                    # PostgreSQL model definitions
```

---

## 🛠️ Prerequisites & Setup

### Requirements

- **Python 3.8+** (Python 3.9+ recommended)
- **MongoDB** (for HWK22 project)
- **PostgreSQL** (for M78__FileStore and psyc projects)
- **pip** (Python package manager)
- **mongorestore** utility (MongoDB Tools, for HWK22 data restoration)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Raminyazdani/HW_all_maktab-78.git
   cd HW_all_maktab-78
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install project-specific dependencies**:
   
   ⚠️ **Note**: Several `requirements.txt` files in this repository are empty, corrupted, or have encoding issues. You may need to manually install dependencies based on import statements in the code.

---

## 📖 Homework Assignments

### HWK1: Python Fundamentals

**Topics**: Input/output, string manipulation, data types, basic control flow

**Key Exercises**:
- **Practice1.py**: String manipulation - Replace spaces, swap case, replace vowels with dots
- **practice2.py**: User input processing
- **practice3.py**: Basic arithmetic operations
- **practice4.py**: Control flow and conditionals
- **practice5.py**: String and character operations

**Learning Outcomes**: Basic Python syntax, string methods (`replace()`, `swapcase()`), user input handling with `input()`

**Reference Materials**: `refrences/` contains `Maktab78-HW1.pdf`, `PyMaktabSharif_1.pdf`, `PyMaktabSharif_2.pdf`

---

### HWK2: Functions & Functional Programming

**Topics**: Function definitions, lambda expressions, `map()`, `filter()`, `zip()`, list comprehensions

**Key Exercises**:
- **EX_1.py**: Temperature conversion (Celsius to Fahrenheit)
  - Demonstrates function composition
  - Uses `map()` for batch conversion
  - Implements `zip()` for paired output formatting
  ```python
  def ctof(degree: float) -> float:
      return ((degree * 9) / 5) + 32
  ```
- **EX_2.py** through **EX_6.py**: Various functional programming exercises

**Learning Outcomes**: Higher-order functions, functional programming paradigms, list transformations

**Reference Materials**: `PyMaktabSharif_3.pdf`, `PyMaktabSharif_4.pdf`, `Maktab78-HW2.pdf`

---

### HWK3: Object-Oriented Programming Basics

**Topics**: Classes, properties, decorators (`@property`, `@classmethod`), datetime operations, OOP design

**Key Exercises**:
- **ex1.py**: `BirthDay` class - Comprehensive age calculator
  - **Features**:
    - Input validation with regex (`re` module)
    - Calculates age (years, months, days, hours, minutes, seconds)
    - Calculates time until next birthday
    - Leap year detection
    - Real-time countdown display
  - **Methods**:
    - `@property year_old`: Returns detailed age breakdown
    - `@property to_birthday`: Returns time until next birthday
    - `@classmethod check_year`, `check_month`, `check_day`, `check_clock`: Input validators
  - Demonstrates advanced OOP concepts and date/time arithmetic

- **ex2.py**: Additional OOP exercises
- **ex3-1.py**, **ex3-2.py**: More class-based implementations

**Learning Outcomes**: Class design, property decorators, class methods, time module usage, validation patterns

**Reference Materials**: `PyMaktabSharif_5.pdf`, `Maktab78-HW3.pdf`

---

### HWK4: File Operations & Linux Terminal

**Topics**: File I/O, text file processing, Linux command-line basics

**Key Exercises**:
- **ex1.py**: File reading and writing operations
- **test.py**: Testing file operations
- **Linux Terminal Research**: Documentation exercises on terminal commands (`.docx` and `.pdf` files)

**Learning Outcomes**: File handling, text processing, basic Linux command knowledge

**Reference Materials**: `PyMaktabSharif_6.pdf`, `Maktab78-HW4.pdf` (includes Linux command references)

---

### HWK5: Design Patterns & System Processes

**Topics**: Singleton pattern, bash scripting, process management (`ps`, `top`, `kill`)

**Key Exercises**:
- **ex1.py**: Multiple Singleton pattern implementations
  ```python
  class SingletonClassic(object):
      instance = None
      def __new__(cls):
          if not hasattr(cls, 'instance'):
              cls.instance = super(SingletonClassic, cls).__new__(cls)
          return cls.instance
  ```
  - Classic Singleton
  - Singleton with `__new__`
  - Metaclass-based Singleton
  - Singleton inheritance patterns

- **downloader.sh**: Bash script for automated downloads
- **ex4.py**: Additional scripting exercises
- **pics archive/**: Downloaded content storage
- **Process Management Documentation**: Research on `ps`, `top`, `kill` commands (`.docx` and `.pdf`)

**Learning Outcomes**: Design patterns, creational patterns, bash scripting basics, Linux process management

**Reference Materials**: `PyMaktabSharif_7.pdf`, `Git-1.pdf` (Git version control introduction)

---

### HWK6: Abstract Classes & Matrix Operations

**Topics**: Abstract Base Classes (ABC), mathematical operations, OOP abstraction

**Key Exercises**:
- **ex1.py**: Matrix operations with abstract base class
  ```python
  from abc import ABC, abstractmethod

  class BaseMatrix(ABC):
      @abstractmethod
      def present_matrix(self) -> None:
          return None
      @abstractmethod
      def get_matrix(self) -> None:
          return None
  ```
  - Implements `Matrix_` class with full matrix operations
  - Dictionary-based matrix storage: `self.matrix_dict[(h, w)]`
  - Supports initialization from number lists
  - Matrix arithmetic operations

- **ex2.pdf**: Documentation on matrix theory

**Learning Outcomes**: Abstract classes, `abc` module, mathematical algorithms, OOP abstraction patterns

**Reference Materials**: `PyMaktabSharif_8.pdf`, `Maktab78-HW6.pdf`

---

### HWK7: Bash Scripting & Serialization

**Topics**: Advanced bash scripting, Python serialization (pickle, dill), logging

**Key Exercises**:
- **ex1.sh**: File validation and content display script
  ```bash
  check_file() {
      local file_name_pass=$1
      if [ -f "${file_name_pass}" ]; then
          echo "File exists"
          tail -10 "${file_name_pass}"
      fi
  }
  ```
  - Command-line argument handling
  - File existence checks
  - Line counting with `wc -l`
  - Displays last 10 lines with `tail`

- **ex2/**: Port documentation exercises
- **ex3/ex3.py**: User management with pickle serialization
  ```python
  import pickle, dill
  class User:
      def __init__(self, id, first_name, last_name, phone):
          # User attributes
  ```
  - Loads data from `users.pickled`
  - Regex pattern matching for phone numbers (`^0919\d{7}$`)
  - Sorting and filtering users
  - Mixed pickle/dill serialization output

- **ex4/**: Logging implementation
  - `person.py`: Person class with logging
  - `sample.py`: Usage examples
  - `person.log`: Log output file

**Learning Outcomes**: Bash scripting, file operations, pickle/dill serialization, logging module, regex validation

**Reference Materials**: `PyMaktabSharif_9.pdf`, bash scripting guides

---

### HWK8: Data Serialization with Pickle

**Topics**: Python `pickle` module, binary serialization, data persistence

**Key Exercises**:
- **excersizes/**: Pickle serialization exercises
- **numbers.pickle**: Serialized data file
- Documentation exercises (`.docx` files)

**Learning Outcomes**: Binary serialization, data persistence, pickle protocol understanding

**Reference Materials**: Pickle module documentation references

---

### HWK9: Database Theory & PostgreSQL

**Topics**: Database concepts, SQL fundamentals, PostgreSQL, normalization, ER diagrams

**Key Exercises**:
- **Theory only** - no code exercises
- Extensive reference materials for database learning

**Learning Outcomes**: Database design principles, SQL basics, relational database theory, normalization forms

**Reference Materials**:
- `Database-System-Concepts.pdf`: Comprehensive database textbook
- `PostgreSQLNotesForProfessionals.pdf`: PostgreSQL practical guide
- `PyMaktabSharif_10.pdf`, `PyMaktabSharif_db_1.pdf`: Course-specific materials
- `Maktab78-HW9.pdf`: Homework assignments

---

### HWK10: Context Managers & Database Operations

**Topics**: Context managers (`with` statement), `__enter__`/`__exit__` methods, database connectivity

**Key Exercises**:
- **ex1.py**: `Indenter` context manager
  ```python
  class Indenter:
      def __init__(self):
          self.indented = -1
      def __enter__(self):
          self.indented += 1
          return self
      def __exit__(self, exc_type, exc_value, exc_tb):
          self.indented -= 1
      def print(self, text):
          print("    " * self.indented + text)
  ```
  - Nested context manager usage
  - Automatic indentation management

- **ex2.py**: Additional context manager patterns
- **ex3.py**: Database connectivity exercises
- **ex4/**: SQL query exercises
  - `ERD.png`: Entity-Relationship Diagram
  - `queries.docx`: SQL query documentation
- **log_cache.txt**: Cached operation logs

**Learning Outcomes**: Context managers, resource management, `with` statement protocol, database connections

**Reference Materials**: `PyMaktabSharif_11.pdf`, `PyMaktabSharif_db_2.pdf`, `Maktab78-HW10.pdf`

---

### HWK11: Command-Line Arguments & Date/Time

**Topics**: `sys.argv`, `argparse`, decorators, `datetime`, `jdatetime` (Jalali calendar)

**Key Exercises**:
- **ex1.py**: Command-line average calculator
  ```python
  import sys
  numbers = sys.argv
  numbers = list(map(lambda x: float(x), numbers[1:]))
  print(sum(numbers) / len(numbers))
  ```
  - Processes command-line arguments
  - Type conversion and error handling

- **ex2.py**: Decorator implementations

- **ex3.py**: Advanced datetime operations
  ```python
  import datetime, jdatetime
  def seconds_between(date1, date2):
      return abs((date1 - date2).total_seconds())
  def is_leap(year):
      return ((year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0)))
  ```
  - Date parsing with `strptime`
  - Leap year detection
  - Clock change calculations
  - Jalali calendar support

- **ex4.py**: Guessing game with `argparse`
  ```python
  parser = argparse.ArgumentParser(description="guessing game")
  parser.add_argument("guessing_game", type=int)
  parser.add_argument("-g", "--guess", type=int, required=False)
  parser.add_argument("-s", "--start", type=int, default=0)
  parser.add_argument("-e", "--end", type=int, default=100)
  ```
  - Interactive number guessing
  - Command-line argument parsing
  - Range validation

- **ex5.py**: Weekday generator
  ```python
  def generate_days(start_time, end_time, day):
      temp = start_time
      while temp <= end_time:
          if temp.weekday() == day:
              yield temp
          temp += datetime.timedelta(days=1)
  ```
  - Generator functions with `yield`
  - Date range iteration
  - Weekday filtering

**Learning Outcomes**: Command-line tools, `sys.argv`, `argparse` module, datetime arithmetic, generators, Jalali calendar, decorators

**Dependencies**: `jdatetime==4.1.0` (Persian calendar support)

**Reference Materials**: `PyMaktabSharif_12.pdf`, `Maktab78-HW11.pdf`

---

### HWK12: Exception Handling & Data Validation

**Topics**: Custom exceptions, regex validation, JSON/HTML generation, data serialization

**Key Exercises**:
- **ex1.py**: Comprehensive validation system
  ```python
  class ValidationError(Exception):
      def __init__(self, message, value=None):
          self.message = message
          self.value = value

  class NameValidationError(ValidationError):
      pass
  class PhoneValidationError(ValidationError):
      pass
  class EmailValidationError(ValidationError):
      pass

  def name_validation(name):
      # Validates: 4 <= len <= 14, only ascii_letters or '_'
      pattern = r"^[a-zA-Z_]{4,14}$"
      return bool(re.match(pattern, name))
  ```
  - Custom exception hierarchy
  - Regex-based validation (name, phone, email)
  - Non-regex validation alternatives

- **ex2.py**: Data transformation exercises
- **ex3.py**: JSON processing
- **ex4.py**: Complex data validation
- **ex4_JSON_time.json**: JSON output with timestamp
- **ex5.html**: HTML generation
- **asghar.json**: Sample JSON data
- **IMG_5283.jpg**: Image asset

**Learning Outcomes**: Exception handling, custom exceptions, regex patterns, JSON serialization, HTML generation, data validation strategies

**Reference Materials**: `PyMaktabSharif_13.pdf`, `PyMaktabSharif_Front_HTML.pdf`, `PyMaktabSharif_Front_CSS_1.pdf`, `Maktab78-HW12.pdf`, `Portfolio.pdf`

---

### HWK13: Frontend Development (HTML/CSS/Bootstrap)

**Topics**: HTML5, CSS3, Bootstrap 5, responsive design, frontend frameworks

**Key Exercises**:
- **ex1.index.html**: HTML page implementation
- **bootstrap/bootstrap-5.2.0-dist/**: Complete Bootstrap 5.2.0 framework
  - Full CSS and JS bundles
  - Icons and utilities
  - Responsive grid system
- **IMG_5283.jpg**: Image assets

**Learning Outcomes**: HTML structure, CSS styling, Bootstrap components, responsive design, frontend best practices

**Reference Materials**:
- `PyMaktabSharif_Front_CSS_2.pdf`: Advanced CSS
- `PyMaktabSharif_Front_bootstrap.pdf`: Bootstrap framework guide
- `Maktab78-HW13.pdf`: Assignment details
- `Portfolio.jpeg`: Portfolio design reference

---

### HWK21: Documentation Exercises

**Topics**: Technical documentation, written communication

**Key Files**:
- **hw21.docx**: Original homework documentation
- **hw21_edited.docx**: Edited version

**Learning Outcomes**: Technical writing, documentation standards, editing skills

---

### HWK22: Flask REST API with MongoDB

**Major Project** - Transaction aggregation and analysis REST API

**Topics**: Flask, Flask-RESTful, MongoDB, pymongo, aggregation pipelines, caching

#### Architecture

```
HWK22/
├── app.py                          # Flask application entry point
├── core/
│   ├── model_query_aggregate/
│   │   └── aggregate_query.py      # MongoDB aggregation builder
│   └── utils/
│       ├── initial_model.py        # DB initialization & mongorestore
│       └── query_machine.py        # Query utilities
├── templates/
│   └── home.html                   # Frontend template
└── static/                         # Static assets (CSS, JS, images)
    ├── Loading_icon.gif
    ├── callender/                  # Calendar widget
    └── main/                       # Main assets (TinyMCE, etc.)
```

#### Features

1. **REST API Endpoints**:
   - `GET /` - Renders home page (`home.html`)
   - `POST /transaction/` - Compute aggregation with parameters
   - `GET /transaction/` - Retrieve last computed results
   - `GET /merchants/` - List all merchant IDs

2. **Query Parameters** (via `reqparse`):
   - `user` (str): Filter by merchant ID
   - `sort` (str): Sort order ("1" ascending, "-1" descending)
   - `currency` (str): "rial" or "toman" (divides by 10 for toman)
   - `time_type` (str): Grouping - "none", "year", "month", "week", "day"
   - `start_time` (str): Start datetime (format: `yyyy-mm-dd-h-m-s-ms`)
   - `end_time` (str): End datetime (same format)

3. **MongoDB Aggregation**:
   - **Pipeline construction** in `aggregate_query.py`
   - Supports complex filtering, grouping, and sorting
   - Currency conversion (rial ↔ toman)
   - Time-based aggregations

4. **Query Caching**:
   - Caches aggregation results in MongoDB collection `transactions_test_cache`
   - Cache key: SHA256 hash of aggregation pipeline
   - Avoids redundant expensive queries

5. **Database Initialization**:
   - Checks for DB `transactions_test`
   - If missing, attempts to restore from `transaction.bson` using `mongorestore`
   - **Important**: `transaction.bson` must be in current working directory
   - **Requires**: `mongorestore` command in PATH

#### Running HWK22

```bash
cd HWK22

# Ensure MongoDB is running
# mongod --dbpath /path/to/data

# If transaction.bson is available:
# Place it in HWK22/ directory
# It will be auto-restored on first run

# Run the Flask app
python app.py

# Access at: http://127.0.0.1:5000/
```

**Example API Usage**:

```bash
# Get merchant list
curl http://127.0.0.1:5000/merchants/

# Post query with parameters
curl -X POST http://127.0.0.1:5000/transaction/ \
  -d "user=merchant_123" \
  -d "sort=1" \
  -d "currency=toman" \
  -d "time_type=month" \
  -d "start_time=2021-01-01-0-0-0-0" \
  -d "end_time=2022-12-31-23-59-59-999"

# Get last results
curl http://127.0.0.1:5000/transaction/
```

**Dependencies**:
- Flask
- Flask-RESTful
- pymongo
- MongoDB Tools (for mongorestore)

**Database Schema**:
- Database: `transactions_test`
- Collection: `transaction` (main data)
- Collection: `transactions_test_cache` (query cache)

**Learning Outcomes**: REST API design, Flask framework, MongoDB operations, aggregation pipelines, caching strategies, API parameter parsing

---

### HWK_GL: Group Learning Materials

**Topics**: Collaborative learning resources

**Key Files**:
- **GL-W4.pdf**: Week 4 group learning materials
- **GL-W6.pdf**: Week 6 group learning materials
- **GL-W7.pdf**: Week 7 group learning materials
- **GL-W8.pdf**: Week 8 group learning materials

**Learning Outcomes**: Peer collaboration, group study techniques

---

## 🚀 Major Projects

### M78__FileStore: PostgreSQL File Management System

**Major Project** - Database-backed file storage system with ORM-like abstraction

**Topics**: PostgreSQL, psycopg2, ORM design, database abstraction layer, MVC pattern

#### Architecture

```
M78__FileStore/
├── main.py               # Application entry point
├── routes.py             # Route definitions
├── configs.py            # Database configuration
├── core/
│   ├── models.py         # Base DBModel abstract class
│   ├── managers.py       # DBManager for CRUD operations
│   ├── query.py          # SQL query builders
│   ├── router.py         # Routing logic
│   └── utils.py          # Validation utilities (descriptors)
├── users/
│   └── models.py         # User model
├── file/
│   └── models.py         # Files model
├── comment/
│   └── models.py         # Comment model
├── order_cart/
│   └── models.py         # Order_cart model
├── order_item/
│   └── models.py         # Order_item model
└── public/               # Public file storage
```

#### Features

1. **Custom ORM Layer**:
   - `DBModel` abstract base class for all models
   - Automatic table creation from model definitions
   - CRUD operations via `DBManager`
   - Property descriptors for validation

2. **Models**:
   - **User**: `first_name`, `last_name`, `username`, `email`, `phone`, `national_id`, `age`, `password`
   - **Files**: File metadata (`file_name`, `username`, `file_path`, `description`)
   - **Comment**: User comments on files
   - **Order_cart**: Shopping cart implementation
   - **Order_item**: Individual cart items

3. **Validation Utilities** (`core/utils.py`):
   - Python descriptors for data validation
   - `First_name`, `Last_name`, `User_name`, `Email`, `Phone`, `National_id`, `Age`, `Password`
   - Automatic validation on attribute assignment

4. **Database Manager** (`core/managers.py`):
   ```python
   class DBManager:
       def __init__(self, db_name):
           # Connects to PostgreSQL database
       def insert_table(self, model_instance):
           # Inserts model instance into DB
       def read(self, model_class):
           # Reads all records from model table
   ```

#### Database Configuration

**File**: `configs.py`
```python
DB_CONNECTION = {
    'HOST': 'localhost',
    'USER': 'postgres',
    'PORT': 5432,
    'PASSWORD': 'your_password'  # Update with actual password
}
```

#### Running M78__FileStore

```bash
cd M78__FileStore

# Ensure PostgreSQL is running
# sudo service postgresql start

# Update configs.py with your PostgreSQL credentials

# Run the application
python main.py
```

**Example Usage** (from `main.py`):

```python
from core.managers import DBManager
from users.models import User
from file.models import Files

DB = DBManager("test")  # Connects to 'test' database

# Insert a user
user = User("ramin", "yazdani", "ramin_yz", 
            "yazdani76ramin@gmail.com", "09124981090", 
            "0020349629", "24", "RAmin@12345")
DB.insert_table(user)

# Read all users
users = DB.read(User)
print("Users:", users)

# Insert a file
file = Files("ketab", "ramin_yz", "C://desktop/", "ketabe darsi")
DB.insert_table(file)
```

**Dependencies**:
- `psycopg2` or `psycopg2-binary`
- PostgreSQL database server

**Note**: `requirements.txt` is empty. Install dependencies manually:
```bash
pip install psycopg2-binary
```

**Learning Outcomes**: Database abstraction, ORM design, PostgreSQL connectivity, descriptor protocol, MVC architecture, SQL query building

---

### password_gen_v1: Advanced CLI Password Generator

**Major Project** - Feature-rich command-line password generation tool

**Topics**: `argparse`, CLI design, logging, password security, itertools

#### Features

1. **Command-Line Interface**:
   - **Unique prefix chars**: `-`, `+`, `/` (non-standard `argparse` usage)
   - Argument groups and mutually exclusive options
   - Complex argument validation

2. **Arguments**:
   - `-w/--words`: List of characters to use in password
   - `-o/--output`: Output file (append mode)
   - `-l/--length`: Password length range (min, max)
   - `-t/--testWords`: Starting characters (prefix)
   - Mutually exclusive group:
     - `-L`: Boolean flag (default False)
     - `+L`: Boolean flag (True)
     - `/L N`: Integer value

3. **Password Generation**:
   - Random character selection from allowed character set
   - Supports custom word lists
   - Length randomization within specified range
   - Prefix/suffix support via `testWords`
   - Seeded randomization for reproducibility

4. **Logging**:
   ```python
   logger = logging.getLogger("password_logger")
   file_handler = logging.FileHandler("password.log", "a", encoding="utf-8")
   logger.setLevel(logging.DEBUG)
   ```
   - Comprehensive logging to `password.log`
   - Error tracking for invalid arguments
   - Logs all password generation events

5. **Custom Exceptions**:
   - `ArgumentTypeErrorRange`: Invalid length range
   - `ArgumentTypeErrorPasswords`: Invalid characters in word list
   - `ArgumentTypeErrorStartWords`: Prefix too long
   - `ArgumentTypeErrorFreq`: Invalid frequency value

6. **Validation**:
   - Ensures characters are in allowed set: `string.ascii_letters + string.digits + "!@#$%^&*()"`
   - Validates length ranges
   - Checks prefix length against max password length

#### Running password_gen_v1

```bash
cd password_gen_v1

# Basic usage
python program.py

# With arguments (examples based on code structure)
python program.py -w a b c d 1 2 3 -l 8 16
python program.py -t a b c -l 10 20 -o password.txt
```

**Output Files**:
- `password.log`: Detailed execution log
- `password.txt`: Generated passwords (if `-o` specified)

**Dependencies**:
- `quantumrandom==1.9.0` (noted in corrupted `requirements.txt`)
- Standard library: `argparse`, `itertools`, `random`, `string`, `logging`

**Note**: `requirements.txt` appears corrupted (encoding issues). Install manually:
```bash
pip install quantumrandom
```

**Learning Outcomes**: Advanced CLI design, `argparse` customization, logging best practices, password generation algorithms, exception handling

---

### password_gen: Password Generator Project

**Topics**: Password generation (earlier version)

**Structure**:
```
password_gen/
└── password_gen/   # Project directory
```

**Learning Outcomes**: Basic password generation concepts

---

### psyc: PostgreSQL Database Models

**Topics**: PostgreSQL, psycopg2, database modeling, UUID generation

#### Features

**File**: `database_psycopg2/models.py`

1. **Database Connection**:
   ```python
   import psycopg2, getpass
   
   password = getpass.getpass(prompt='Enter your password:')
   con = psycopg2.connect(dbname="models_test", 
                          user="postgres", 
                          password=password)
   ```
   - Secure password entry (not echoed to terminal)
   - Auto-commit enabled

2. **Dynamic Table Creation**:
   ```python
   def create_table(cursor, instance):
       query = f"Create Table {instance.__class__.__name__} ("
       for column, data_type in postgresql_table_data_names_types:
           query += f"{column} {data_type},"
       query = query[:-1] + ");"
       cursor.execute(query)
   ```
   - Automatically creates tables from model instances
   - Checks for table existence before creation

3. **Model Definition**:
   ```python
   class Student:
       postgresql_table_data_types = [
           "VARCHAR(32)", "VARCHAR(32)", "INTEGER", 
           "VARCHAR(64)", "VARCHAR(64)", "UUID NOT NULL"
       ]
       
       def __init__(self, name, surname, age, national_id, degree):
           self.name = name
           self.surname = surname
           self.age = age
           self.national_id = national_id
           self.degree = degree
           self.id = generate_uuid()
   ```
   - UUID primary keys via `uuid4()`
   - Type annotations for PostgreSQL
   - Automatic ID generation

4. **CRUD Operations**:
   - `not_exist()`: Check table existence
   - `create_table()`: Create table from instance
   - `insert_instance()`: Insert data into table
   - `insert_into()`: Combined check and insert

#### Running psyc

```bash
cd psyc/database_psycopg2

# Ensure PostgreSQL is running with database 'models_test'
# sudo service postgresql start
# psql -U postgres -c "CREATE DATABASE models_test;"

# Run the models script
python models.py
# Enter PostgreSQL password when prompted
```

**Dependencies**:
- `psycopg2` or `psycopg2-binary`
- PostgreSQL server with `models_test` database

**Learning Outcomes**: PostgreSQL connectivity, UUID generation, dynamic SQL query building, secure credential handling, ORM patterns

---

## 🏃 Running the Projects

### Quick Start Commands

#### HWK22 (Flask + MongoDB)
```bash
cd HWK22
# Ensure MongoDB is running and transaction.bson is in this directory
python app.py
# Visit http://127.0.0.1:5000/
```

#### M78__FileStore (PostgreSQL)
```bash
cd M78__FileStore
# Update configs.py with PostgreSQL credentials
pip install psycopg2-binary
python main.py
```

#### password_gen_v1
```bash
cd password_gen_v1
pip install quantumrandom
python program.py
```

#### psyc (PostgreSQL Models)
```bash
cd psyc/database_psycopg2
# Ensure database 'models_test' exists
python models.py
```

#### Individual Homework Exercises
```bash
# Navigate to specific homework folder
cd HWK3/excersizes
python ex1.py  # Run birthday calculator

cd ../../HWK7/excersizes
bash ex1.sh filename.txt  # Run bash script

cd ../../HWK11/excersizes
python ex4.py 50 -s 1 -e 100  # Guessing game
```

---

## 📦 Dependencies & Requirements

### Global Dependencies (Recommended)

For comprehensive project support, install:

```bash
pip install flask flask-restful pymongo psycopg2-binary jdatetime quantumrandom
```

### Project-Specific Dependencies

| Project | Dependencies | Notes |
|---------|-------------|-------|
| HWK11 | `jdatetime==4.1.0` | Jalali calendar support |
| HWK22 | `flask`, `flask-restful`, `pymongo` | Requires MongoDB server |
| M78__FileStore | `psycopg2-binary` | Requires PostgreSQL server |
| password_gen_v1 | `quantumrandom==1.9.0` | Quantum random number generation |
| psyc | `psycopg2-binary` | Requires PostgreSQL server |

### ⚠️ Important Notes

1. **Empty/Corrupted Requirements Files**:
   - `M78__FileStore/requirements.txt`: Empty
   - `password_gen_v1/requirements.txt`: Encoding issues
   - `HWK11/requirements.txt`: Encoding issues
   
   **Solution**: Install dependencies manually based on import statements

2. **Virtual Environments Committed**:
   - Several folders contain committed `venv/` directories
   - These should be excluded from version control
   - Recommended: Add to `.gitignore`:
     ```
     venv/
     venve/
     __pycache__/
     *.pyc
     .idea/
     ```

3. **Database Requirements**:
   - **MongoDB**: Required for HWK22
   - **PostgreSQL**: Required for M78__FileStore, psyc
   - Ensure database servers are running before executing projects

---

## 🔧 Notes & Troubleshooting

### Common Issues

#### HWK22: MongoDB Connection

**Error**: `MongoClient` connection failed

**Solution**:
```bash
# Start MongoDB server
mongod --dbpath /path/to/data/db

# If transaction.bson restore fails:
# Ensure mongorestore is in PATH
# Place transaction.bson in HWK22/ directory
# The app will auto-restore on startup
```

#### M78__FileStore: PostgreSQL Connection

**Error**: Connection refused / authentication failed

**Solution**:
1. Update `configs.py` with correct credentials
2. Ensure PostgreSQL is running:
   ```bash
   sudo service postgresql start
   ```
3. Create database if needed:
   ```bash
   psql -U postgres -c "CREATE DATABASE test;"
   ```

#### password_gen_v1: Module Not Found

**Error**: `ModuleNotFoundError: No module named 'quantumrandom'`

**Solution**:
```bash
pip install quantumrandom
```

#### HWK11: Import Error for jdatetime

**Error**: `ModuleNotFoundError: No module named 'jdatetime'`

**Solution**:
```bash
pip install jdatetime
```

### General Recommendations

1. **Use Virtual Environments**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

2. **Check Python Version**:
   - Minimum: Python 3.8
   - Recommended: Python 3.9+
   ```bash
   python --version
   ```

3. **Inspect Code for Dependencies**:
   - Check `import` statements at top of files
   - Install missing packages as needed

4. **Database Setup**:
   - Ensure database servers are properly configured
   - Check connection parameters in config files
   - Verify database/collection/table names

### Project-Specific Notes

- **HWK22**: Requires `transaction.bson` file for data restoration (not included in repo)
- **HWK7/ex3**: Requires `users.pickled` file (not included in repo)
- **Bash Scripts**: May need execution permissions (`chmod +x script.sh`)

---

## 📄 License

This project is an educational portfolio. No explicit license is provided. All code is for learning and demonstration purposes.

**Recommendation**: If sharing publicly, consider adding an open-source license (e.g., MIT, Apache 2.0).

---

## 🎓 About Maktab Sharif - Maktab 78

This repository represents the complete coursework from **Maktab Sharif's Python Bootcamp (Maktab 78)**, covering:

- 13 weekly homework assignments
- 4 major projects
- Database integration (MongoDB, PostgreSQL)
- Web development (Flask REST APIs)
- Frontend technologies (HTML/CSS/Bootstrap)
- Software engineering practices (OOP, design patterns, testing)

**Instructor Materials**: Each homework includes PDF references from course instructors (`PyMaktabSharif_*.pdf` series)

---

## 📞 Contact

For questions or collaboration opportunities:

- **Repository**: [Raminyazdani/HW_all_maktab-78](https://github.com/Raminyazdani/HW_all_maktab-78)
- **Email**: yazdani76ramin@gmail.com (from M78__FileStore/main.py)
- **Username**: ramin_yz

---

## 🙏 Acknowledgments

- **Maktab Sharif** for providing comprehensive Python education
- **Instructors** for detailed course materials and guidance
- **Bootcamp Cohort (Maktab 78)** for collaborative learning

---

**Last Updated**: December 2024

**Repository Status**: ✅ Complete - All bootcamp assignments and projects included

**Total Exercises**: 60+ Python exercises, 4 major projects, extensive reference materials

---

*This README provides comprehensive documentation of the entire repository. For specific implementation details, refer to individual homework folders and project directories.*
