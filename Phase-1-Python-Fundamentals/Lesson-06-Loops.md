# Lesson 6: Loops in Python

## Learning objectives
- Understand why loops are used.
- Use `for` and `while` loops.
- Use `range()`, `break`, and `continue`.
- Build counters and running totals.

## 1. Theory notes

A **loop** repeats a block of code. Loops are useful when processing many records, log events, failed login attempts, or sales values without writing the same code repeatedly.

### `for` loop
Use a `for` loop to iterate over a sequence, such as a list or a range of numbers.

```python
for item in sequence:
    # code to repeat
```

### `range()`
- `range(stop)`: starts at 0 and stops before `stop`.
- `range(start, stop)`: starts at `start` and stops before `stop`.
- `range(start, stop, step)`: moves by `step` each time.

Example: `range(1, 6)` produces 1, 2, 3, 4, 5. The stop value is excluded.

### `while` loop
A `while` loop repeats as long as its condition is `True`. Update the condition-related variable so the loop can eventually stop; otherwise, you may create an infinite loop.

### Loop controls
- `break`: immediately exits the loop.
- `continue`: skips the rest of the current iteration and moves to the next one.

### Counters and accumulators
- A **counter** tracks how many times something happens.
- An **accumulator** keeps a running total, often starting at 0.

## 2. Examples with explanations

### Example 1: Print numbers 1 to 5
```python
for number in range(1, 6):
    print(number)
```
Output:
```text
1
2
3
4
5
```
The stop value 6 is excluded.

### Example 2: Sum numbers from 1 to 100
```python
total = 0
for number in range(1, 101):
    total += number
print("Sum:", total)
```
Output: `Sum: 5050`

The accumulator `total` starts at 0 and adds each number.

### Example 3: A `while` countdown
```python
number = 5
while number >= 1:
    print(number)
    number -= 1
```
Output: 5, 4, 3, 2, 1 (each on a new line). Decreasing `number` eventually makes the condition false.

### Example 4: Skip an item with `continue`
```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```
Output: 1, 2, 4, 5. The iteration for 3 is skipped.

### Example 5: Count and total sales
```python
sales = [200, 450, 150, 300, 500]
total = 0
count = 0

for sale in sales:
    total += sale
    if sale >= 300:
        count += 1

print("Total sales:", total)
print("Sales of at least 300:", count)
```
Output:
```text
Total sales: 1600
Sales of at least 300: 3
```
The accumulator adds every sale; the counter increases only for sales of at least 300.

## 3. SOC example: Count failed logins
This is a small **simulated** example, not a live log collector.

```python
events = ["failed", "success", "failed", "failed"]
failed_count = 0

for event in events:
    if event == "failed":
        failed_count += 1

print("Failed login events:", failed_count)
```
Output: `Failed login events: 3`

A real investigation would also examine timestamps, accounts, source IPs, logon types, and what happened after a successful login. A count alone does not prove compromise.

## 4. Practice exercises

1. Use a `for` loop to print numbers from 1 to 10.
2. Calculate the sum of numbers from 1 to 100.
3. Print the even numbers from 2 to 20.
4. Use a `while` loop to print 5, 4, 3, 2, 1.
5. Given `events = ["success", "failed", "failed", "success", "failed"]`, count failed events.
6. Given `sales = [200, 450, 150, 300, 500]`, calculate the total and count how many sales are at least 300.

## 5. Selected exercise solutions

### Exercise 2
```python
total = 0
for number in range(1, 101):
    total += number
print("Sum:", total)
```
Output: `Sum: 5050`

### Exercise 4
```python
number = 5
while number >= 1:
    print(number)
    number -= 1
```

### Exercise 6
```python
sales = [200, 450, 150, 300, 500]
total = 0
count = 0

for sale in sales:
    total += sale
    if sale >= 300:
        count += 1

print("Total sales:", total)
print("Sales of at least 300:", count)
```
Output: total is 1600; 3 sales are at least 300.

## 6. Key points to remember
- Use `for` to iterate over sequences and `while` when repetition depends on a condition.
- `range()` excludes its stop value.
- Update variables in a `while` loop to avoid an infinite loop.
- `break` exits; `continue` skips the current iteration.
- Counters count events; accumulators calculate totals.
