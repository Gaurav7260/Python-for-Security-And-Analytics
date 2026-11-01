# Lesson 10 — Functions in Python

**Phase:** 1 — Python Fundamentals  
**Level:** Beginner  
**Environment:** Google Colab compatible  
**Applications:** SOC automation and Data Analytics

## 1. Theory Notes

### What is a function?

A function is a reusable block of code that performs a particular task. Functions help organize programs, avoid repeating code, and make scripts easier to test and maintain.

### Defining and calling a function

Use the `def` keyword to define a function. The indented code beneath it is the function body.

```python
def welcome():
    print("Welcome to Python")

welcome()
```

Output:
```text
Welcome to Python
```

Defining a function does not execute it. Calling the function by its name followed by parentheses runs its code.

### Parameters and arguments

A **parameter** is a variable listed in the function definition. An **argument** is the value passed when the function is called.

```python
def greet(name):          # name is a parameter
    print("Hello", name)

greet("Gourav")           # "Gourav" is an argument
```

Output:
```text
Hello Gourav
```

### Functions with multiple parameters

```python
def add_numbers(a, b):
    print(a + b)

add_numbers(10, 20)
```

Output:
```text
30
```

### The return statement

`return` sends a result back to the part of the program that called the function. This lets you store the result or use it in another calculation.

```python
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print(result)
```

Output:
```text
30
```

**Difference between `print()` and `return`:**
- `print()` displays information on the screen.
- `return` gives a value back to the caller.
- A function without an explicit `return` statement returns `None`.

### Default parameters

A parameter can have a default value. The default is used when the caller does not supply that argument.

```python
def greet(name="User"):
    print("Hello", name)

greet()
greet("Aman")
```

Output:
```text
Hello User
Hello Aman
```

### Keyword arguments

You can pass arguments by naming the parameters. This makes calls clearer and allows you to specify them in a different order.

```python
def describe_alert(username, severity):
    print(username, severity)

describe_alert(severity="High", username="admin")
```

### Local and global variables

- A **local variable** is created inside a function and is normally available only inside that function.
- A **global variable** is defined outside functions and can be read inside them.

```python
status = "Under investigation"  # global variable

def show_status():
    message = "Alert detected"  # local variable
    print(message)
    print(status)

show_status()
```

Avoid changing global variables unnecessarily. Passing values through parameters and returning results usually makes functions easier to understand and test.

### Built-in and user-defined functions

- **Built-in functions:** provided by Python, such as `print()`, `len()`, `sum()`, `max()`, and `min()`.
- **User-defined functions:** created by programmers using `def`.

## 2. Examples with explanations

### Example 1 — Calculate a square

```python
def square(number):
    return number * number

print(square(5))
print(square(8))
```

Output:
```text
25
64
```

The function accepts a number and returns its square.

### Example 2 — Check whether a number is even or odd

```python
def check_number(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_number(10))
print(check_number(7))
```

Output:
```text
Even
Odd
```

The modulo operator `%` gives the remainder. An even number has a remainder of zero when divided by two.

### Example 3 — Calculate revenue

```python
def calculate_revenue(price, quantity):
    return price * quantity

revenue = calculate_revenue(500, 4)
print("Total revenue:", revenue)
```

Output:
```text
Total revenue: 2000
```

The function can be reused for different prices and quantities.

## 3. Real-world applications

### A. SOC example — count failed logins

```python
def count_failed_logins(events):
    failed_count = 0

    for event in events:
        if event == "FAILED":
            failed_count += 1

    return failed_count

login_events = ["FAILED", "SUCCESS", "FAILED", "FAILED", "SUCCESS"]

result = count_failed_logins(login_events)
print("Failed login attempts:", result)
```

Output:
```text
Failed login attempts: 3
```

**Explanation:** The function accepts a list of login events, counts the entries marked `FAILED`, and returns the count. This is a simplified, illustrative example of reusable log-analysis logic.

### B. SOC example — classify alert severity

```python
def classify_alert(attempts):
    if attempts >= 10:
        return "High"
    elif attempts >= 5:
        return "Medium"
    else:
        return "Low"

print(classify_alert(12))
print(classify_alert(7))
print(classify_alert(2))
```

Output:
```text
High
Medium
Low
```

This is a basic rule-based demonstration, not a complete production detection rule. Real alert severity should consider additional context such as time window, source, affected account, and other correlated events.

### C. Data Analytics example — calculate average sales

```python
def calculate_average(sales):
    if len(sales) == 0:
        return 0

    return sum(sales) / len(sales)

sales_data = [200, 450, 150, 300, 500]

average = calculate_average(sales_data)
print("Average sales:", average)
```

Output:
```text
Average sales: 320.0
```

The empty-list check prevents division by zero.

## 4. Practical exercises

Try these in Google Colab.

1. **Welcome function:** Create a function called `welcome()` that prints a welcome message. Call it three times.
2. **Personal greeting:** Create a function that accepts a name and prints a greeting.
3. **Addition:** Create a function that accepts two numbers and returns their sum.
4. **Square:** Create a function that accepts a number and returns its square.
5. **Even or odd:** Create a function that accepts a number and returns `"Even"` or `"Odd"`.
6. **SOC failed-login counter:** Create a function that accepts a list of login events and returns the number of failed attempts.
7. **Sales average:** Create a function that accepts a list of sales values and returns their average. Handle an empty list safely.
8. **Alert classification:** Create `classify_alert(attempts)` that returns:
   - `"High"` for 10 or more attempts.
   - `"Medium"` for 5–9 attempts.
   - `"Low"` for fewer than 5 attempts.

## 5. Quick quiz

1. Which keyword is used to define a function?
2. What is the difference between a parameter and an argument?
3. What does `return` do?
4. What does a function return if it has no explicit `return` statement?
5. What is a default parameter?
6. What is the difference between a local and a global variable?

**Answers:**
1. `def`
2. A parameter is named in the function definition; an argument is supplied when calling it.
3. It sends a value back to the caller.
4. `None`
5. A parameter with a predefined value used when no argument is supplied for it.
6. A local variable belongs to its function scope; a global variable is defined outside functions.

## 6. Key points to remember

1. Functions make code reusable and organized.
2. Use `def` to define a function.
3. Call a function using its name and parentheses.
4. Parameters receive values; arguments are passed during a call.
5. `return` sends a result back; `print()` displays it.
6. A function without an explicit return statement returns `None`.
7. Default parameters provide fallback values.
8. Prefer parameters and return values over unnecessary global-variable changes.

**Next lesson:** Lesson 11 — File Handling in Python.
