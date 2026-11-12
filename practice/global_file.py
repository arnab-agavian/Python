# num = len(input("Enter a string: "))
# print(num + num)

global_int = 0
names = ["Alice", "Bob", "Charlie"]

def mainFunc():
    global names
    first_name = list(filter(lambda name: name.find("A") != -1, names))
    print(f"Names starting with A: {first_name}")
    globa = 0
    print(f"This is the main function - {globa}")
    def inner():
        nonlocal globa
        globa += 1
        print(f"This is the inner function - {globa}")

    inner()
    print(f"This is the main function after inner call - {globa}")

def globalFunc():
    def inner():    
        global global_int
        global_int += 1
        print(f"This is the global function - {global_int}")
    inner()
def multiple_returns():
    def inner():
        return 1, 2, 3
    a, b, c = inner()
    print(f"Multiple returns: {a}, {b}, {c}")

def pure_function(x, y):
    return x + y
def impure_function(x):
    global global_int
    global_int += x
    return global_int

def recursive_function(n):
    if n <= 0:
        return 1
    else:
        return n * recursive_function(n - 1)