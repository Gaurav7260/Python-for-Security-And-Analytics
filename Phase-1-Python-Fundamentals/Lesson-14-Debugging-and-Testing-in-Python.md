# Lesson 14 — Debugging and Testing in Python

**Phase:** 1 — Python Fundamentals  
**Focus:** Finding bugs, understanding errors, debugging programs, and testing code  
**Practice environment:** Google Colab or local Python 3

## Learning objectives

By the end of this lesson, you should be able to:

- Explain debugging and distinguish syntax, runtime, and logical errors.
- Read a Python traceback and locate the source of an error.
- Debug code using `print()`, `type()`, `repr()`, and `breakpoint()`.
- Use Python's `logging` module to record application activity.
- Understand test cases and common testing types.
- Test functions using `assert` and the built-in `unittest` framework.
- Understand the purpose of `pytest`, regression testing, code coverage, and TDD.
- Build and test simple SOC and Data Analytics functions.

---

## 1. What is debugging?

**Debugging** is the systematic process of identifying, analyzing, locating, and fixing errors (bugs) in a program.

A bug is an error or defect that causes a program to behave differently from what is expected.

A program can run without crashing and still contain a logical bug.

### Example: a logical error

```python
failed_logins = 10
successful_logins = 5

total = failed_logins - successful_logins

print(total)
```

Output:

```text
5
```

If the goal is to calculate total login attempts, the correct operation is addition:

```python
total = failed_logins + successful_logins
print(total)
```

Output:

```text
15
```

The first program runs successfully but gives the wrong answer. Debugging is not only about fixing crashes; it also involves finding incorrect results.

## 2. Three common categories of programming errors

| Error type | Meaning | Example |
|---|---|---|
| Syntax error | Python grammar is incorrect | Missing colon |
| Runtime error | An error occurs while executing | Dividing by zero |
| Logical error | Program runs but gives an incorrect result | Subtraction instead of addition |

### Syntax error

```python
if 10 > 5
    print("Greater")
```

The condition is missing a colon.

Correct:

```python
if 10 > 5:
    print("Greater")
```

### Runtime error

```python
number = 10 / 0
```

This raises `ZeroDivisionError`.

### Logical error

```python
price = 100
quantity = 5

total = price + quantity
print(total)
```

Output: `105`

Correct calculation:

```python
total = price * quantity
print(total)
```

Output: `500`

## 3. Reading and understanding error messages

### What is a traceback?

A **traceback** is Python's report showing where an exception occurred and the sequence of function calls that led to it.

```python
def calculate_average(total, count):
    return total / count

result = calculate_average(100, 0)
print(result)
```

This raises:

```text
ZeroDivisionError: division by zero
```

Important parts of a traceback:

- **File:** The file in which the error occurred.
- **Line number:** The line that triggered the error.
- **Function name:** The function being executed, if applicable.
- **Exception type:** The category of error.
- **Error message:** A description of what went wrong.

When an error occurs in Google Colab, the traceback appears below the cell that failed.

### Questions to ask when debugging

1. What was the expected output?
2. What output did I actually receive?
3. Which line caused the issue?
4. What values were passed into that line?
5. Is it a syntax, runtime, or logical error?
6. Can I reproduce the problem consistently?

## 4. Debugging techniques

### 4.1 Using `print()` for debugging

Printing variable values at different stages is a simple way to understand program execution.

```python
failed_logins = 7
threshold = 5

print("Failed logins:", failed_logins)
print("Threshold:", threshold)

if failed_logins >= threshold:
    print("High failed-login activity detected")
else:
    print("Normal activity")
```

Output:

```text
Failed logins: 7
Threshold: 5
High failed-login activity detected
```

Use print statements to check:

- Whether a variable contains the expected value.
- Whether a condition is being executed.
- Whether a loop is processing all records.
- Whether a function is returning the expected result.

Remove unnecessary debugging prints from final code or replace them with appropriate logging.

### 4.2 Checking variable types

Sometimes a bug occurs because a variable has an unexpected data type.

Remember that `input()` returns a string, even when the user enters a number.

