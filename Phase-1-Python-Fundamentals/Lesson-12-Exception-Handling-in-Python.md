# Lesson 12 — Exception Handling in Python

## 1. What is exception handling?

An **exception** is an error that occurs while a program is running and interrupts its normal flow. Exception handling lets us respond to runtime problems instead of allowing the program to terminate unexpectedly.

Examples include invalid integer conversion (`ValueError`), division by zero (`ZeroDivisionError`), a missing dictionary key (`KeyError`), and a missing file (`FileNotFoundError`).

### Errors vs exceptions
- **Syntax error:** Python cannot parse the code.
- **Runtime exception:** A problem occurs while valid code is executing.
- **Logical error:** The program runs but produces an incorrect result.

## 2. try and except

Put code that may fail inside `try`, and handle the expected exception in `except`.

```python
try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)
except ValueError:
    print("Please enter a valid whole number.")
```

Prefer specific exception types. A bare `except:` can hide unrelated programming errors.

## 3. Handling multiple exceptions

```python
try:
    number = int(input("Enter a number: "))
    print(100 / number)
except ValueError:
    print("Enter a valid integer.")
except ZeroDivisionError:
    print("The number cannot be zero.")
```

## 4. else and finally

- `else` runs only if the `try` block completes without an exception.
- `finally` runs whether an exception occurred or not. It is useful for cleanup.

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
else:
    print("You entered:", number)
finally:
    print("Program execution finished.")
```

## 5. Common exceptions

| Exception | Typical cause |
|---|---|
| `ValueError` | Invalid value supplied |
| `TypeError` | Operation uses an incompatible type |
| `ZeroDivisionError` | Division by zero |
| `IndexError` | Sequence index is out of range |
| `KeyError` | Dictionary key does not exist |
| `NameError` | Variable name is not defined |
| `FileNotFoundError` | Requested file does not exist |
| `AttributeError` | Object lacks the requested attribute |
| `ImportError` / `ModuleNotFoundError` | Import cannot be completed |
| `PermissionError` | Operation is not permitted |

## 6. Raising exceptions

Use `raise` when your code detects a condition that should be treated as an error.

```python
password = "abc"
if len(password) < 8:
    raise ValueError("Password must contain at least 8 characters.")
```

**Important:** `raise` immediately interrupts normal execution in the current path. Statements after it in that path will not run.

## 7. Creating a custom exception

A custom exception gives a meaningful name to an application-specific error. Define it by inheriting from `Exception`.

```python
class InvalidPasswordError(Exception):
    pass

def validate_password(password):
    if len(password) < 8:
        raise InvalidPasswordError(
            "Password must be at least 8 characters long."
        )

    return "Password accepted"

try:
    result = validate_password("dhj26wssjw")
    print(result)
except InvalidPasswordError as error:
    print("Error:", error)
```

Output:
```text
Password accepted
```

If the password is shorter than eight characters, the custom exception is raised and caught by the matching `except` block.

**Common return-value mistake:** If a function reaches its end without executing a `return` statement, Python returns `None`. Put the success return outside the invalid-input `if` block when it should run for every valid password.

## 8. SOC example — validating simulated login records

These are **simulated practice records**, not logs from a real organization.

```python
logs = [
    {"username": "alice", "status": "success"},
    {"username": "bob", "status": "failed"},
    {"username": "charlie", "status": "failed"},
    {"username": "david", "status": "success"},
    {"username": "", "status": "failed"},
]

valid_logs = []
invalid_count = 0

for log in logs:
    try:
        username = log["username"]
        status = log["status"]

        if not username:
            raise ValueError("Username is missing")
        if status not in ["success", "failed"]:
            raise ValueError("Unknown login status")

        valid_logs.append(log)
    except (KeyError, ValueError) as error:
        invalid_count += 1
        print("Invalid record:", error)

print("Valid records:", len(valid_logs))
print("Invalid records:", invalid_count)
```

This shows how validation and exception handling can prevent malformed records from breaking a log-processing workflow.

## 9. Data Analytics example — validating sales values

```python
sales = ["100", "250", "invalid", "400", "-50", "500"]
valid_sales = []
invalid_count = 0

for value in sales:
    try:
        amount = float(value)
        if amount < 0:
            raise ValueError("Sales amount cannot be negative")
        valid_sales.append(amount)
    except ValueError as error:
        invalid_count += 1
        print("Skipped value:", value, "| Reason:", error)

if valid_sales:
    print("Total:", sum(valid_sales))
    print("Average:", sum(valid_sales) / len(valid_sales))

print("Valid values:", len(valid_sales))
print("Invalid values:", invalid_count)
```

## 10. Best practices

1. Catch specific exceptions rather than hiding errors with a bare `except:`.
2. Keep the `try` block focused on operations that may fail.
3. Give clear, useful error messages.
4. Do not silently discard errors in security or data-processing workflows.
5. Use `finally` or context managers for cleanup.
6. Validate input before processing it.
7. Use custom exceptions when they make application logic clearer.

## Lesson checklist

- [ ] Understand exceptions and runtime errors.
- [ ] Use `try` and `except`.
- [ ] Handle multiple exception types.
- [ ] Understand `else` and `finally`.
- [ ] Recognize common built-in exceptions.
- [ ] Raise built-in exceptions.
- [ ] Create and catch custom exceptions.
- [ ] Apply exception handling to simulated SOC logs and sales data.

See [Lesson 12 — Exercise Answers](Lesson-12-Exercise-Answers.md) for practical solutions.
