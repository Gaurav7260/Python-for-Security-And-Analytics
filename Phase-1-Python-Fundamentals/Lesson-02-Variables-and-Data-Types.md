# Python Phase 1 — Lesson 2: Variables and Data Types

**Environment:** Google Colab  
**Format:** Theory notes → Examples → Practice

## Part 1 — Theory notes

### 1. Variables
A variable is a name that refers to a value in a program. Assignment uses `=`.

```python
failed_logins = 15
total_sales = 25000
```

### 2. Basic data types

| Type | Meaning | Example |
|---|---|---|
| `int` | Whole number | `25` |
| `float` | Decimal number | `3.14` |
| `str` | Text | `"Gourav"` |
| `bool` | Boolean | `True`, `False` |
| `NoneType` | No value assigned / absence of value | `None` |

An IP address is commonly represented as text in a basic log-analysis example, rather than a number for arithmetic.

### 3. The type() function
Use `type(value)` to inspect the type of a value.

```python
age = 21
print(type(age))  # <class 'int'>
```

### 4. Variable naming rules
- Names may contain letters, digits, and underscores.
- A name cannot start with a digit.
- Spaces are not allowed.
- Names are case-sensitive.
- Don't use reserved Python keywords as names.
- Prefer descriptive `snake_case` names such as `failed_login_count`.

## Part 2 — Examples

### Example 1: Create and print variables
```python
name = "Gourav"
age = 21
course = "B.Tech CSE"

print(name)
print(age)
print(course)
```

### Example 2: Inspect data types
```python
student_name = "Gourav"
graduation_year = 2027
percentage = 85.5
is_learning_python = True
assigned_project = None

print(type(student_name))
print(type(graduation_year))
print(type(percentage))
print(type(is_learning_python))
print(type(assigned_project))
```

### Example 3: Reassign a value
```python
failed_logins = 3
print(failed_logins)

failed_logins = 7
print(failed_logins)
```

### Example 4: Calculate a total
```python
product_price = 500
quantity = 4
total_cost = product_price * quantity
print(total_cost)  # 2000
```

### Example 5: Security event fields
```python
username = "admin"
failed_attempts = 8
source_ip = "192.168.1.25"
is_suspicious = True

print(username, failed_attempts, source_ip, is_suspicious)
```

This is illustrative data, not a real security event.

## Part 3 — Practice exercises

1. Create and print variables for your name, degree, and graduation year.
2. Create an integer, float, string, Boolean, and `None` variable. Print each variable's type.
3. Store a product price of 250 and quantity of 6. Calculate and print the total cost.
4. Create variables for a username, source IP, and failed-login count. Print their values.
5. Fix the errors below:
   ```python
   2name = "Gourav"
   student age = 21
   is_learning = true
   print(type("Gourav))
   ```

## Quick quiz
1. What is the type of `"2027"`? Answer: `str`.
2. Which Boolean value is correct? Answer: `True` with capital T.
3. What is the type of `15.5`? Answer: `float`.

## Key takeaways
- `=` assigns a value.
- Common types are `int`, `float`, `str`, `bool`, and `NoneType`.
- Use `type()` to inspect a type.
- Use clear variable names in `snake_case`.