```python
failed_logins = input("Enter failed login count: ")

print(type(failed_logins))
```

If the user enters `10`, the output is:

```text
<class 'str'>
```

This causes a problem:

```python
failed_logins = "10"
print(failed_logins + 5)
```

This raises `TypeError` because Python cannot concatenate a string and an integer.

Correct:

```python
failed_logins = int("10")
print(failed_logins + 5)
```

Output: `15`

Useful debugging functions:

| Function | Purpose |
|---|---|
| `print()` | Displays values |
| `type()` | Identifies data type |
| `len()` | Checks length |
| `isinstance()` | Checks whether an object belongs to a type |
| `repr()` | Displays an object's representation, useful for spotting spaces and escape characters |

Example:

```python
username = "admin "

print(repr(username))
print(len(username))
print(type(username))
print(isinstance(username, str))
```

Output:

```text
'admin '
6
<class 'str'>
True
```

There is an extra space after `admin`. It can cause a username comparison to fail.

### 4.3 Using `breakpoint()`

Python provides a built-in debugging function called `breakpoint()`. It pauses program execution and lets you inspect variables and execute debugger commands.

```python
failed_logins = 8
threshold = 5

breakpoint()

if failed_logins >= threshold:
    print("Suspicious activity")
else:
    print("Normal activity")
```

Useful debugger commands:

| Command | Purpose |
|---|---|
| `n` | Execute the next line |
| `s` | Step into a function |
| `c` | Continue execution |
| `p variable` | Print a variable |
| `l` | Show nearby source code |
| `q` | Quit debugging |

For example, enter `p failed_logins` to inspect its value.

**Google Colab note:** Interactive debugger behavior can vary in notebook environments. Start with print-based debugging or run a small Python script in a terminal if the debugger does not behave as expected.

### 4.4 Debugging with `logging`

In real applications, developers often use the `logging` module instead of many print statements. Logging records program events with severity levels.

Five commonly used levels:

| Level | Meaning |
|---|---|
| `DEBUG` | Detailed diagnostic information |
| `INFO` | Normal program activity |
| `WARNING` | Something unexpected happened, but execution can continue |
| `ERROR` | An operation failed |
| `CRITICAL` | A serious failure that may prevent the program from continuing |

Example:

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)

failed_logins = 8

logging.debug("Checking failed login count")
logging.info("Login analysis started")

if failed_logins >= 5:
    logging.warning("High failed-login activity detected")
else:
    logging.info("Login activity is normal")
```

Example output:

```text
DEBUG: Checking failed login count
INFO: Login analysis started
WARNING: High failed-login activity detected
```

Logging helps a SOC automation script record when processing started, how many records were processed, whether malformed records were skipped, whether a detection condition was triggered, and whether the script encountered an error.

**Important distinction:** Application logging records what your script does. Security logs record activity from systems, users, and network devices.

## 5. Introduction to software testing

**Software testing** is the process of checking whether a program behaves as expected under different conditions.

Debugging focuses on finding and fixing defects. Testing helps discover defects and verify that the program works correctly.

### What is a test case?

A **test case** is a specific input, condition, or action used to verify expected behavior.

A test case normally contains:

1. Test input.
2. Expected output.
3. Actual output.
4. Result: Pass or Fail.

Example for a failed-login detector:

| Test input | Expected result |
|---:|---|
| 2 | Normal |
| 5 | Suspicious |
| 10 | Suspicious |
| 0 | Normal |
| -1 | Invalid |

### Common testing types

**Unit testing:** Tests one small component, such as a function.

**Integration testing:** Checks whether multiple components work together. For example, whether a log-reading function passes records correctly to an analysis function.

**Functional testing:** Checks whether the program performs the required functionality. For example, whether it identifies repeated failed logins.

**Regression testing:** Checks whether previously working functionality still works after code changes.

**Edge-case testing:** Checks unusual or boundary inputs, such as empty lists, zero, negative numbers, missing dictionary keys, invalid dates, and very large files.

## 6. Testing with `assert`

An **assertion** checks whether a condition is true.

Syntax:

```python
assert condition, "Error message"
```

If the condition is true, Python continues. If false, Python raises `AssertionError`.

Example:

```python
age = 20

