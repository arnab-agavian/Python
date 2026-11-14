import global_file
import comprihensions.comprihensions as cmp
# from global_file import global_int, names

global_file.mainFunc()
global_file.globalFunc()
global_file.multiple_returns()
print(f"Pure function result: {global_file.pure_function(5, 3)}")
print(f"Impure function result: {global_file.impure_function(2)}")
print(f"Recursive function result: {global_file.recursive_function(5)}")
cmp.list_comprehension_example([1, 2, 3, 4, 5])
cmp.set_comprehension_example([1, 2, 3, 4, 5, 2, 3])
cmp.dict_comprehension_example([1, 2, 3, 4, 5])
cmp.generator_expression_example([1, 2, 3, 4, 5])

touple_example = (1, 2, 3, 4, 5)
def tuple_unpacking():
    a, b, c, d, e = touple_example
    print(f"Tuple unpacking: {a}, {b}, {c}, {d}, {e}")
def list_unpacking():
    a, b, *rest = [1, 2, 3, 4, 5]
    print(f"List unpacking: {a}, {b}, {rest}")
def dict_unpacking():
    my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
    name, age, city = my_dict.values()
    print(f"Dict unpacking: {name}, {age}, {city}")
def set_unpacking():
    my_set = {1, 2, 3, 4, 5}
    a, b, *rest = my_set
    print(f"Set unpacking: {a}, {b}, {rest}")
def unpacking_examples():
    tuple_unpacking()
    list_unpacking()
    dict_unpacking()
    set_unpacking()


tuple_function = lambda x, y: x + y
def lambda_example():
    result = tuple_function(5, 10)
    print(f"Lambda example: {result}")
unpacking_examples()
lambda_example()