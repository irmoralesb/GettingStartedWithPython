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