assert age >= 18, "Age must be at least 18"

print("Age validation successful")
```

Output:

```text
Age validation successful
```

If `age = 15`, the assertion raises:

```text
AssertionError: Age must be at least 18
```

### Testing a function with assertions

```python
def classify_alert(failed_logins):

    if failed_logins < 0:
        return "Invalid"

    elif failed_logins >= 5:
        return "Suspicious"

    else:
        return "Normal"
```

Test it:

```python
assert classify_alert(2) == "Normal"
assert classify_alert(5) == "Suspicious"
assert classify_alert(10) == "Suspicious"
assert classify_alert(0) == "Normal"
assert classify_alert(-1) == "Invalid"

print("All tests passed!")
```

Output:

```text
All tests passed!
```

These tests check normal input, the threshold boundary, a high value, zero, and invalid negative input.

**Important:** Assertions are useful for development checks. Do not use them as the only validation mechanism for untrusted input because Python can disable assertions when optimization is enabled.

## 7. Automated testing with `unittest`

Python includes a built-in testing framework called `unittest`. It lets you write test cases, execute multiple tests, and identify which tests pass or fail.

Basic example:

```python
import unittest

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(10 + 5, 15)

    def test_subtraction(self):
        self.assertEqual(10 - 5, 5)

if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
```

The output indicates that two tests ran successfully:

```text
Ran 2 tests

OK
```

The `argv` and `exit` arguments make this example suitable for running inside Google Colab.

### Important assertion methods in `unittest`

| Method | Purpose |
|---|---|
| `assertEqual(a, b)` | Checks whether two values are equal |
| `assertNotEqual(a, b)` | Checks whether two values are different |
| `assertTrue(x)` | Checks whether a condition is true |
| `assertFalse(x)` | Checks whether a condition is false |
| `assertIsNone(x)` | Checks whether a value is `None` |
| `assertIn(a, b)` | Checks whether an item exists in a collection |
| `assertRaises()` | Checks whether an expected exception occurs |

Example:

```python
import unittest

def divide(a, b):
    return a / b

class TestDivision(unittest.TestCase):

    def test_valid_division(self):
        self.assertEqual(divide(10, 2), 5)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

unittest.main(argv=["first-arg-is-ignored"], exit=False)
```

This checks normal behavior and verifies that division by zero raises the expected exception.

## 8. SOC practical — Debug and test a failed-login detector

**Scenario:** A SOC Analyst L1 receives authentication events and wants to identify IP addresses with five or more failed login attempts.

The following dataset is simulated for learning.

```python
import logging
from collections import Counter

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

login_logs = [
    {"ip": "192.168.1.10", "status": "failed"},
    {"ip": "192.168.1.10", "status": "failed"},
    {"ip": "192.168.1.10", "status": "failed"},
    {"ip": "192.168.1.10", "status": "failed"},
    {"ip": "192.168.1.10", "status": "failed"},
    {"ip": "192.168.1.20", "status": "success"},
    {"ip": "192.168.1.20", "status": "failed"},
    {"ip": "192.168.1.30", "status": "failed"}
]

def detect_brute_force(logs, threshold=5):

    if not isinstance(logs, list):
        raise TypeError("Logs must be a list")

    if threshold <= 0:
        raise ValueError("Threshold must be positive")

    failed_counts = Counter()

    for log in logs:

        if not isinstance(log, dict):
            logging.warning("Skipping invalid log record")
            continue

        if log.get("status") == "failed":
            ip = log.get("ip")

            if ip:
                failed_counts[ip] += 1

    alerts = {
        ip: count
        for ip, count in failed_counts.items()
        if count >= threshold
    }

    logging.info("Processed %d log records", len(logs))

    return alerts


result = detect_brute_force(login_logs)

