# Lesson 13 — Modules and Packages in Python

## Learning objectives

By the end of this lesson, you should be able to:
- Explain what modules and packages are and how they differ.
- Import complete modules, selected functions, and aliases.
- Use useful Python standard-library modules.
- Create your own modules and packages.
- Import code from packages and subpackages.
- Understand third-party packages and install them with pip.
- Apply modules and packages to small SOC and Data Analytics tasks.

---

# Part 1 — Modules

## 1. What is a module?

A **module** is a Python file (usually ending in `.py`) that contains reusable Python code. It can contain functions, variables, classes, and executable statements.

For example, a file named `calculator.py`:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
```

This file is a module. Its functions can be imported into another Python file rather than rewritten.

### Why use modules?

1. Reuse code in multiple programs.
2. Keep related functionality together.
3. Make projects easier to read and maintain.
4. Test and debug smaller pieces independently.
5. Avoid duplicating the same functions.

## 2. Importing modules

Python's `import` statement makes code from another module available.

### Method 1 — Import the complete module

```python
import math

print(math.sqrt(25))
print(math.pi)
```

Output:

```text
5.0
3.141592653589793
```

Use the module name followed by a dot to access its members: `math.sqrt()`.

### Method 2 — Import a specific function

```python
from math import sqrt

print(sqrt(36))
```

Output:

```text
6.0
```

### Method 3 — Import multiple members

```python
from math import sqrt, factorial

print(sqrt(64))
print(factorial(5))
```

Output:

```text
8.0
120
```

### Method 4 — Import with an alias

An alias is a shorter alternative name.

```python
import math as m

print(m.sqrt(81))
```

Output:

```text
9.0
```

Common Data Analytics conventions:

```python
import numpy as np
import pandas as pd
```

### A note about wildcard imports

You may see:

```python
from math import *
```

This imports many names directly, but it is generally better to import the specific names you need. Wildcard imports can make it unclear where a name came from and can cause naming conflicts.

## 3. Useful Python standard-library modules

The **Python standard library** is the collection of modules and packages distributed with Python. They generally do not need a separate pip installation.

| Module | Purpose | Example use |
|---|---|---|
| `math` | Mathematical operations | Square roots and factorials |
| `random` | Pseudorandom values | Generating test data |
| `datetime` | Date and time | Event timestamps |
| `os` | Operating-system interaction | Listing files and directories |
| `sys` | Interpreter and runtime information | Command-line arguments |
| `json` | JSON encoding and decoding | Structured alerts and API data |
| `re` | Regular expressions | Finding patterns in log text |
| `csv` | CSV file reading and writing | Tabular datasets |
| `statistics` | Basic statistical calculations | Mean and median |
| `collections` | Specialized containers | Counting repeated events |

### 3.1 math

```python
import math

number = 25

print("Square root:", math.sqrt(number))
print("Power:", math.pow(2, 3))
print("Factorial:", math.factorial(5))
```

Output:

```text
Square root: 5.0
Power: 8.0
Factorial: 120
```

### 3.2 random

```python
import random

number = random.randint(1, 10)
print("Generated number:", number)
```

The output varies because the number is generated pseudorandomly. This can be useful for generating simulated test records. Do not use the ordinary `random` module for passwords, tokens, or cryptographic secrets; use `secrets` for security-sensitive randomness.

### 3.3 datetime

```python
from datetime import datetime

current_time = datetime.now()

print("Current date and time:", current_time)
print("Year:", current_time.year)
print("Month:", current_time.month)
print("Day:", current_time.day)
```

Output depends on when the code runs and the environment's timezone.

**SOC application:** Analysts examine timestamps to establish the order of events during an investigation. In real systems, preserve timezone information and normalize timestamps carefully before correlating logs.

### 3.4 os

```python
import os

print("Current directory:", os.getcwd())
print("Operating system name:", os.name)

files = os.listdir(".")
print("Directory contents:", files)
```

The output depends on the machine and working directory.

**SOC application:** A script can locate log files, inspect directory contents, and organize investigation output. Avoid modifying or deleting evidence files during an investigation.

### 3.5 json

JSON (JavaScript Object Notation) is a text format commonly used to exchange structured data between programs and services.

```python
import json

alert = {
    "username": "admin",
    "ip": "192.168.1.10",
    "event": "failed_login",
    "severity": "high"
}

