# Python Phase 1 — Lesson 4: Operators

**Environment:** Google Colab  
**Format:** Theory notes → Examples → Practice

## Part 1 — Theory notes

Operators are symbols or keywords that perform operations on values and variables.

### 1. Arithmetic operators

| Operator | Meaning | Example | Result |
|---|---|---|---:|
| `+` | Addition | `10 + 5` | 15 |
| `-` | Subtraction | `10 - 5` | 5 |
| `*` | Multiplication | `10 * 5` | 50 |
| `/` | Division | `10 / 5` | 2.0 |
| `//` | Floor division | `11 // 2` | 5 |
| `%` | Remainder (modulus) | `11 % 2` | 1 |
| `**` | Exponentiation | `2 ** 3` | 8 |

Floor division rounds down toward negative infinity; ordinary division `/` returns a float in Python 3.

### 2. Comparison operators
These return `True` or `False`.

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal | `5 == 5` → `True` |
| `!=` | Not equal | `5 != 3` → `True` |
| `>` | Greater than | `8 > 5` → `True` |
| `<` | Less than | `3 < 5` → `True` |
| `>=` | Greater than or equal | `5 >= 5` → `True` |
| `<=` | Less than or equal | `3 <= 5` → `True` |

Remember: `=` assigns a value; `==` compares values.

### 3. Logical operators
- `and`: both conditions must be true.
- `or`: at least one condition must be true.
- `not`: reverses a truth value.

### 4. Assignment operators
- `x = 10`: assign 10.
- `x += 2`: same as `x = x + 2`.
- `x -= 2`: same as `x = x - 2`.
- `x *= 2`: same as `x = x * 2`.
- `x /= 2`: same as `x = x / 2`.

### 5. Membership operators
`in` checks whether a value exists in a collection; `not in` checks whether it does not.

### 6. Identity operators
`is` and `is not` check object identity, not value equality. Use `==` for most value comparisons and `is None` to test for `None`.

## Part 2 — Examples

### Example 1: Arithmetic
```python
a = 11
b = 2

print(a + b)   # 13
print(a - b)   # 9
print(a * b)   # 22
print(a / b)   # 5.5
print(a // b)  # 5
print(a % b)   # 1
print(a ** b)  # 121
```

### Example 2: Comparisons
```python
failed_attempts = 8

print(failed_attempts > 5)  # True
print(failed_attempts == 8) # True
print(failed_attempts < 3)  # False
```

### Example 3: Logical SOC rule
```python
failed_attempts = 8
unusual_source = True

suspicious = failed_attempts >= 5 and unusual_source
print(suspicious)  # True
```

This is only a simplified illustrative rule, not a production detection.

### Example 4: Assignment operators
```python
count = 10
count += 5
print(count)  # 15

count -= 3
print(count)  # 12

count *= 2
print(count)  # 24
```

### Example 5: Membership
```python
roles = ["admin", "analyst", "guest"]

print("admin" in roles)     # True
print("hacker" in roles)    # False
print("guest" not in roles) # False
```

## Part 3 — Practice exercises

1. Set `a = 17` and `b = 4`. Print their sum, difference, product, division, floor division, and remainder.
2. Set `failed_attempts = 6`. Print whether the count is greater than 5, equal to 6, and less than 3.
3. Set `failed_attempts = 9` and `unusual_source = True`. Flag only when the count is at least 5 and the source is unusual.
4. A product costs ₹250 and a customer buys 4 units. Calculate the total and check whether it is greater than ₹900.
5. With `roles = ["admin", "analyst", "guest"]`, check whether `"analyst"` is present and whether `"manager"` is absent.

## Quick quiz answers
1. `17 % 4` is `1`.
2. `==` checks equality.
3. `True and False` evaluates to `False`.

## Key takeaways
- Arithmetic operators calculate; comparisons return Boolean results.
- `and`, `or`, and `not` combine or reverse conditions.
- `in` and `not in` test membership.
- Prefer `==` for value equality.