print(result)
```

Output:

```text
{'192.168.1.10': 5}
```

What the program does:

1. Receives authentication logs.
2. Counts failed login attempts for each IP.
3. Ignores successful logins.
4. Skips malformed records.
5. Generates an alert when an IP reaches the threshold.

This is a basic rule-based demonstration, not a production-ready brute-force detection system. Real investigations need additional context, such as time windows, usernames, source reputation, and authentication patterns.

### Test the SOC detector

```python
import unittest

class TestBruteForceDetector(unittest.TestCase):

    def test_brute_force_detected(self):
        logs = [
            {"ip": "10.0.0.1", "status": "failed"}
            for _ in range(5)
        ]
        result = detect_brute_force(logs)
        self.assertEqual(result, {"10.0.0.1": 5})

    def test_normal_activity(self):
        logs = [
            {"ip": "10.0.0.2", "status": "failed"}
            for _ in range(3)
        ]
        result = detect_brute_force(logs)
        self.assertEqual(result, {})

    def test_successful_logins_ignored(self):
        logs = [
            {"ip": "10.0.0.3", "status": "success"}
        ]
        result = detect_brute_force(logs)
        self.assertEqual(result, {})

    def test_empty_logs(self):
        result = detect_brute_force([])
        self.assertEqual(result, {})

    def test_invalid_threshold(self):
        with self.assertRaises(ValueError):
            detect_brute_force([], threshold=0)


unittest.main(argv=["first-arg-is-ignored"], exit=False)
```

Expected result:

```text
Ran 5 tests

OK
```

## 9. Data Analytics practical — Debug and test sales calculations

**Scenario:** Calculate total and average sales from a list of sales values.

```python
def calculate_sales(sales):

    if not sales:
        return 0, 0

    total = sum(sales)
    average = total / len(sales)

    return total, average


sales = [1000, 2000, 1500, 2500]

total, average = calculate_sales(sales)

print("Total sales:", total)
print("Average sales:", average)
```

Output:

```text
Total sales: 7000
Average sales: 1750.0
```

Test it:

```python
import unittest

class TestSalesCalculator(unittest.TestCase):

    def test_total_sales(self):
        total, average = calculate_sales([100, 200, 300])
        self.assertEqual(total, 600)

    def test_average_sales(self):
        total, average = calculate_sales([100, 200, 300])
        self.assertEqual(average, 200)

    def test_empty_sales(self):
        total, average = calculate_sales([])
        self.assertEqual(total, 0)
        self.assertEqual(average, 0)

    def test_single_sale(self):
        total, average = calculate_sales([500])
        self.assertEqual(total, 500)
        self.assertEqual(average, 500)


unittest.main(argv=["first-arg-is-ignored"], exit=False)
```

Expected result:

```text
Ran 4 tests

OK
```

**Limitation:** This function assumes every value is a valid number. A real analytics pipeline should also validate data types, missing values, and negative or malformed values.

## 10. Additional testing concepts

### Test-driven development (TDD)

**Test-driven development** is an approach in which developers write tests before writing the actual implementation.

It generally follows three stages:

1. **Red — Write a failing test:** Create a test for functionality that does not exist yet.
2. **Green — Write the code:** Implement the minimum code required to pass the test.
3. **Refactor — Improve the code:** Improve readability and structure while keeping the tests passing.

### Code coverage

**Code coverage** measures how much of a program's code is executed during testing.

For example, if tests execute 80 out of 100 executable statements, approximate statement coverage is 80%.

However, 100% code coverage does not guarantee that a program is free from bugs. Tests must check meaningful inputs, outputs, and edge cases.

### What is pytest?

`pytest` is a popular third-party Python testing framework. It makes it easier to write and execute tests, particularly in larger projects.

Install it in a notebook:

```python
!pip install pytest
```

Create a module file:

```python
%%writefile example.py

def check_even(number):
    return number % 2 == 0
```

Create a test file:

```python
%%writefile test_example.py

from example import check_even

def test_even_number():
    assert check_even(10) == True

def test_odd_number():
    assert check_even(7) == False
```

Run:

```python
!pytest -v test_example.py
```

The output should show two passing tests. In Colab, run the file-creation cells before running pytest.

## 11. Practical exercises

Try these yourself in Google Colab before checking solutions.

### Exercise 1 — Identify the bug

Find and correct the error:

```python
failed = 10
successful = 5