json_text = json.dumps(alert, indent=4)
print(json_text)
```

Output:

```json
{
    "username": "admin",
    "ip": "192.168.1.10",
    "event": "failed_login",
    "severity": "high"
}
```

Important functions:

| Function | Purpose |
|---|---|
| `json.dumps()` | Python object to JSON string |
| `json.loads()` | JSON string to Python object |
| `json.dump()` | Write a Python object as JSON to a file |
| `json.load()` | Read JSON data from a file |

Example of decoding:

```python
import json

json_text = '{"username": "admin", "severity": "high"}'
alert_data = json.loads(json_text)

print(alert_data["username"])
print(alert_data["severity"])
```

Output:

```text
admin
high
```

### 3.6 re — regular expressions

Regular expressions help search for text patterns. The `re` module is useful for extracting candidate indicators from unstructured text.

```python
import re

log = "Failed login detected from 192.168.1.105"

ip_candidates = re.findall(
    r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    log
)

print(ip_candidates)
```

Output:

```text
['192.168.1.105']
```

This pattern finds IPv4-shaped strings, but it does not validate that each octet is between 0 and 255. Pattern matching and full data validation are different tasks.

### 3.7 statistics

```python
import statistics

sales = [1200, 1500, 1800, 2000, 2500]

print("Mean:", statistics.mean(sales))
print("Median:", statistics.median(sales))
```

Output:

```text
Mean: 1800
Median: 1800
```

## 4. Creating your own module

You can create a Python file and import it from another file.

Project structure:

```text
my_project/
├── main.py
└── calculator.py
```

**calculator.py**

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

**main.py**

```python
import calculator

print(calculator.add(10, 20))
print(calculator.multiply(5, 4))
```

Output:

```text
30
20
```

You can also import selected functions:

```python
from calculator import add, multiply

print(add(10, 20))
print(multiply(5, 4))
```

### Creating files in Google Colab

In a Colab cell, use the `%%writefile` magic to create a Python file:

```python
%%writefile calculator.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

Then import it in another cell:

```python
import calculator

print(calculator.add(10, 20))
```

If you edit a module after importing it in a notebook, the notebook may still hold the previously imported version. You can reload it with:

```python
import importlib
importlib.reload(calculator)
```

---

# Part 2 — Packages

## 5. What is a package?

A **package** is a way to organize related Python modules in a directory hierarchy. A package can contain modules and subpackages.

Remember:

- **Module:** Usually one Python `.py` file.
- **Package:** A directory that groups related modules and possibly subpackages.
- **Subpackage:** A package inside another package.

Example:

```text
security_toolkit/
├── __init__.py
├── log_analyzer.py
├── ip_checker.py
└── alert_report.py
```

Here, `security_toolkit` is the package. The three `.py` files are modules.

### Why use packages?

- Organize a larger project into logical areas.
- Separate responsibilities.
- Make code easier to maintain and test.
- Reuse functionality across different parts of a project.
- Support nested project structures through subpackages.

## 6. Understanding __init__.py

In a traditional regular package, `__init__.py` marks the directory as a package and can contain initialization code or selected imports.

It can be empty:

```python
# __init__.py
```

Modern Python also supports **namespace packages**, which can work without an `__init__.py` file. For beginner projects, using `__init__.py` is a clear and familiar approach.

## 7. Creating your own package — step by step

Let's build a small simulated SOC toolkit.

Project structure:

```text
project/
├── main.py
└── security_toolkit/
    ├── __init__.py
    ├── log_analyzer.py
    ├── ip_checker.py
    └── alert_report.py
```

### File 1 — security_toolkit/log_analyzer.py

```python
def count_failed_logins(logs):
    count = 0

    for log in logs:
        if "failed" in log.lower():
            count += 1

    return count
```

### File 2 — security_toolkit/ip_checker.py

```python
def check_ip(ip):
    simulated_suspicious_ips = [
        "192.168.1.100",
        "10.0.0.50"
    ]

    if ip in simulated_suspicious_ips:
        return "Flagged in simulated test list"

    return "Not present in simulated test list"
```

This is only a local demonstration list, not a real threat-intelligence reputation service.

### File 3 — security_toolkit/alert_report.py

```python
def generate_alert(message, severity):
    return {
        "message": message,
        "severity": severity
    }
```

### File 4 — security_toolkit/__init__.py

```python
# Package initialization file
```

### File 5 — main.py

```python
from security_toolkit.log_analyzer import count_failed_logins
from security_toolkit.ip_checker import check_ip
from security_toolkit.alert_report import generate_alert

logs = [
    "alice failed login",
    "bob successful login",
    "charlie failed login"
]

print("Failed logins:", count_failed_logins(logs))
print(check_ip("192.168.1.100"))

alert = generate_alert(
    "Multiple failed logins",
    "High"
)

print(alert)
```

