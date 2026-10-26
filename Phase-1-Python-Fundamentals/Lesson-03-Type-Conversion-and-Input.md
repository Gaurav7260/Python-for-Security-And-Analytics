# Python Phase 1 — Lesson 3: Type Conversion and User Input

**Environment:** Google Colab  
**Format:** Theory notes → Examples → Practice

## Part 1 — Theory notes

### 1. Type conversion
Type conversion changes a value from one data type to another.

- Implicit conversion: Python converts types automatically in some operations, such as `5 + 2.0` producing `7.0`.
- Explicit conversion: you deliberately convert a value using functions such as `int()`, `float()`, `str()`, and `bool()`.

### 2. Useful conversion functions

```python
int("21")       # 21
float("99.50")  # 99.5
str(95)         # "95"
bool(0)         # False
bool("False")   # True, because the string is non-empty
```

Note: `int("21.5")` raises a `ValueError`. If appropriate, convert the string to `float` first.

### 3. The input() function
`input()` prompts the user to enter data and returns the entered value as a string.

```python
name = input("Enter your name: ")
print(name)
print(type(name))
```

### 4. Why conversion matters
If `input()` reads `10` and `20`, the values are strings. Adding them with `+` concatenates them into `"1020"`. Convert them to integers to perform arithmetic.

### 5. Invalid conversions
Converting an unsuitable value, such as `int("hello")`, raises a `ValueError`. Later we'll learn how `try` and `except` can handle such errors.

## Part 2 — Examples

### Example 1: String to integer
```python
number = "100"
print(type(number))

converted_number = int(number)
print(converted_number)
print(type(converted_number))
```

### Example 2: Shopping bill
```python
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity
print("Total bill:", total)
```

### Example 3: Average marks
```python
mark1 = float(input("Enter first mark: "))
mark2 = float(input("Enter second mark: "))
mark3 = float(input("Enter third mark: "))

average = (mark1 + mark2 + mark3) / 3
print("Average marks:", average)
```

### Example 4: Security log entry entered manually
```python
username = input("Enter username: ")
failed_attempts = int(input("Enter failed login count: "))

print("Username:", username)
print("Failed attempts:", failed_attempts)
print("Data type:", type(failed_attempts))
```

This illustrates manual input; it does not collect live security telemetry.

## Part 3 — Practice exercises

1. Ask the user for their name and age. Convert age to an integer and print both values with their types.
2. Ask the user for two integers. Print their sum, difference, product, and division result. Assume the second number is not zero.
3. Ask for a product price and quantity. Convert price to float and quantity to int, then calculate total cost.
4. Ask for a username and failed-login count. Print both in a message.
5. Predict then run the code:
   ```python
   a = "10"
   b = "5"

   print(a + b)
   print(int(a) + int(b))
   print(float(a) / int(b))
   ```

Expected output for exercise 5:
```text
105
15
2.0
```

## Quick quiz answers
1. `input()` returns a string by default.
2. `int("25")` returns integer `25`.
3. String concatenation of `"10"` and `"5"` produces `"105"`.

## Key takeaways
- `input()` returns strings.
- Use `int()` and `float()` before numeric calculations.
- `+` concatenates strings and adds numeric values.
- Invalid conversions can raise `ValueError`.