total = failed - successful

print("Total login attempts:", total)
```

Expected output:

```text
Total login attempts: 15
```

### Exercise 2 — Debug the data type

Find the problem and correct the program so it calculates a numerical total:

```python
price = input("Enter product price: ")
quantity = 3

total = price * quantity

print(total)
```

### Exercise 3 — Debug a function

Find the logical error:

```python
def calculate_average(numbers):
    total = sum(numbers)
    average = total / 2
    return average

print(calculate_average([10, 20, 30, 40]))
```

Expected output: `25.0`

### Exercise 4 — Add exception handling

Create a division function that:

- Accepts two numbers.
- Handles division by zero.
- Handles invalid numeric input.
- Returns the correct division result when inputs are valid.

### Exercise 5 — SOC testing

Create a function called `classify_login_activity()`.

Requirements:

- 0–2 failed attempts: `Normal`
- 3–4 failed attempts: `Medium`
- 5 or more failed attempts: `High`
- Negative values: `Invalid`

Write at least five test cases using `assert`.

### Exercise 6 — SOC debugging challenge

The code is supposed to count failed login attempts by IP address. Find and fix the problems:

```python
logs = [
    {"ip": "10.0.0.1", "status": "failed"},
    {"ip": "10.0.0.1", "status": "failed"},
    {"ip": "10.0.0.2", "status": "success"},
    {"ip": "10.0.0.1", "status": "failed"}
]

failed_count = {}

for log in logs:
    ip = log["ip"]

    if log["status"] == "success":
        failed_count[ip] = failed_count.get(ip, 0) + 1

print(failed_count)
```

Expected result:

```text
{'10.0.0.1': 3}
```

### Exercise 7 — Data Analytics testing

Create a function that calculates total sales and average sales.

Test it with:

- `[100, 200, 300]`
- `[500]`
- `[]`
- `[1000, 2000, 3000, 4000]`

Use `unittest` and include at least four test methods.

### Exercise 8 — Mini testing project

Build a program that:

1. Reads a list of simulated login events.
2. Counts failed login attempts by IP.
3. Identifies IPs with five or more failed attempts.
4. Handles malformed records.
5. Uses logging to report processing activity.
6. Uses `unittest` to verify at least five scenarios.

Document the bugs you found during development and how you fixed them.

## 12. Quick quiz

1. What is debugging?
2. Which error occurs when Python divides a number by zero?
3. Which function pauses execution for interactive debugging?
4. Which testing type checks an individual function?
5. What does `assertEqual()` check?
6. Which logging level indicates a serious failure?
7. What is regression testing?
8. What does TDD stand for?

## 13. Important interview questions

1. What is debugging, and why is it important?
2. Differentiate syntax, runtime, and logical errors.
3. What is a traceback?
4. What is the difference between debugging and testing?
5. Explain unit testing and integration testing.
6. What is the purpose of Python's `assert` statement?
7. What is the difference between `unittest` and `pytest`?
8. What is regression testing?
9. Explain the purpose of the Python `logging` module.
10. What is test-driven development?

## 14. Key takeaways

| Concept | Remember |
|---|---|
| Debugging | Finding and fixing bugs |
| Traceback | Shows where an exception occurred |
| `print()` | Basic debugging technique |
| `breakpoint()` | Interactive debugging |
| `logging` | Records program activity |
| Test case | Input and expected behavior |
| `assert` | Checks a condition |
| `unittest` | Built-in testing framework |
| `pytest` | Third-party testing framework |
| Regression testing | Checks old functionality after changes |
| TDD | Write tests before implementation |

### Why this lesson matters

SOC automation scripts must not silently produce incorrect detections, and analytics scripts must not silently produce incorrect calculations. Debugging and testing help make your work more reliable and defensible.

---

**Progress:** Lessons 01–14 completed after finishing this lesson's practice.

**Next lesson:** Lesson 15 — To be introduced after Lesson 14 exercises and quiz are completed.
