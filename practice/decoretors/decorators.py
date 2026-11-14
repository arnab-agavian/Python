"""
Examples of decorators and decorators that accept configuration.

A decorator takes a function and returns a replacement function (a wrapper).
The @decorator syntax applies the decorator when the function is defined:

    @decorator
    def greet(name):
        ...

is equivalent to:

    greet = decorator(greet)

The first decorator below prints before and after calling the original
function. Its wrapper uses *args and **kwargs to accept and forward any
positional and keyword arguments. It returns the original function's result.

@wraps(func) copies the original function's metadata to its wrapper, so
introspection such as greet.__name__ still reports "greet". It does not change
how the function executes. If the wrapped function raises an exception, the
first decorator will not reach its "After" print or return statement.

decorator_with_args is a decorator factory: it first accepts configuration
values, then returns a decorator, which receives the function. The wrapper
remembers the configuration values in a closure and prints them before calling
the original function.

The example functions print messages but do not explicitly return values, so
their return value is None. The main guard runs main() only when this file is
executed directly, not when it is imported.
"""

from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper


def decorator_with_args(arg1, arg2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Decorator arguments: {arg1}, {arg2}")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} completed")
        return result
    return wrapper


def main():
    print(decorator.__name__)  # Output: decorator

    # This is equivalent to: say_hello = decorator(say_hello)
    @decorator
    def say_hello(name):
        print(f"Hello, {name}!")

    print(say_hello.__name__)  # Output: say_hello

    # The factory receives its options, then returns the decorator.
    @decorator_with_args("arg1_value", "arg2_value")
    def say_goodbye(name):
        print(f"Goodbye, {name}!")

    @log_activity
    def print_todo(todo_list, prefix="Todo:"):
        for item in todo_list:
            print(f"{prefix} {item}")

    say_hello("Alice")
    say_goodbye("Bob")
    print_todo(["Buy milk", "Walk the dog"])

if __name__ == "__main__":
    main()