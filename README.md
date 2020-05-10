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

## Dictionaries

They are used several places, such as
 
 * Backing Store for types, classes, and objects
 * Isomorphic with JSON
 * Keyword arguments in methods
 * Add significant performance to random access
 * Can add switch like functionality to Python
 * Database records
 
 
### Performance
Dictionaries have better performance over List when search is used using on single field, such as Id if it is used as key 

Syntax to create a dictionary from class list

```python
data_list = []
data_dict = { d.id : d for d in data_list }
```

### Merging dictionaries
 
 ```python
route = {'id': 271, 'title': 'Fast apps'}
query = {'id': 1, 'render_fast': True}
post = {'email': 'email@domain.com', 'name':'Jeff'}

# Classic Pythonic Way
m2 = query.copy()
m2.update(post)
m2.update(route)

# Via dictionary comprehensions
m3 = {k: v for d in [query, post, route] for k, v in d.items()}

# Python 3.5+ pythonic way
m4 = { **query, **post, **route}

```

### Hacking Python's memory with \__slots\__

It has a better performance than classes, mainly over memory. But only to be used when you really need it.

```python
class ImmutableThing:
    __slots__ = ['a','b','c','d']
    
    def __init__ (self, a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
 
```
### Safer dictionary item access

Avoid crashes when accessing a dictionary using invalid keys

```python
data = dict()
if 'key' in data:
    print(data['key'])
# or
print(data.get('key'))

# or
print(data.get('key','default_value'))

#or
import collections
data = defaultdict(lambda: "MISSING", data) #When missing key, it returns "MISSING"
```

### Dictionary as switch statements
Pretty simple the use of keys to simulate switch statement
also it can execute functions

```python
from enum import Enum


def main():
    d_text = input("Which direction [n,s,w,e,nw,ne,sw,se]? ")
    m = Moves.parse(d_text)

    print("You chose: {}".format(m))

    squirrel = Character("Chippy")
    squirrel.move(m)


class Moves(Enum):
    West = 1
    North = 2
    East = 3
    South = 4
    NorthEast = 5
    SouthEast = 6
    NorthWest = 7
    SouthWest = 8

    @staticmethod
    def parse(text: str):
        if not text:
            return None

        text = text.strip().lower()
        parse_dict = {
            'w': Moves.West, 's': Moves.South, 'e': Moves.East, 'n': Moves.North,
            'nw': Moves.NorthWest, 'ne': Moves.NorthEast, 'sw': Moves.SouthWest, 'se': Moves.SouthEast
        }
        return parse_dict.get(text)


class Character:
    def __init__(self, name):
        self.name = name

    def move(self, direction: Moves):
        action_dict = {
            Moves.North: lambda: print("{} moves north with a special hesitation!".format(self.name)),
            Moves.South: lambda: print("{} is going south for winter!".format(self.name))
        }

        action = action_dict.get(
            direction,
            lambda: print("{} moves quickly to {}".format(self.name, direction)))
        action()


if __name__ == '__main__':
    main()
```
### JSON -> dict -> JSON

```python
import json

movie_json = """
{
"Title":"Johnny 5",
"Year":"2001",
"Runtime":"119 min",
"Country":"USA"
}
"""

movie_data = json.loads(movie_json)
print(type(movie_data), movie_data)

print("The title is {}".format(movie_data.get('Title')))

movie_json_text_2 = json.dumps(movie_data)
print(type(movie_json_text_2), movie_json_text_2)

# print(type(movie_json), movie_json)
# md = {
#     "Title":"Johnny 5",
#     "Year":"2001",
#     "Runtime":"119 min",
#     "Country":"USA"
#     }
# print(type(md), md)
```
