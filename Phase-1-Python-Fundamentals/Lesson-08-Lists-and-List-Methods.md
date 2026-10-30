# Lesson 8: Lists and List Methods

## Learning objectives
- Understand Python lists and their characteristics.
- Access, slice, and modify list elements.
- Use common list methods.
- Apply lists to simple SOC and data analytics examples.

## 1. Theory notes

### What is a list?
A **list** is a Python data structure that stores multiple values in a single variable.

```python
fruits = ["apple", "banana", "mango"]
print(fruits)
```

List characteristics:
- Ordered: items maintain their position.
- Mutable: items can be changed.
- Indexed: items can be accessed by position.
- Allows duplicate values.
- Can contain different data types.

Example:
```python
data = ["admin", 25, 192.168, True]
print(data)
```

### Accessing list elements
Python uses zero-based indexing.

```python
tools = ["Splunk", "Wazuh", "Sentinel", "QRadar"]

print(tools[0])   # First element
print(tools[1])   # Second element
print(tools[-1])  # Last element
```
Output:
```text
Splunk
Wazuh
QRadar
```

### List slicing
Use `list_name[start:stop]` to extract a portion. The start is included and the stop is excluded.

```python
tools = ["Splunk", "Wazuh", "Sentinel", "QRadar"]
print(tools[0:2])
print(tools[1:3])
```
Output:
```text
['Splunk', 'Wazuh']
['Wazuh', 'Sentinel']
```

### Modifying list elements
Lists are mutable, so an element can be reassigned.

```python
tools = ["Splunk", "Wazuh", "Sentinel"]
tools[1] = "Microsoft Sentinel"
print(tools)
```

### Important list methods and functions

| Method / function | Purpose |
|---|---|
| `append(item)` | Adds one item at the end |
| `insert(index, item)` | Adds an item at a specific position |
| `extend(iterable)` | Adds multiple items from an iterable |
| `remove(value)` | Removes the first matching value |
| `pop(index)` | Removes and returns an item; defaults to the last |
| `sort()` | Sorts the list in place |
| `reverse()` | Reverses the list in place |
| `count(value)` | Counts occurrences |
| `index(value)` | Finds the first matching index |
| `clear()` | Removes all items |
| `len(list)` | Returns the number of items |

## 2. Examples with explanations

### Example 1: append()
```python
tools = ["Splunk", "Wazuh"]
tools.append("Sentinel")
print(tools)
```
Output: `['Splunk', 'Wazuh', 'Sentinel']`

`append()` adds one element at the end.

### Example 2: insert()
```python
tools = ["Splunk", "Wazuh"]
tools.insert(1, "Sentinel")
print(tools)
```
Output: `['Splunk', 'Sentinel', 'Wazuh']`

`insert(1, ...)` adds the element at index 1.

### Example 3: extend()
```python
tools = ["Splunk", "Wazuh"]
tools.extend(["Sentinel", "QRadar"])
print(tools)
```
Output: `['Splunk', 'Wazuh', 'Sentinel', 'QRadar']`

`extend()` adds multiple elements from another iterable.

### Example 4: remove()
```python
tools = ["Splunk", "Wazuh", "Sentinel"]
tools.remove("Wazuh")
print(tools)
```
Output: `['Splunk', 'Sentinel']`

`remove()` deletes the first matching value. It raises `ValueError` if the value does not exist.

### Example 5: pop()
```python
tools = ["Splunk", "Wazuh", "Sentinel"]
removed_tool = tools.pop(1)

print("Removed:", removed_tool)
print("Remaining:", tools)
```
Output:
```text
Removed: Wazuh
Remaining: ['Splunk', 'Sentinel']
```
`pop()` removes an item and returns it. Without an index, it removes the last item.

### Example 6: sort()
```python
numbers = [50, 10, 40, 20, 30]
numbers.sort()
print(numbers)
```
Output: `[10, 20, 30, 40, 50]`

For descending order:
```python
numbers.sort(reverse=True)
print(numbers)
```
Output: `[50, 40, 30, 20, 10]`

### Example 7: count() and index()
```python
events = ["failed", "success", "failed", "failed"]
print(events.count("failed"))
print(events.index("success"))
```
Output:
```text
3
1
```
- `count()` tells how often a value appears.
- `index()` returns the position of its first occurrence.

## 3. Real-world applications

### SOC example: Count authentication events
This is a small simulated example, not a live log collector.

```python
events = ["failed", "success", "failed", "failed"]

failed_count = events.count("failed")
success_count = events.count("success")

print("Failed logins:", failed_count)
print("Successful logins:", success_count)
```
Output:
```text
Failed logins: 3
Successful logins: 1
```

A real investigation should also examine timestamps, accounts, source IPs, logon types, and activity after successful logins. Counts alone do not prove compromise.

### Data analytics example: Sales analysis
```python
sales = [200, 450, 150, 300, 500]

print("Total records:", len(sales))
print("Highest sale:", max(sales))
print("Lowest sale:", min(sales))
print("Total sales:", sum(sales))
```
Output:
```text
Total records: 5
Highest sale: 500
Lowest sale: 150
Total sales: 1600
```

- `len()` counts records.
- `max()` finds the highest value.
- `min()` finds the lowest value.
- `sum()` calculates the total.

## 4. Practice exercises

1. Create a list containing five programming languages and print the complete list.
2. Given `tools = ["Splunk", "Wazuh", "Sentinel", "QRadar"]`, print the first and last elements.
3. Given `numbers = [10, 20, 30, 40, 50]`, print only `[20, 30, 40]`.
4. Add `"Microsoft Defender"` to the end of `tools = ["Splunk", "Wazuh"]`.
5. Insert 100 at index 1 in `numbers = [10, 20, 30]`.
6. Remove `"failed"` from `events = ["success", "failed", "failed", "success"]`.
7. Count how many times `"failed"` appears in `events = ["failed", "success", "failed", "failed"]`.
8. Given `sales = [200, 450, 150, 300, 500]`, calculate the total, maximum, and minimum.

## 5. Quick quiz
1. What is the index of the first element in a list? **0.**
2. Which method adds an element to the end of a list? **append().**
3. What is the difference between `append()` and `extend()`? **append adds one item; extend adds items from an iterable.**
4. Does `pop()` return the removed element? **Yes.**
5. Are Python lists mutable? **Yes.**

## 6. Key points to remember
- Lists store multiple values in one variable.
- Indexing starts at zero.
- Slicing extracts a portion of a list.
- Lists are mutable.
- `append()` adds one item; `extend()` adds multiple items.
- `remove()` removes by value; `pop()` removes by index (or the last item by default).
- `count()` and `index()` are useful for searching and analyzing data.
