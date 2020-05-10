# GettingStartedWithPython
Exercises from "Python Jumpstart" and "Write Pythonic Code Like a Seasoned Developer " course - https://training.talkpython.fm/courses/


## Truthiness

```shell script
False  # false is false
[]     # empty list / arrays are false
{}     # empty dictionaries are false
""     # empty strings are false
0      # zero ints are false
0.0    # zero floats are false
None   # None / null / nil pointers are false
Custom # Custom __bool__ / __nonzero__ are false
```

Everything else in True

\__bool\__ gives us the chance of set the truethiness of a class, example
```python
class AClass:
    def __init__(self):
        self.data = []

    def __bool__(self):
        return True if self.data else False
```

## Testing for None

```python
def find_accounts(search_text):
    # perf search
    if not db_is_available:
        return None

accounts = find_accounts('Python')
if accounts is None: #Checks for null pointer!!!
    print("Error: DB not available.")
else:
    print("Accounts found: Would list them here?")
```

## Multiple Test Against a Single Variable

```python
# Regular way
if m == Moves.North or m == Moves.South or m == Moves.West or m == Moves.East:
  print("Blah...")

# Pythonic way

if m in { Moves.North, Moves.South, Moves.West, Moves.East }: 
    print("Blah...")
```

## Chose a Random Item
```python
letters = {"asdfghjklzxcvbnmqwertyuiop1234567890"}
item = random.choice(letters)
```

## String Formatting

```python
# Old format
print("Hi I'm %s and I'm %d years old." % (name, age))

# Better approach
print("Hi I'm {} and I'm {} years old.".format(name, age))

# with dictionary
data = {'data': "Saturday", 'office':'Home Office', 'other':'UNUSED'}
print("On {day} I was working in my office {office}!".format(**data))

# Python 3.6 or above
print(f"On {day} I was working in my {office}!") # those are variables in the scope
```

# Send an Exit Code
If it is called from other consumer scripts, the exit numbers are recommended.

```python
import sys
... # Code

    print("Format Cancelled!")
    sys.exit(1)
... # Code
    print("Completed Successfully!")
    sys.exit(0) 
```
**Always use 0 for success**
