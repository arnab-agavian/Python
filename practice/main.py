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