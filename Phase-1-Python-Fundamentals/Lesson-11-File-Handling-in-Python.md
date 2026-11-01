# Lesson 11 — File Handling in Python

**Phase:** 1 — Python Fundamentals  
**Level:** Beginner  
**Environment:** Google Colab compatible  
**Applications:** SOC operations and Data Analytics

## 1. Theory Notes

### What is file handling?
File handling means using Python to create, read, write, append, and process files. It is useful for reading security logs, saving investigation reports, processing datasets, and storing analysis results.

### File modes

| Mode | Meaning |
|---|---|
| `r` | Read an existing file |
| `w` | Write; creates a file or overwrites existing content |
| `a` | Append content without deleting existing content |
| `x` | Create a new file; fails if it already exists |
| `r+` | Read and write |

**Warning:** `w` overwrites existing content.

### Opening and closing files

Use `open()` to open a file. Prefer the `with open()` context manager because it closes the file automatically when the block finishes.

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

### Reading methods

- `read()`: reads the entire file and returns a string.
- `readline()`: reads one line.
- `readlines()`: returns all lines as a list.

```python
with open("example.txt", "r") as file:
    content = file.read()

with open("example.txt", "r") as file:
    first_line = file.readline()

with open("example.txt", "r") as file:
    lines = file.readlines()
```

### Writing and appending

```python
# Create or overwrite a file
with open("report.txt", "w") as file:
    file.write("SOC Investigation Report")

# Add content without overwriting
with open("report.txt", "a") as file:
    file.write("\nInvestigation completed.")
```

Use `\n` to insert a new line.

### File paths

A file path tells Python where a file is stored. Examples:

- `"report.txt"`
- `"datasets/login_logs.txt"`
- `"/content/login_logs.txt"`

In Google Colab, uploaded files commonly appear under `/content/`.

## 2. Examples with explanations

### Example 1 — Create and read a file

```python
with open("test.txt", "w") as file:
    file.write("Learning Python File Handling")

with open("test.txt", "r") as file:
    content = file.read()

print(content)
```

Output:
```text
Learning Python File Handling
```

The first block creates the file and writes text. The second opens it in read mode.

### Example 2 — Write multiple lines

```python
with open("notes.txt", "w") as file:
    file.write("Python Fundamentals\n")
    file.write("File Handling\n")
    file.write("SOC Automation\n")
```

### Example 3 — Read line by line

```python
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())
```

Output:
```text
Python Fundamentals
File Handling
SOC Automation
```

`strip()` removes surrounding whitespace, including the newline character.

### Example 4 — Append content

```python
with open("notes.txt", "a") as file:
    file.write("Data Analytics\n")

with open("notes.txt", "r") as file:
    print(file.read())
```

Output:
```text
Python Fundamentals
File Handling
SOC Automation
Data Analytics
```

## 3. Real-world applications

### A. SOC — analyse simulated login logs

The following is a small, simulated log dataset:

```text
10:00,admin,FAILED,192.168.1.10
10:02,admin,FAILED,192.168.1.10
10:03,user1,SUCCESS,192.168.1.20
10:05,admin,FAILED,192.168.1.10
10:06,admin,SUCCESS,192.168.1.10
```

Create the file and count failed logins:

```python
logs = """10:00,admin,FAILED,192.168.1.10
10:02,admin,FAILED,192.168.1.10
10:03,user1,SUCCESS,192.168.1.20
10:05,admin,FAILED,192.168.1.10
10:06,admin,SUCCESS,192.168.1.10"""

with open("login_logs.txt", "w") as file:
    file.write(logs)

failed_count = 0

with open("login_logs.txt", "r") as file:
    for line in file:
        if "FAILED" in line:
            failed_count += 1

print("Failed login attempts:", failed_count)
```

Output:
```text
Failed login attempts: 3
```

**SOC takeaway:** This is a basic log-processing example. Real investigations should also examine usernames, source IPs, timestamps, successful logins, and subsequent activity.

### B. Data Analytics — read sales data

```python
sales_data = """200
450
150
300
500"""

with open("sales.txt", "w") as file:
    file.write(sales_data)

total = 0
count = 0

with open("sales.txt", "r") as file:
    for line in file:
        sale = int(line.strip())
        total += sale
        count += 1

average = total / count if count > 0 else 0

print("Total sales:", total)
print("Average sales:", average)
```

Output:
```text
Total sales: 1600
Average sales: 320.0
```

## 4. Handling file errors

Trying to read a missing file raises `FileNotFoundError`. Use `try-except` to handle it gracefully.

```python
try:
    with open("unknown.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File does not exist.")
```

Output:
```text
File does not exist.
```

## 5. Practical exercises

Try these in Google Colab.

1. **Create a file:** Create `student.txt` and write your name, course, and graduation year. Read and print its contents.
2. **Read line by line:** Create a file containing five different names. Read it line by line and print each name.
3. **Append content:** Create `activities.txt` with two activities. Append two more without deleting the original content.
4. **Count words:** Create a text file containing a paragraph. Read it and count the total words. *Hint:* use `.split()` and `len()`.
5. **SOC log investigation:** Create a file containing these simulated events and count failed logins, successful logins, and total events.

   ```text
   admin,FAILED,192.168.1.10
   admin,FAILED,192.168.1.10
   user1,SUCCESS,192.168.1.20
   admin,FAILED,192.168.1.10
   user2,SUCCESS,192.168.1.30
   ```

6. **Identify suspicious IPs:** Read the same log file and identify IP addresses associated with failed login attempts.
7. **Generate a report:** Create `soc_report.txt` containing total events, failed attempts, successful attempts, and investigation status.
8. **Handle missing files:** Try reading `security_logs.txt`. If it does not exist, display a meaningful message using `try-except`.

## 6. Quick quiz

1. Which mode opens a file for reading?
2. Which mode adds content without overwriting existing content?
3. Which method reads the entire file?
4. What is the benefit of `with open()`?
5. Which error occurs when a requested file is missing?

**Answers:** 1. `r`  2. `a`  3. `read()`  4. It automatically closes the file  5. `FileNotFoundError`

## 7. Key points to remember

1. `open()` opens files.
2. `read()` reads the entire file.
3. `readline()` reads one line.
4. `readlines()` returns lines as a list.
5. `write()` creates or overwrites content.
6. `a` mode appends without overwriting.
7. `with open()` automatically closes files.
8. Use `try-except` to handle missing files.

**Next lesson:** Lesson 12 — Exception Handling in Python.
