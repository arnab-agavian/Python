def list_comprehension_example(numbers):
    # numbers = [1, 2, 3, 4, 5]
    squared_numbers = [x**2 for x in numbers]
    print(f"Squared numbers: {squared_numbers}")

list_comprehension_example([1, 2, 3, 4, 5])

def set_comprehension_example(numbers):
    # numbers = [1, 2, 3, 4, 5, 2, 3]
    unique_numbers = {x for x in numbers}
    print(f"Unique numbers: {unique_numbers}")

set_comprehension_example([1, 2, 3, 4, 5, 2, 3])

def dict_comprehension_example(numbers):
    # numbers = [1, 2, 3, 4, 5]
    squared_dict = {x: x**2 for x in numbers if x % 2 == 0}
    print(f"Squared dictionary: {squared_dict}")

dict_comprehension_example([1, 2, 3, 4, 5])

def generator_expression_example(numbers):
    # numbers = [1, 2, 3, 4, 5]
    squared_gen = (x**2 for x in numbers)
    print(f"Squared generator: {list(squared_gen)}")

generator_expression_example([1, 2, 3, 4, 5])