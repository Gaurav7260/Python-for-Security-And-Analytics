# Python Phase 1 — Lesson 1: Introduction to Python and print()

**Environment:** Google Colab  
**Format:** Theory notes → Examples → Practice

## Part 1 — Theory notes

### What is Python?
Python is a high-level, general-purpose programming language used for automation, cybersecurity, data analytics, AI, and web development.

### What is a Python interpreter?
The Python interpreter runs Python code. Google Colab provides a hosted Python runtime, so you can write and execute code in notebook cells without setting up Python locally.

### The print() function
The built-in `print()` function displays information in the output.

```python
print("Hello, World!")
```

### Strings
A string (`str`) represents text. Text is usually enclosed in matching single or double quotation marks.

```python
"Hello"
'Hello'
```

### Comments
A comment begins with `#`. Python ignores it during normal execution.

```python
# This is a comment
print("Hello")
```

### Python is case-sensitive
`print()` is correct; `Print()` is not the same function name.

## Part 2 — Examples

### Example 1: Display a message
```python
print("Hello, World!")
```

Output:
```text
Hello, World!
```

### Example 2: Display multiple lines
```python
print("My name is Gourav.")
print("I am a B.Tech CSE student.")
print("I am learning Python.")
```

### Example 3: Print numbers and calculations
```python
print(25)
print(10 + 20)
print(100 - 35)
```

Output:
```text
25
30
65
```

### Example 4: Use comments
```python
# Cybersecurity example
print("Analyzing security logs")

# Analytics example
print("Analyzing sales data")
```

## Part 3 — Practice exercises

1. Print your name, degree, and graduation batch.
2. Print the results of `45 + 55`, `100 - 28`, and `12 * 8`.
3. Print three lines describing what a SOC Analyst does, including at least one comment.
4. Fix the errors:
   ```python
   Print("Learning Python")
   print("My first program)
   ```

## Key takeaways
- `print()` displays output.
- Strings represent text and need matching quotation marks.
- Comments start with `#`.
- Python is case-sensitive.
- In Google Colab, use separate code cells to run examples and exercises.