Output:

```text
Failed logins: 2
Flagged in simulated test list
{'message': 'Multiple failed logins', 'severity': 'High'}
```

This example demonstrates how multiple modules can be organized into one package and used by a main program.

### Creating the package in Google Colab

Run the following in a Colab cell to create the folders and files:

```python
import os

os.makedirs("security_toolkit", exist_ok=True)

with open("security_toolkit/__init__.py", "w") as file:
    file.write("# Security toolkit package\n")

with open("security_toolkit/log_analyzer.py", "w") as file:
    file.write('''def count_failed_logins(logs):
    return sum("failed" in log.lower() for log in logs)
''')

with open("security_toolkit/ip_checker.py", "w") as file:
    file.write('''def check_ip(ip):
    suspicious_ips = ["192.168.1.100", "10.0.0.50"]
    if ip in suspicious_ips:
        return "Flagged in simulated test list"
    return "Not present in simulated test list"
''')

with open("security_toolkit/alert_report.py", "w") as file:
    file.write('''def generate_alert(message, severity):
    return {"message": message, "severity": severity}
''')
```

Then import and test:

```python
from security_toolkit.log_analyzer import count_failed_logins
from security_toolkit.ip_checker import check_ip
from security_toolkit.alert_report import generate_alert

logs = ["alice failed login", "bob successful login"]

print(count_failed_logins(logs))
print(check_ip("192.168.1.100"))
print(generate_alert("Repeated login failures", "High"))
```

## 8. Different ways to import from a package

Assume the package structure from the previous section.

### Method 1 — Import a module from a package

```python
import security_toolkit.log_analyzer

logs = ["alice failed login"]
print(security_toolkit.log_analyzer.count_failed_logins(logs))
```

### Method 2 — Import a specific function

```python
from security_toolkit.log_analyzer import count_failed_logins

print(count_failed_logins(["alice failed login"]))
```

### Method 3 — Import a module using an alias

```python
import security_toolkit.log_analyzer as la

print(la.count_failed_logins(["alice failed login"]))
```

### Method 4 — Import a module from the package

```python
from security_toolkit import ip_checker

print(ip_checker.check_ip("192.168.1.100"))
```

## 9. What is a subpackage?

A **subpackage** is a package nested inside another package. It helps organize larger applications into smaller areas.

Example:

```text
security_toolkit/
├── __init__.py
├── log_analysis/
│   ├── __init__.py
│   ├── windows_logs.py
│   └── linux_logs.py
└── threat_intelligence/
    ├── __init__.py
    ├── ip_reputation.py
    └── ioc_extractor.py
```

In this structure:
- `security_toolkit` is the main package.
- `log_analysis` and `threat_intelligence` are subpackages.
- `windows_logs.py`, `linux_logs.py`, and the other `.py` files are modules.

Example import:

```python
from security_toolkit.threat_intelligence.ioc_extractor import extract_iocs
```

This assumes that the function `extract_iocs()` is defined in `ioc_extractor.py`.

## 10. Modules, packages, libraries, and frameworks

These terms are related, but they are not interchangeable.

| Term | Meaning | Example |
|---|---|---|
| Function | A reusable block of code that performs a task | `print()`, `add()` |
| Class | A definition for creating objects | A custom `Alert` class |
| Module | A Python file containing code | `calculator.py`, `json` |
| Package | Organizes related modules and subpackages | `security_toolkit`, `pandas` |
| Library | Reusable code made available to developers; may contain modules and packages | Pandas |
| Framework | Provides a structure and conventions for building an application | Django |

A library may be distributed as one or more packages. The terms can overlap in everyday Python usage.

---

# Part 3 — External Packages and pip

## 11. Built-in standard library vs third-party packages

| Category | Examples | Installation |
|---|---|---|
| Python standard library | `os`, `json`, `datetime`, `re` | Included with Python |
| Third-party packages | `pandas`, `numpy`, `requests` | Usually installed separately |
| Your own modules/packages | `calculator.py`, `security_toolkit` | Created in your project |

## 12. What is pip?

**pip** is the standard package installer commonly used to install Python packages from the Python Package Index (PyPI) or other configured sources.

In Google Colab:

```python
!pip install pandas
```

Then import it:

```python
import pandas as pd

data = [10, 20, 30, 40]
series = pd.Series(data)

print(series)
```

Output:

```text
0    10
1    20
2    30
3    40
dtype: int64
```

Other useful commands:

```bash
pip --version
pip show pandas
pip list
pip uninstall pandas
```

