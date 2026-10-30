# Lesson 9: Tuples, Sets, and Dictionaries

## Learning objectives
- Understand tuples, sets, and dictionaries.
- Know when to use each data structure.
- Access and update dictionary values.
- Perform basic set operations.
- Apply these structures to SOC and analytics examples.

## 1. Theory notes

### Tuples
A **tuple** stores multiple values, like a list, but is **immutable**: its elements cannot be changed after creation.

```python
tools = ("Splunk", "Wazuh", "Sentinel")
print(tools[0])
print(tools[-1])
print(len(tools))
```
Output:
```text
Splunk
Sentinel
3
```

Tuple characteristics:
- Ordered and indexed.
- Allows duplicate values.
- Supports indexing and slicing.
- Immutable.
- Can contain different data types.

Use tuples for collections that should remain fixed, such as coordinates or fixed configuration values.

### Sets
A **set** stores unique values.

```python
tools = {"Splunk", "Wazuh", "Splunk", "Sentinel"}
print(tools)
```
Only one copy of each value remains. Display order may vary.

Set characteristics:
- Does not allow duplicate values.
- Unordered; do not rely on positions.
- Mutable.
- Does not support indexing.
- Useful for deduplication and mathematical set operations.

An empty set is created with `set()`. Empty `{}` creates a dictionary.

Important set methods:

| Method | Purpose |
|---|---|
| `add()` | Adds one element |
| `update()` | Adds multiple elements |
| `remove()` | Removes an element; raises an error if missing |
| `discard()` | Removes an element; does not error if missing |
| `union()` | Combines sets |
| `intersection()` | Finds common elements |
| `difference()` | Finds elements in the first set but not the second |

### Dictionaries
A **dictionary** stores data as key-value pairs.

```python
student = {
    "name": "Rahul",
    "age": 21,
    "course": "B.Tech"
}
```

Dictionary characteristics:
- Stores key-value pairs.
- Mutable.
- Keys must be unique; values may repeat.
- Values can have different data types.
- Access values using keys.
- Preserves insertion order in modern Python.

## 2. Examples with explanations

### Example 1: Access dictionary values
```python
student = {"name": "Rahul", "age": 21, "course": "B.Tech"}
print(student["name"])
print(student["age"])
```
Output:
```text
Rahul
21
```
Dictionaries use keys for lookup rather than list-style numeric indexes.

### Example 2: Add and update values
```python
student = {"name": "Rahul", "age": 21}
student["course"] = "Computer Science"
student["age"] = 22
print(student)
```
A new key adds an entry; assigning to an existing key updates its value.

### Example 3: Dictionary methods
```python
student = {"name": "Rahul", "age": 21, "course": "B.Tech"}
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
```

| Method | Purpose |
|---|---|
| `keys()` | Returns dictionary keys |
| `values()` | Returns dictionary values |
| `items()` | Returns key-value pairs |
| `get()` | Retrieves a value safely |
| `update()` | Updates dictionary entries |
| `pop()` | Removes a key and returns its value |

`get()` returns `None` by default when a key is missing, instead of raising a `KeyError`. You can supply a default:
```python
print(student.get("email", "Not available"))
```

### Example 4: Loop through a dictionary
```python
student = {"name": "Rahul", "age": 21, "course": "B.Tech"}
for key, value in student.items():
    print(key, ":", value)
```

### Example 5: Set operations
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
```
- Union contains all unique elements from both sets.
- Intersection contains elements common to both.
- Difference `A - B` contains elements in A but not B.

## 3. Real-world applications

### SOC example 1: Remove duplicate IP addresses
```python
ip_addresses = [
    "192.168.1.10",
    "10.0.0.5",
    "192.168.1.10",
    "172.16.0.2",
    "10.0.0.5"
]

unique_ips = set(ip_addresses)
print(unique_ips)
print("Unique IP count:", len(unique_ips))
```
This produces three unique IP addresses. A unique IP is not automatically malicious; it still needs investigation and context.

### SOC example 2: Represent a security event
```python
event = {
    "username": "admin",
    "source_ip": "192.168.1.20",
    "event_type": "failed_login",
    "severity": "high",
    "timestamp": "2026-10-30 10:00:00"
}

print("Username:", event["username"])
print("Source IP:", event["source_ip"])
print("Event:", event["event_type"])
print("Severity:", event["severity"])
```
This is a simplified representation of a structured security event.

### Data analytics example: Product revenue
```python
product = {
    "product_name": "Laptop",
    "price": 55000,
    "quantity_sold": 10,
    "category": "Electronics"
}

revenue = product["price"] * product["quantity_sold"]
print("Product:", product["product_name"])
print("Revenue:", revenue)
```
Output: revenue is 550000.

## 4. Comparison: list, tuple, set, dictionary

| Feature | List | Tuple | Set | Dictionary |
|---|---|---|---|---|
| Syntax | `[]` | `()` | `{}` | `{key: value}` |
| Ordered | Yes | Yes | No | Yes |
| Mutable | Yes | No | Yes | Yes |
| Duplicates | Yes | Yes | No | Keys must be unique |
| Access | Index | Index | No indexing | Key |

Memory aid:
- List: collection you may change.
- Tuple: collection you want to keep fixed.
- Set: unique values.
- Dictionary: key-value information.

## 5. Practice exercises

1. Create a tuple containing five SIEM tools. Print the first and last elements.
2. Create a set from `[10, 20, 10, 30, 20, 40]`. Print the unique elements and their count.
3. Create a set of three programming languages. Add Python to it.
4. Create a dictionary for a student with name, age, and course. Print each value.
5. Add an email key to your student dictionary and update the age.
6. Given `event = {"username": "admin", "ip": "192.168.1.10", "status": "failed"}`, print the IP using `get()`.
7. Given `ips = ["10.0.0.1", "10.0.0.2", "10.0.0.1", "10.0.0.3"]`, create a set of unique IPs.
8. Create `A = {1, 2, 3, 4}` and `B = {3, 4, 5, 6}`. Find their union, intersection, and difference `A - B`.

## 6. Quick quiz

1. Which data structure does not allow duplicate elements? **Set.**
2. Can you modify a tuple after creating it? **No.**
3. What is the difference between `remove()` and `discard()` in sets? **Both remove an element; `remove()` raises an error if it is missing, while `discard()` does not.**
4. What does `dictionary.get("name")` do? **Retrieves the value for the key "name", or returns None if it is absent and no default is supplied.**
5. Which data structure stores key-value pairs? **Dictionary.**

## 7. Key points to remember
- Tuples are immutable.
- Sets store unique elements.
- Dictionaries store key-value pairs.
- `get()` is useful for safe dictionary lookups.
- `union()`, `intersection()`, and `difference()` are important set operations.
- SOC event records and analytics records can be represented using dictionaries.
