# Lesson 12 — Exception Handling: Practical Exercise Answers

Try each problem independently before reviewing its solution.

## Exercise 1 — Division calculator

```python
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a / b)
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

## Exercise 2 — Age validation

```python
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print("Age:", age)
except ValueError as error:
    print("Invalid age:", error)
```

## Exercise 3 — List index handling

```python
items = ["Python", "SQL", "Power BI"]

try:
    index = int(input("Enter an index: "))
    print(items[index])
except ValueError:
    print("Enter an integer index.")
except IndexError:
    print("That index is outside the list.")
```

## Exercise 4 — Dictionary KeyError

```python
student = {"name": "Aman", "course": "B.Tech"}

try:
    print(student["grade"])
except KeyError as error:
    print("Key not found:", error)
```

## Exercise 5 — File handling with try, except, else and finally

A context manager is the cleanest way to ensure that the file is closed:

```python
try:
    with open("data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist.")
else:
    print(content)
finally:
    print("File operation completed.")
```

## Exercise 6 — Validate simulated SOC login records

```python
logs = [
    {"username": "alice", "status": "success"},
    {"username": "bob", "status": "failed"},
    {"username": "charlie", "status": "failed"},
    {"username": "david", "status": "success"},
    {"username": "", "status": "failed"},
]

valid_logs = []
invalid_logs = []

for log in logs:
    try:
        username = log["username"]
        status = log["status"]

        if not username:
            raise ValueError("Missing username")
        if status not in ["success", "failed"]:
            raise ValueError("Invalid status")

        valid_logs.append(log)
    except (KeyError, ValueError) as error:
        invalid_logs.append((log, str(error)))

print("Valid records:", len(valid_logs))
print("Invalid records:", len(invalid_logs))
```

Expected counts:
```text
Valid records: 4
Invalid records: 1
```

## Exercise 7 — Validate sales data

```python
sales = ["100", "200", "invalid", "300", "-50", "600"]
valid_sales = []
invalid_count = 0

for value in sales:
    try:
        amount = float(value)
        if amount < 0:
            raise ValueError("Negative sales value")
        valid_sales.append(amount)
    except ValueError as error:
        invalid_count += 1
        print("Invalid value:", value, "-", error)

if valid_sales:
    total = sum(valid_sales)
    average = total / len(valid_sales)
    print("Total:", total)
    print("Average:", average)

print("Valid values:", len(valid_sales))
print("Invalid values:", invalid_count)
```

Expected result:
```text
Total: 1200.0
Average: 300.0
Valid values: 4
Invalid values: 2
```

## Exercise 8 — Custom InvalidPasswordError

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
    result = validate_password("abc123")
    print(result)
except InvalidPasswordError as error:
    print("Error:", error)
```

Output:
```text
Error: Password must be at least 8 characters long.
```

For a valid password:

```python
print(validate_password("dhj26wssjw"))
```

Output:
```text
Password accepted
```

**Remember:** The success `return` must be outside the `if` block. If a function finishes without executing a `return` statement, Python returns `None`.

## Mini challenge — SOC login log processor

This is simulated practice data. It counts valid successful and failed login records while skipping malformed records.

```python
logs = [
    "alice,success",
    "bob,failed",
    "charlie,failed",
    "david,success",
    "invalid_record",
    ",failed",
]

success_count = 0
failed_count = 0
invalid_count = 0

for line in logs:
    try:
        parts = line.split(",")
        if len(parts) != 2:
            raise ValueError("Incorrect record format")

        username, status = parts
        if not username:
            raise ValueError("Missing username")

        if status == "success":
            success_count += 1
        elif status == "failed":
            failed_count += 1
        else:
            raise ValueError("Unknown login status")

    except ValueError as error:
        invalid_count += 1
        print("Skipped record:", line, "|", error)

print("\nSOC Login Summary")
print("Successful logins:", success_count)
print("Failed logins:", failed_count)
print("Invalid records:", invalid_count)
```

Expected counts:
- Successful logins: 2
- Failed logins: 2
- Invalid records: 2

## Key takeaways

- `try` contains code that may raise an exception.
- `except` handles a matching exception.
- `else` runs when no exception occurs in `try`.
- `finally` runs whether or not an exception occurs.
- `raise` triggers an exception.
- Custom exceptions make application-specific validation errors clearer.
- A function with no executed `return` statement returns `None`.