In notebooks, prefix shell commands with `!` when appropriate, for example `!pip show pandas`.

Only install packages from sources you trust. In real projects, keep track of dependencies so that the environment can be reproduced.

---

# Part 4 — Real-world applications

## 13. SOC application — Small security log analyzer

The following is a learning example using **simulated security logs**. It is not production detection logic.

```python
import json
import re
from datetime import datetime

logs = [
    "Failed login from 192.168.1.10",
    "Failed login from 192.168.1.10",
    "Successful login from 192.168.1.20",
    "Failed login from 192.168.1.10"
]

failed_ips = []

for log in logs:
    if "Failed login" in log:
        candidates = re.findall(
            r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
            log
        )

        if candidates:
            failed_ips.append(candidates[0])

report = {
    "timestamp": datetime.now().isoformat(),
    "total_failed_logins": len(failed_ips),
    "unique_source_ips": sorted(set(failed_ips))
}

print(json.dumps(report, indent=4))
```

Expected key values:

```text
total_failed_logins: 3
unique_source_ips: ['192.168.1.10']
```

Modules used:

| Module | Responsibility |
|---|---|
| `re` | Extract candidate IP strings |
| `datetime` | Add a timestamp |
| `json` | Format the report |

A real detection would also need time-window analysis, source/destination context, validation, and correlation with other events.

## 14. Data Analytics application — Sales summary

```python
import statistics

sales = [1200, 1500, 1800, 2000, 2500]

print("Mean:", statistics.mean(sales))
print("Median:", statistics.median(sales))
print("Maximum:", max(sales))
print("Minimum:", min(sales))
```

Output:

```text
Mean: 1800
Median: 1800
Maximum: 2500
Minimum: 1200
```

Later, you will use Pandas and NumPy for larger datasets, data cleaning, analysis, and transformations.

---

# Part 5 — Practical exercises

Use Google Colab. For file and package creation, use `%%writefile`, `open()`, or `os.makedirs()` as demonstrated above.

## Module exercises

1. Import the `math` module and calculate the square root of 144 and factorial of 6.
2. Import `random` and generate five random integers between 1 and 100.
3. Use `datetime` to print the current date and time, and extract the year and month.
4. Create a dictionary containing a username, IP address, and severity. Convert it into a JSON string using `json.dumps()`.
5. Given the text `Alert: suspicious activity from 10.0.0.25`, extract the IP-shaped string using `re.findall()`.
6. Given a list of five sales values, calculate the mean and median using `statistics`.
7. Use `os.getcwd()` and `os.listdir()` to display your current directory and its contents.

## Package exercises

8. Create a package named `my_calculator` containing `addition.py` and `subtraction.py`.
9. Define an `addition()` function in the first module and a `subtract()` function in the second.
10. Import both functions into a separate `main.py` file and execute them.
11. Create a package named `soc_toolkit` containing `log_analyzer.py` and `ip_checker.py`.
12. Create a subpackage named `threat_intelligence` inside `soc_toolkit` and add an `ioc_extractor.py` module. Define a simple function in it and import that function into your main program.

---

# Part 6 — Quick quiz

Answer these questions after completing the lesson:

1. What is a Python module?
2. What is a Python package?
3. What is the main difference between a module and a package?
4. What does `import math as m` do?
5. What is the conventional alias for Pandas?
6. Which module is useful for extracting text patterns?
7. What does `json.loads()` do?
8. What is the purpose of `__init__.py` in a traditional regular package?
9. What is a subpackage?
10. What is pip used for?

---

# Key points to remember

1. A module is generally a single Python `.py` file containing reusable code.
2. A package organizes related modules in a directory hierarchy.
3. A subpackage is a package nested inside another package.
4. `import` loads a module or package functionality.
5. `from ... import ...` imports selected names.
6. `as` creates an alias.
7. The standard library is included with Python; third-party packages are usually installed separately.
8. pip is commonly used to install third-party packages.
9. `os`, `re`, `json`, and `datetime` are useful in SOC scripting.
10. Pandas and NumPy are important tools for Data Analytics.

## Lesson 13 completion checklist

- [ ] Understand what a module is.
- [ ] Import complete modules and selected functions.
- [ ] Use aliases correctly.
- [ ] Practise standard-library modules.
- [ ] Create and import your own module.
- [ ] Understand packages and `__init__.py`.
- [ ] Create a package with multiple modules.
- [ ] Import from a package.
- [ ] Understand subpackages.
- [ ] Understand pip and third-party packages.
- [ ] Complete the practical exercises and quiz.

**Next lesson:** Lesson 14 — Debugging and Testing in Python.
