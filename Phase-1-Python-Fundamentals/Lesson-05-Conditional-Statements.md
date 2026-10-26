# Python Phase 1 — Lesson 5: Conditional Statements

**Environment:** Google Colab  
**Format:** Theory notes → Examples → Practice

## Part 1 — Theory notes

### 1. What are conditionals?
Conditional statements run different code blocks depending on whether conditions evaluate to `True` or `False`. Python's main conditional keywords are `if`, `elif`, and `else`.

### 2. The if statement
```python
if condition:
    # executes when condition is True
    print("Condition is true")
```
A colon follows the condition; indentation defines the block.

### 3. if-else
Use `else` for the alternative branch when the `if` condition is false.

### 4. if-elif-else
Python evaluates conditions from top to bottom and executes the first matching branch. The `else` branch runs if none of the preceding conditions match.

### 5. Nested if
A nested `if` is inside another conditional block. It can model decisions involving multiple stages.

### 6. Truthy and falsy values
Common falsy values include `False`, `0`, `0.0`, `""`, `None`, and empty collections such as `[]` and `{}`. Most other values are truthy, including non-empty strings.

## Part 2 — Examples

### Example 1: if
```python
temperature = 35
if temperature > 30:
    print("It is hot today.")
```

### Example 2: Even or odd
```python
number = 7
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```
Output: `Odd number`.

### Example 3: Sales categories
```python
sales = 12000
if sales >= 20000:
    print("High sales")
elif sales >= 10000:
    print("Medium sales")
else:
    print("Low sales")
```
Output: `Medium sales`.

### Example 4: Simplified SOC alert classification
```python
failed_attempts = 8
if failed_attempts >= 10:
    print("High-priority review")
elif failed_attempts >= 5:
    print("Investigate login activity")
else:
    print("Below review threshold")
```
Output: `Investigate login activity`.

This is an illustrative training rule, not a production detection. Real analysis needs context such as the time window, account, source IP, and successful logins.

### Example 5: Combining conditions
```python
failed_attempts = 8
unusual_source = True

if failed_attempts >= 5 and unusual_source:
    print("Flag for investigation")
else:
    print("Condition not met")
```

## Part 3 — Practice exercises with answers

### Exercise 1: Positive, negative, or zero
```python
number = int(input("Enter an integer: "))

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")
```

### Exercise 2: Even or odd
```python
number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

### Exercise 3: Grade calculator
```python
marks = float(input("Enter marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Needs Improvement")
```

### Exercise 4: SOC alert classification
```python
failed_attempts = 12

if failed_attempts >= 10:
    print("High Priority")
elif failed_attempts >= 5:
    print("Investigate")
else:
    print("Low Priority")
```
Output for 12: `High Priority`.

### Exercise 5: Combined conditions
```python
failed_attempts = 7
unusual_source = True

if failed_attempts >= 5 and unusual_source:
    print("Flag for Investigation")
else:
    print("No Flag")
```

### Revision challenge
Given `failed_attempts = 4` and `unusual_source = True`, the following prints `Low Priority`, because neither conditional branch is satisfied:
```python
failed_attempts = 4
unusual_source = True

if failed_attempts >= 10:
    print("High Priority")
elif failed_attempts >= 5 and unusual_source:
    print("Investigate")
else:
    print("Low Priority")
```

## Quick quiz answers
1. `elif` checks another condition after the `if` branch fails.
2. For `x = 3`, `if x > 5: print("A") else: print("B")` prints `B`.
3. `else` executes when none of the preceding conditions is true.

## Key takeaways
- Use `if` for a condition, `elif` for additional alternatives, and `else` as a fallback.
- Use a colon and consistent indentation.
- Combine conditions with `and`, `or`, and `not`.
- A single threshold rule is not sufficient to conclude that an account is compromised.
