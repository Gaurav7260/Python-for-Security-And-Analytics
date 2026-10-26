# Python Phase 1 — Lesson 5: Conditional Statements (Exercises and Review)

**Environment:** Google Colab  
**Format:** Theory notes → Examples → Practice

## Exercise solutions

### 1. Positive, negative, or zero
```python
number = int(input("Enter an integer: "))

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")
```

### 2. Even or odd
```python
number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

### 3. Grade calculator
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

### 4. SOC alert classification
```python
failed_attempts = 12

if failed_attempts >= 10:
    print("High Priority")
elif failed_attempts >= 5:
    print("Investigate")
else:
    print("Low Priority")
```

### 5. Combined conditions
```python
failed_attempts = 7
unusual_source = True

if failed_attempts >= 5 and unusual_source:
    print("Flag for Investigation")
else:
    print("No Flag")
```

### Revision challenge answer
With `failed_attempts = 4` and `unusual_source = True`, the output is `Low Priority`. The first condition fails, and the second fails because the login count is under five.

## Quick quiz answers
1. `elif`.
2. `B`.
3. `else` executes when no previous condition is true.

## Reminder
This is a simplified training rule, not a real-world compromise verdict. A SOC analyst uses additional evidence and context.
