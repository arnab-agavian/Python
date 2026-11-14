# Python Notes for Beginners

These notes cover core Python concepts with short examples. Python uses
indentation (usually four spaces) to mark blocks of code.

## Index

- [1. Printing and comments](#1-printing-and-comments)
- [2. Variables and data types](#2-variables-and-data-types)
- [3. Strings](#3-strings)
- [4. Lists](#4-lists)
- [5. Tuples](#5-tuples)
- [6. Sets and dictionaries](#6-sets-and-dictionaries)
- [7. `if`, `elif`, and `else`](#7-if-elif-and-else)
- [8. Switch-style choices with `match` / `case`](#switch-case)
- [9. Loops](#9-loops)
- [10. Functions](#10-functions)
- [11. Object-oriented programming (OOP)](#11-object-oriented-programming-oop)
- [12. Handling errors](#12-handling-errors)
- [13. Comprehensions](#13-comprehensions)
- [14. Iterators and generators](#14-iterators-and-generators)
- [15. Modules, packages, and project structure](#15-modules-packages-and-project-structure)
- [16. Virtual environments and packages](#16-virtual-environments-and-packages)
- [17. Working with files and JSON](#17-working-with-files-and-json)
- [18. Type hints and dataclasses](#18-type-hints-and-dataclasses)
- [19. Decorators](#19-decorators)
- [20. Testing](#20-testing)
- [21. Logging](#21-logging)
- [22. Calling a web API](#22-calling-a-web-api)
- [23. Asynchronous programming](#23-asynchronous-programming)
- [24. Command-line arguments](#24-command-line-arguments)
- [25. Mutability and copying](#25-mutability-and-copying)
- [26. Scope and namespaces](#26-scope-and-namespaces)
- [27. Unpacking and useful built-ins](#27-unpacking-and-useful-built-ins)
- [28. Context managers](#28-context-managers)
- [29. Custom exceptions](#29-custom-exceptions)
- [30. Configuration and environment variables](#30-configuration-and-environment-variables)
- [31. Databases with SQLite](#31-databases-with-sqlite)
- [32. Debugging](#32-debugging)
- [33. Performance and concurrency](#33-performance-and-concurrency)
- [34. Documentation and application entry points](#34-documentation-and-application-entry-points)
- [35. Secure development checklist](#35-secure-development-checklist)
- [Quick reminders](#quick-reminders)

## 1. Printing and comments

`print()` writes readable output to the terminal. It can display several values,
separating them with spaces by default, and adds a newline at the end. Comments
begin with `#`; Python ignores them while running the program. Use comments to
explain a reason or a non-obvious decision, rather than restating what the code
already says.

```python
print("Hello, Python!")
print("Total:", 3 + 4)

# This is a one-line comment.
```

Triple-quoted strings are often used for multi-line docstrings, not as a special
multi-line comment syntax.

## 2. Variables and data types

A variable is a name that refers to a value. Python determines its type from
the value assigned to it.

Python is dynamically typed: a name can later be assigned a value of another
type. The value still has a type, and operations must be valid for that type.
For example, adding two numbers performs arithmetic, while adding two strings
joins their text. `None` represents an absent or not-yet-provided value; test
for it with `is None`.

```python
name = "Asha"          # str (text)
age = 20               # int (whole number)
height = 1.65          # float (decimal number)
is_learning = True     # bool (True or False)
nothing = None         # NoneType (no value)

print(name)
print(type(age))       # <class 'int'>
```

Variable names can contain letters, numbers, and underscores, but cannot start
with a number. Names are case-sensitive. Prefer descriptive `snake_case` names,
such as `total_price`.

Assignment (`=`) binds a name to a value; it does not mean "equals" as in
mathematics. Use `==` to compare values. Constants are usually written in
uppercase by convention (for example, `MAX_RETRIES = 3`), although Python does
not make them immutable.

### Converting between types

Conversion functions such as `int()`, `float()`, and `str()` create a
corresponding value when the input is valid. Invalid text such as
`int("hello")` raises `ValueError`, so validate or handle untrusted input.
Conversion is not always lossless: `int(3.9)` truncates the fractional part.

```python
age_text = "20"
age_number = int(age_text)
price = float("3.50")
message = str(age_number)

# input() always returns text; convert it before doing numeric calculations.
number = int(input("Enter a whole number: "))
print(number + 1)
```

Common operators:

The `/` operator always performs true division and returns a float. `//`
performs floor division, which rounds down (toward negative infinity); `%`
gives the associated remainder. `and`, `or`, and `not` are logical operators.
Use parentheses when they make a compound expression clearer.

```python
total = 8 + 3       # addition: 11
difference = 8 - 3  # subtraction: 5
product = 8 * 3     # multiplication: 24
quotient = 8 / 3    # division: 2.666...
whole = 8 // 3      # floor division: 2
remainder = 8 % 3   # remainder: 2
power = 2 ** 3      # exponent: 8
```

## 3. Strings

Strings are immutable sequences of text enclosed in single or double quotes.
Because they are immutable, methods such as `.upper()` return a new string
instead of changing the original. Indexing selects one character; slicing
selects a range, and the end index is excluded. An f-string evaluates
expressions inside `{}` and is a readable way to include values in text.

```python
first_name = "Asha"
greeting = f"Hello, {first_name}!"  # f-string
print(greeting)

print(first_name.upper())  # ASHA
print(len(first_name))     # 4
print(first_name[0])       # A (indexes start at 0)
```

Use `.strip()` to remove surrounding whitespace, `.lower()` for
case-insensitive comparisons, and `.split()` to divide text into parts. These
operations do not automatically validate text; check input according to the
rules of your application.

Five more useful string methods:

```python
sentence = "Python is fun"

print(sentence.replace("fun", "powerful"))  # replace matching text
print(sentence.find("is"))                  # index of "is", or -1 if absent
print(sentence.startswith("Python"))        # True
print(sentence.endswith("fun"))             # True
print(", ".join(["red", "green", "blue"]))  # join strings with a separator
```

`replace()` returns a new string and leaves the original unchanged.
`startswith()` and `endswith()` return Boolean values. `join()` is called on
the separator string and combines an iterable of strings.

## 4. Lists

A list is an ordered, changeable collection. It can contain values of different
types, though lists of one type are often easier to work with.

Lists preserve their item order and allow duplicates. Indexing reads or updates
one item, while slicing creates a new list containing a portion. `append()`
adds one item; `extend()` adds items from another iterable. `remove()` deletes
the first matching value and raises `ValueError` if it is absent; `pop()` takes
an item out and returns it. Check `len(items)` before indexing when the list
might be empty.

```python
fruits = ["apple", "banana", "orange"]
print(fruits[0])          # apple
print(fruits[-1])         # orange (last item)

fruits.append("grape")   # add to the end
fruits[1] = "pear"       # change an item
fruits.remove("orange")  # remove by value
last_fruit = fruits.pop()  # remove and return the last item

print(len(fruits))
print(fruits[0:2])       # slice: items at indexes 0 and 1
```

## 5. Tuples

A tuple is ordered like a list, but cannot be changed after it is created.
Use parentheses; a one-item tuple needs a trailing comma.

Tuple immutability makes tuples useful for fixed records, coordinates, and
values returned together from a function. A tuple can contain a mutable object
such as a list; the tuple's references cannot be reassigned, but that inner
list can still change. A tuple can be used as a dictionary key only when all
its contents are hashable.

```python
point = (4, 7)
print(point[0])  # 4

single_item = ("hello",)
```

Use a tuple for a fixed group of values. Use a list when you need to add,
remove, or update items.

## 6. Sets and dictionaries

A set stores unique hashable values and is useful for removing duplicates or
checking membership. Sets are unordered collections, so do not depend on their
display or iteration order. Set operations include union (`|`), intersection
(`&`), and difference (`-`).

```python
colors = {"red", "blue", "red"}
colors.add("green")
print(colors)  # contains red, blue, and green; each only once
```

A dictionary stores values under keys.

Dictionary keys must be hashable; strings and numbers are common choices.
Looking up a missing key with square brackets raises `KeyError`; `.get()` can
return a default instead. Dictionaries preserve insertion order in modern
Python, but choose keys for their meaning rather than relying on position.

```python
person = {
    "name": "Asha",
    "age": 20,
}

print(person["name"])
person["city"] = "Pune"       # add a key and value
person["age"] = 21            # update a value
print(person.get("country", "Not provided"))  # safe lookup with a default
```

## 7. `if`, `elif`, and `else`

Use conditionals to choose which code to run. Comparison operators include
`==`, `!=`, `<`, `>`, `<=`, and `>=`.

Python evaluates conditions as true or false. An `if` branch runs only when
its condition is true; `elif` checks another condition if earlier branches
were false; `else` handles the remaining case. Only the first matching branch
runs. Indentation defines the body of each branch.

```python
score = 82

if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
else:
    print("Keep practicing")
```

Combine conditions with `and`, `or`, and `not`:

`and` and `or` short-circuit: Python may skip evaluating the right-hand side
when the left-hand value already determines the result. Empty collections,
zero, and empty strings are false-like; non-empty values are generally
true-like. Prefer explicit comparisons when truthiness would be unclear.

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
```

<a id="switch-case"></a>

## 8. Switch-style choices with `match` / `case`

Python 3.10 and later provide `match` / `case` for matching a value against
several choices. It is similar to a switch statement in other languages. Python
`match` can also destructure structured values, so it is more general than
simple equality-based switch statements. Cases are tested from top to bottom;
put more specific patterns before broad patterns.

```python
day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print("It's the weekend")
    case "Monday":
        print("Start of the week")
    case _:
        print("A weekday")
```

The `_` case is the catch-all default and is conventionally placed last. A
matching case runs only its body; Python does not fall through to later cases.
For older Python versions, use `if` / `elif` or a dictionary lookup instead.

## 9. Loops

Loops repeat work. Choose `for` when iterating over items or a known sequence
of values, and `while` when repetition depends on a condition that changes
during the loop. Keep each loop's work focused and make sure a `while` loop
updates the state used by its condition.

### `for` loop

Use a `for` loop to go through items in a collection or a range of numbers.
The loop variable is assigned each item in turn. `range(stop)` starts at zero
and excludes `stop`; `range(start, stop, step)` lets you set the start and
increment. A `for` loop also works with strings, tuples, dictionaries, and
other iterables.

```python
for fruit in ["apple", "banana", "orange"]:
    print(fruit)

for number in range(1, 4):  # 1, 2, 3; the ending value is not included
    print(number)
```

### `while` loop

A `while` loop repeats as long as its condition is true. Make sure the
condition can eventually become false.

At the start of each iteration Python checks the condition. If it is false
initially, the body runs zero times. A counter or other state update inside
the loop commonly ensures it eventually stops. If a loop completes normally,
an optional `else` block can run; it is skipped if the loop exits with
`break`.

```python
count = 1
while count <= 3:
    print(count)
    count += 1
```

`break` exits a loop; `continue` skips to its next iteration.

```python
for number in range(5):
    if number == 2:
        continue
    if number == 4:
        break
    print(number)  # prints 0, 1, 3
```

## 10. Functions

Functions package reusable steps behind a name. Define one with `def`, then
call it by name. A function body does not run when the function is defined; it
runs when called. Functions make programs easier to reuse, test, and explain
when each one has a clear responsibility.

The names in the definition's parentheses are parameters; the values supplied
when calling it are arguments. `return` sends a result back to the caller and
ends that call. A function with no `return` statement returns `None`.

```python
def greet(name):
    """Return a greeting for the given name."""
    return f"Hello, {name}!"

message = greet("Asha")
print(message)
```

Parameters can have default values. A function can return a result with
`return`.

Arguments can be supplied positionally or by keyword, for example
`add_numbers(first=5, second=10)`. Defaults are used when an argument is
omitted. Avoid mutable default values such as `items=[]`; that same list would
be reused across calls. Use `None` as a default and create a fresh list inside
the function when needed.

```python
def add_numbers(first, second=0):
    return first + second

print(add_numbers(5, 10))  # 15
print(add_numbers(5))      # 5
```

`input()` returns a string, so convert user input before numeric operations:

```python
def add_user_numbers():
    first = float(input("Enter a number: "))
    second = float(input("Enter another number: "))
    return first + second

print(add_user_numbers())
```

## 11. Object-oriented programming (OOP)

OOP organizes code around **objects**. A **class** is a blueprint; an **object**
is an instance created from that blueprint. Objects can have data (attributes)
and behavior (methods). OOP is helpful when a program models entities that
combine state and operations. It is one design approach, not a requirement for
every Python program; modules and functions are often simpler for small tasks.

### Classes, objects, attributes, and methods

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"


my_dog = Dog("Milo", 3)
print(my_dog.name)   # attribute
print(my_dog.bark()) # method
```

`__init__` initializes an already-created object with its starting state; it
is commonly called the initializer. `self` refers to the particular instance
whose method is running, and Python passes it automatically when a method is
called through that instance. Instance attributes such as `self.name` belong
to each object; class attributes are shared through the class unless
overridden on an instance.

### The four common OOP concepts

1. **Encapsulation** — keep related data and methods together in a class.
   A leading underscore, as in `_balance`, signals that an attribute is
   intended for internal use; it does not make the attribute truly private.
2. **Inheritance** — create a class based on another class to reuse or extend
   its behavior.
3. **Polymorphism** — different classes can provide methods with the same name
   and respond in their own way.
4. **Abstraction** — expose the essential operations while hiding
   implementation details. Python's `abc` module can define abstract classes.

Use inheritance for a genuine "is-a" relationship. If one object merely uses
another object, composition ("has-a") is often easier to maintain. Encapsulation
is primarily a design convention in Python; a single leading underscore marks
an internal name, while a double leading underscore triggers name mangling
rather than strict privacy.

Inheritance example:

```python
class Animal:
    def speak(self):
        return "Some sound"


class Cat(Animal):
    def speak(self):
        return "Meow"


pet = Cat()
print(pet.speak())  # Meow
```

`Cat` inherits from `Animal` and overrides `speak()`. Calling `speak()` on
different animal objects can produce different results (polymorphism).

## 12. Handling errors

Use `try` / `except` to handle errors you expect, such as invalid number input.

An exception signals that an operation could not proceed normally. Put only
the statements that may raise the expected exception inside the `try` block,
and catch specific exception types so unrelated bugs are not hidden.
`else` can hold work that should run only when no exception occurred, and
`finally` can hold cleanup that must happen either way. Raise an exception
when a function cannot satisfy its contract instead of returning a misleading
success value.

```python
try:
    number = int(input("Enter a whole number: "))
    print(10 / number)
except ValueError:
    print("Please enter a valid whole number.")
except ZeroDivisionError:
    print("The number must not be zero.")
```

## 13. Comprehensions

Comprehensions build a collection from an iterable in a compact way. A list
comprehension has the general form
`[expression for item in iterable if condition]`; the filter is optional.
Dictionary and set comprehensions use `{}` with key/value or item expressions.
Comprehensions create a new collection and are best for straightforward
transformations and filters.

```python
squares = [number**2 for number in range(5)]
even_squares = [number**2 for number in range(10) if number % 2 == 0]
lengths = {word: len(word) for word in ["cat", "python"]}
```

Use a regular loop instead when the comprehension becomes difficult to read.

## 14. Iterators and generators

An iterator produces values one at a time. A generator function uses `yield`
to produce values lazily, which can save memory for large sequences.

An iterable is something you can loop over; calling `iter()` on it obtains an
iterator, and `next()` asks that iterator for its next value. When there are no
values left, iteration ends with `StopIteration` (normally handled by `for`).
A generator remembers where it paused at `yield` and continues from there when
asked for another item. Generators are consumed as they are iterated; create a
new generator if you need to repeat the traversal.

```python
def count_up_to(limit):
    number = 1
    while number <= limit:
        yield number
        number += 1


for value in count_up_to(3):
    print(value)
```

## 15. Modules, packages, and project structure

A module is a Python file that can be imported. A package is a directory that
groups related modules. Importing a module makes its names available through
that module's namespace; for example, `math.sqrt` makes clear where `sqrt`
comes from. Avoid naming your own files after standard-library modules (such
as `json.py`), since that can interfere with imports.

```python
# Import a standard-library module.
import math

print(math.sqrt(16))
```

Example project layout:

```text
my_project/
    pyproject.toml
    README.md
    src/
        my_project/
            __init__.py
            main.py
    tests/
        test_main.py
```

Keep related code in modules and import only what you need. Run a module from
the project directory with `python -m my_project.main` (depending on the
project's layout).

## 16. Virtual environments and packages

A virtual environment keeps a project's installed packages separate from
other Python projects. From the project directory, create and activate one:

The `.venv` folder contains an isolated interpreter environment and installed
libraries for this project. Activation adjusts the current terminal so
`python` and `pip` point to that environment; you can also invoke its
interpreter directly without activation. Recreate the environment when
switching Python versions or when it becomes inconsistent; do not normally
commit the `.venv` folder.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install requests
```

Use `python -m pip` so pip runs for the selected Python interpreter. Record
project dependencies in a project manifest such as `pyproject.toml`; avoid
installing project packages globally when working on separate projects.

Packages are reusable code published for installation. Review a package's
documentation and maintenance before adding it, and install only dependencies
the application needs. A project's manifest should describe its build system,
metadata, and dependencies in a reproducible way appropriate to its chosen
tools.

## 17. Working with files and JSON

Use `pathlib.Path` for paths and a `with` block to make sure files are closed.
Paths may be relative to the program's current working directory, which is not
always the directory containing the script. Use absolute paths or establish a
clear project-relative base path when file location matters. Specify an
encoding such as UTF-8 for text files to avoid relying on machine defaults.

```python
from pathlib import Path

file_path = Path("notes.txt")
file_path.write_text("Python is useful!\n", encoding="utf-8")
text = file_path.read_text(encoding="utf-8")
print(text)
```

The `json` module reads and writes JSON data.

JSON represents objects, arrays, strings, numbers, booleans, and `null`.
`json.dumps()` converts a compatible Python value to JSON text;
`json.loads()` parses JSON text into Python values. For files, use
`json.dump()` and `json.load()` with an open file. Parsing untrusted or invalid
JSON can raise `JSONDecodeError`; JSON also cannot directly represent every
Python object, such as a custom class instance.

```python
import json

settings = {"theme": "light", "font_size": 14}
json_text = json.dumps(settings, indent=2)
restored_settings = json.loads(json_text)
```

## 18. Type hints and dataclasses

Type hints document the kinds of values a function expects and returns. Python
does not enforce hints automatically at runtime, but editors and type checkers
can use them to find mistakes. Use annotations to make interfaces clearer,
especially for public functions and values with non-obvious shapes. A type
checker can report incompatible uses before the code runs, but it does not
replace input validation when data comes from a user, file, or network.

```python
def calculate_total(prices: list[float]) -> float:
    return sum(prices)
```

Use a dataclass for a class that mainly stores data:

`@dataclass` generates common methods such as an initializer and a readable
representation based on the declared fields. It is convenient for simple
records, but regular classes are a better fit when behavior or invariants are
more central. Use `field(default_factory=...)` for mutable per-instance
defaults rather than sharing a single mutable object.

```python
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float


item = Product("Notebook", 4.5)
print(item.name, item.price)
```

## 19. Decorators

A decorator wraps a function to add behavior without changing the function's
main body. Decorators are common in web frameworks and testing tools.

The `@announce` syntax is shorthand for replacing the decorated name with the
result of calling the decorator on the original function. A wrapper often
accepts `*args` and `**kwargs` so it can forward different calls. `wraps()`
preserves helpful metadata such as the original function's name and docstring.
Decorators execute when the function is defined, not each time the decorated
function is called; the wrapper executes on each call.

```python
from functools import wraps


def announce(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Starting")
        return function(*args, **kwargs)

    return wrapper


@announce
def greet(name):
    return f"Hello, {name}!"


print(greet("Asha"))
```

## 20. Testing

Tests check that code behaves as expected. The standard library includes
`unittest`; third-party tools such as `pytest` are also widely used.

Each test should focus on a behavior and compare an actual result to an
expected result. Tests can also check that invalid input raises the expected
exception. Small, independent tests are easier to diagnose than tests that
depend on ordering or external services. Mocking or fakes can isolate a unit
from slow or unreliable dependencies, but should not replace tests of the
real integration where practical.

```python
import unittest


def add(first, second):
    return first + second


class AddTests(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)


if __name__ == "__main__":
    unittest.main()
```

Save this example in a Python file and run it with `python filename.py`.
Write tests for normal cases, boundary cases, and expected errors.

Run tests regularly and whenever code changes. A test suite documents intended
behavior and makes refactoring safer; passing tests increase confidence but
cannot prove that every possible input is correct.

## 21. Logging

Use the `logging` module for diagnostic messages in applications. It provides
levels such as `DEBUG`, `INFO`, `WARNING`, and `ERROR`. `DEBUG` is detailed
diagnostic information, `INFO` records normal milestones, `WARNING` indicates
an unexpected condition that can be handled, and `ERROR` reports a failure.
Choose a level and message that help someone understand what happened.

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Application started")
logging.error("Something went wrong")
```

Avoid using `print()` as the only way to report problems in a larger
application.

Loggers can include timestamps, levels, and other metadata through
configuration. Avoid logging passwords, tokens, personal information, or
large amounts of unhelpful detail. In reusable libraries, prefer obtaining a
module logger with `logging.getLogger(__name__)` and let the application
configure the output.

## 22. Calling a web API

The third-party `requests` package can send HTTP requests. Install it in the
project's virtual environment with `python -m pip install requests`. An API
request typically uses an HTTP method (`GET` to read, `POST` to submit, and
others for updates or deletion), a URL, optional headers or parameters, and
possibly a body. The response includes a status code, headers, and often data.

```python
import requests

response = requests.get("https://api.example.com/items", timeout=10)
response.raise_for_status()  # raise an error for an unsuccessful HTTP status
items = response.json()
print(items)
```

Use a timeout, check the response status, and handle expected request or JSON
errors in real applications. Do not put passwords, API keys, or other secrets
directly in source code; load them from a secure configuration or environment.

Handle network failures and unsuccessful status codes explicitly; servers can
be unavailable, slow, or return unexpected data. Follow the service's
authentication, rate-limit, and data-format requirements. Use HTTPS for
services carrying credentials or sensitive data.

## 23. Asynchronous programming

`async` and `await` are useful for I/O-bound work, such as handling many
network requests. They do not automatically make CPU-heavy work faster.

Calling an `async def` function creates a coroutine; it does not run to
completion until awaited or scheduled on an event loop. `await` pauses the
current coroutine while an awaitable operation is pending, allowing other
coroutines to make progress. Use `asyncio.run()` once at a synchronous program
entry point to run a top-level coroutine. Do not call it inside an already
running event loop.

```python
import asyncio


async def main():
    print("Starting")
    await asyncio.sleep(1)  # yields control while waiting
    print("Finished")


asyncio.run(main())
```

Use an async-compatible library for network or database operations in an
async application; a regular blocking call can block the event loop.

Concurrency means multiple tasks make progress during overlapping periods;
parallelism means work executes at the same instant. Asyncio commonly
coordinates concurrent I/O on one thread. Use it when the workload and
libraries support it, not simply because it is a newer syntax.

## 24. Command-line arguments

Use `argparse` to build command-line tools that accept named options.

The parser reads arguments supplied after the script name, validates their
shape, converts declared types, and provides a generated help message.
Positional arguments are required in order by default; optional arguments
usually begin with `--`. Parsing returns a namespace whose attributes hold
the parsed values. Separating parsing from application logic makes command-line
programs easier to test.

```python
import argparse

parser = argparse.ArgumentParser(description="Greet someone")
parser.add_argument("name")
args = parser.parse_args()
print(f"Hello, {args.name}!")
```

Run the saved script with `python greet.py Asha`.

## 25. Mutability and copying

Lists and dictionaries are mutable: their contents can change. Integers,
strings, and tuples are examples of immutable values. Assignment binds another
name to the same object; it does not automatically copy that object. This is
why changing a shared mutable object through one name is visible through the
other.

```python
first = [1, 2]
second = first
second.append(3)
print(first)  # [1, 2, 3] -- both names refer to the same list
```

Copy a list when you need a separate outer list:

```python
original = [1, 2]
copied = original.copy()
copied.append(3)
print(original)  # [1, 2]
```

For nested collections, `.copy()` is shallow: nested objects are still shared.
Use `copy.deepcopy()` only when a fully independent nested copy is needed.
Copying has costs, and deep copies may not be appropriate for objects that
represent external resources or intentionally shared state. Choose the
smallest copying behavior that matches the intended ownership of the data.

## 26. Scope and namespaces

Names created inside a function are local to that function. Avoid changing
global variables from inside functions; passing values in and returning results
makes code easier to test.

A namespace is the mapping from names to objects. Function parameters and
local assignments normally create local names. A function can read a global
name, but assigning to that name inside the function makes it local unless
declared `global`. Nested functions can read names in enclosing functions;
`nonlocal` permits reassignment of an enclosing function's name.

```python
tax_rate = 0.1


def add_tax(price):
    return price * (1 + tax_rate)


print(add_tax(100))
```

Python looks up names using the LEGB order: Local, Enclosing, Global, Built-in.
Use `nonlocal` or `global` only when there is a clear reason to reassign a name
from an outer scope.

## 27. Unpacking and useful built-ins

Unpacking assigns items from an iterable to several names. `enumerate()` gives
an index and item; `zip()` pairs items from multiple iterables. Unpacking
requires the expected number of values unless a starred target collects the
remaining values. By default, `zip()` stops when the shortest input ends; use
`itertools.zip_longest()` if missing values should be filled instead.

```python
first, second = ("red", "blue")
name, *scores = ("Asha", 80, 95)

for index, fruit in enumerate(["apple", "pear"], start=1):
    print(index, fruit)

for name, score in zip(["Asha", "Ben"], [90, 85]):
    print(name, score)
```

Use `sorted()` to get a new sorted list, or `.sort()` to change a list in
place. The `key` argument customizes sorting and should produce comparable
values. Other useful built-ins include `any()` and `all()` for testing
conditions across iterables, and `sum()` and `min()` / `max()` for common
numeric or ordering tasks.

```python
names = ["Maya", "Al", "Christopher"]
by_length = sorted(names, key=len)
print(by_length)
```

## 28. Context managers

A context manager handles setup and cleanup around a block. The `with`
statement is commonly used for files, locks, and database connections.
Entering the block acquires or prepares a resource; leaving it triggers
cleanup even when an exception occurs. This makes resource handling more
reliable than manually remembering to close a file in every code path.

```python
from pathlib import Path

with Path("notes.txt").open(encoding="utf-8") as file:
    for line in file:
        print(line.rstrip())
```

When the block ends, the file is closed automatically, including if an error
occurs.

Many standard-library resources support `with`. Custom context managers can
be created with `__enter__` / `__exit__` methods or the `contextlib` module.
Use them when code owns a resource that must be released predictably.

## 29. Custom exceptions

Raise a specific exception when a function cannot complete its job. A custom
exception can make errors in an application easier to distinguish and handle.
Usually inherit from `Exception`, give the exception a meaningful name, and
include a message that helps callers decide what to do. Do not use exceptions
for ordinary control flow when a regular condition is clearer.

```python
class InsufficientFundsError(Exception):
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Not enough funds")
    return balance - amount
```

Catch exceptions where you can take a useful action. Avoid catching every
exception without re-raising or reporting it.

## 30. Configuration and environment variables

Keep environment-specific settings out of source code. The standard library's
`os.environ` reads environment variables; use a clear error if a required
setting is missing. Configuration separates values that change between
development, testing, and production (such as service URLs) from program
logic. Environment variables are strings, so parse and validate values such as
ports, feature flags, and timeouts before using them.

```python
import os

service_url = os.environ.get("SERVICE_URL", "http://localhost:8000")
api_key = os.environ.get("SERVICE_API_KEY")

if api_key is None:
    raise RuntimeError("Set the SERVICE_API_KEY environment variable")
```

Do not commit credentials or `.env` files containing secrets to version
control. For local development, use a properly ignored local configuration
file or your platform's secret-management tools.

Provide safe defaults only for non-sensitive settings where a default makes
sense. For required secrets or production settings, fail clearly instead of
silently using an insecure or incorrect value.

## 31. Databases with SQLite

SQLite is included with Python and is useful for small applications and local
data. Use placeholders for values in SQL queries; do not build queries by
concatenating user input. A database stores structured data in tables, and SQL
statements create tables, insert rows, update or delete records, and query
results. A connection manages access to the database; a cursor or connection
executes statements and returns rows.

```python
from contextlib import closing
import sqlite3

with closing(sqlite3.connect("app.db")) as connection, connection:
    connection.execute(
        "CREATE TABLE IF NOT EXISTS tasks (name TEXT, done INTEGER)"
    )
    connection.execute(
        "INSERT INTO tasks (name, done) VALUES (?, ?)",
        ("Learn Python", 0),
    )
    rows = connection.execute(
        "SELECT name, done FROM tasks WHERE done = ?", (0,)
    ).fetchall()
    print(rows)
```

The connection context commits a successful transaction or rolls it back if an
error occurs; `closing()` closes the connection afterward.

For larger applications, learn database migrations, transactions, and the
appropriate database library for your chosen database server.

A transaction groups changes so they can be committed together or rolled back
if something fails. SQL placeholders protect values from being interpreted as
SQL syntax; table or column names generally cannot be passed as ordinary
placeholders. Keep database work inside a well-defined layer and close
connections when finished.

## 32. Debugging

Read the complete traceback: the last lines usually show the exception type
and the code location where it occurred. Add a breakpoint to inspect values
while a program runs. Debugging is the process of turning a reported problem
into a reproducible case, observing the program's state, finding the cause,
and then verifying the correction with a test or repeatable check.

```python
def calculate_average(values):
    breakpoint()  # inspect values here in an interactive debugger
    return sum(values) / len(values)
```

Run the program normally; at the debugger prompt, commands such as `n` (next),
`s` (step into), `p values` (print a value), and `c` (continue) are useful.
Most IDEs also provide graphical breakpoints and variable inspection.

Start with the exact error message, input, and code path. Inspect values near
the failure rather than changing unrelated code. Remove temporary breakpoints
before committing or sharing code.

## 33. Performance and concurrency

First make code correct and measure it before optimizing. The `timeit` module
can compare small pieces of code; profilers help locate slow parts of a
program. Avoid guessing where a performance problem is. Consider algorithmic
complexity and data size as well as the speed of individual lines; a more
efficient algorithm often matters more than a small syntax-level change.

Choose a concurrency approach based on the work:

- **Asyncio** is useful for many I/O waits when libraries support async.
- **Threading** can help overlap I/O tasks that use blocking libraries.
- **Multiprocessing** can run CPU-heavy work across processes, with extra
  memory and communication costs.

Concurrency adds complexity. Start with straightforward sequential code and
introduce it when a measured requirement calls for it.

Use `timeit` for small isolated operations and a profiler for a representative
whole program. Measure realistic inputs, repeat measurements, and check that
an optimization preserves correctness. Concurrent programs also need careful
handling of shared state, cancellation, failures, and cleanup.

## 34. Documentation and application entry points

Use docstrings to explain a function's purpose, important arguments, and
return value. Add a main guard so a module can be imported without immediately
running its command-line behavior. A docstring is a string placed first in a
module, class, or function body and is available through documentation tools
and `help()`. Explain behavior and constraints that are not obvious from the
signature.

```python
def main():
    """Run the application."""
    print("Application started")


if __name__ == "__main__":
    main()
```

Follow a consistent style such as PEP 8, write a useful `README.md`, and keep
setup and run instructions up to date.

The main guard distinguishes direct execution from importing: when run as a
script, `__name__` is `"__main__"`; when imported, it is the module's name.
This keeps reusable definitions available to tests and other modules without
starting the application as a side effect.

## 35. Secure development checklist

Security is part of normal development: protect data, restrict access, and
handle untrusted input at system boundaries. These practices lower risk but do
not replace a security review appropriate to the application and its threat
model.

- Validate external input and handle errors explicitly.
- Use parameterized database queries.
- Keep secrets out of source code and version control.
- Set timeouts on network requests and verify responses.
- Use maintained dependencies and update them regularly.
- Give files, accounts, and services only the permissions they need.

Also avoid exposing internal error details to users, keep dependencies
up-to-date, and review what data is logged or sent to external services.

## Quick reminders

- Python is case-sensitive: `name` and `Name` are different variables.
- Indent blocks consistently, usually with four spaces.
- List indexes start at `0`; negative indexes count from the end.
- Use `=` to assign a value and `==` to compare values.
- Use `match` / `case` only with Python 3.10 or later.
- Prefer small functions, clear names, tests, and version control as a project grows.