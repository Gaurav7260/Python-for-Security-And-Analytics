# Lesson 7: Strings and String Methods

## Learning objectives
- Understand strings and indexing.
- Extract portions of a string using slicing.
- Clean and search text with common string methods.
- Apply case-insensitive matching to simple log messages.

## 1. Theory notes

A **string** (`str`) is text surrounded by quotes, for example `"hello"` or `'hello'`.

### Indexing
Python uses zero-based indexing:
- First character: index 0
- Second character: index 1
- Last character: index -1

Example: `word = "PYTHON"`; `word[0]` is `"P"`, and `word[-1]` is `"N"`.

### Slicing
Use `string[start:stop]` to extract a portion. The start index is included and the stop index is excluded.

Example: `"PYTHON"[1:4]` gives `"YTH"`.

### Common string methods
- `.lower()`: converts letters to lowercase.
- `.upper()`: converts letters to uppercase.
- `.strip()`: removes whitespace from the beginning and end.
- `.replace(old, new)`: replaces matching text.
- `.split()`: splits text into a list; by default, it splits on whitespace.
- `.find(substring)`: returns the first matching index, or -1 if not found.
- `.count(substring)`: counts non-overlapping occurrences.
- `.startswith(prefix)` / `.endswith(suffix)`: test the beginning or ending.
- `in`: checks whether a substring exists.

### Strings are immutable
String methods return a new string; they do not change the original string in place. Store the result if you want to keep the cleaned version.

## 2. Examples with explanations

### Example 1: Indexing and slicing
```python
word = "PYTHON"
print(word[0])
print(word[-1])
print(word[0:3])
```
Output:
```text
P
N
PYT
```

### Example 2: Clean and normalize text
```python
message = "  HELLO WORLD  "
clean_message = message.strip().lower()
print(clean_message)
```
Output: `hello world`

`strip()` removes surrounding whitespace, and `lower()` normalizes the case.

### Example 3: Count a phrase
```python
message = "failed login from admin, failed login from guest"
print(message.count("failed login"))
```
Output: `2`

### Example 4: Split a simple log-like line
```python
log = "admin 192.168.1.20 failed"
parts = log.split()
print(parts)
print("Username:", parts[0])
print("IP:", parts[1])
print("Status:", parts[2])
```
Output:
```text
['admin', '192.168.1.20', 'failed']
Username: admin
IP: 192.168.1.20
Status: failed
```
This assumes the line has exactly these three whitespace-separated fields. Real logs often have structured fields, quoted text, or different formats.

### Example 5: Case-insensitive keyword search
```python
message = "ERROR: connection failed"

if "error" in message.lower():
    print("Error found")
else:
    print("Error not found")
```
Output: `Error found`

Converting a copy to lowercase makes the keyword check case-insensitive. In production log analysis, preserve the original event and normalize a separate value for matching.

### Example 6: Replace a URL prefix
```python
url = "http://example.com"
secure_url = url.replace("http://", "https://")
print(secure_url)
```
Output: `https://example.com`

Note: this is a string replacement demonstration, not a guarantee that the website supports HTTPS.

## 3. Practice exercises

1. Given `word = "PYTHON"`, print the first character, last character, and first three characters.
2. Convert `"  HELLO WORLD  "` to `"hello world"`.
3. Given `message = "failed login from admin, failed login from guest"`, count occurrences of `"failed login"`.
4. Given `log = "admin 192.168.1.20 failed"`, split it and print the username, IP, and status.
5. Check whether `"error"` occurs in `"ERROR: connection failed"`, ignoring case.
6. Replace `"http://"` with `"https://"` in `"http://example.com"`.

## 4. Quick quiz and answers
- What does `"PYTHON"[1:4]` return? **`"YTH"`**
- What does `.strip()` remove? **Whitespace from the beginning and end.**
- Are strings mutable? **No. String methods return new strings rather than modifying the original string in place.**

## 5. Key points to remember
- Indexing starts at 0; negative indexing counts backward from the end.
- In slicing, the start is included and the stop is excluded.
- Use `.strip()` to clean surrounding whitespace and `.lower()` / `.upper()` to normalize case.
- `.split()` is useful for simple whitespace-separated text.
- Use `in` or `.count()` to search for text.
- For security analysis, avoid treating a keyword match as proof of an incident; review context and related events.
