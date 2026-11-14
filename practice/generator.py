"""
A generator produces values one at a time instead of returning them all at once.

Generator function                    Regular function
Calling it returns a generator object Calling it runs the function and returns its result
Uses yield to produce each value      Uses return to produce its result
Pauses at each yield and resumes      Stops when it reaches return

`yield` sends a value to the caller, pauses the function, and remembers its
local state. The next `next()` call (or loop iteration) resumes execution
after that `yield`. Unlike `return`, it does not finish the function.

This is useful when values can be produced as needed: it avoids building a
complete list in memory and can represent an unbounded sequence, such as the
infinite generator below. Consume a generator with `next()` or a `for` loop.
"""


def generator_function():
    yield "Hello"
    yield "World"


def normal_function():
    return "Hello World"


value1 = generator_function()
value2 = normal_function()

# Each next() call resumes the generator until it reaches the next yield.
print(next(value1))  # Output: Hello
print(next(value1))  # Output: World
print(value2)  # Output: Hello World

# infinite generator

def infinite_generator():
    num = 0
    while True:
        yield f"Current: {num}"
        num += 1

values = infinite_generator()

for _ in range(5):
    print(next(values))  # Output: Current: 0, Current: 1, Current: 2, Current: 3, Current: 4


def generator_send_value():
    def generator():
        while True:
            value = yield
            print(f"Received: {value}")

    gen = generator()
    next(gen)  # Start the generator

    gen.send("Hello")  # Output: Received: Hello
    gen.send("World")  # Output: Received: World

    def order_chai():
        order = yield
        while True:
            print(f"Order received: {order}")
            order = yield
    order_gen = order_chai()
    next(order_gen)  # Start the generator
    order_gen.send("Chai")  # Output: Order received: Chai
    order_gen.send("Coffee")  # Output: Order received: Coffee
    order_gen.send("Capatino")  # Output: Order received: Capatino

def generator_with_return():
    def generator():
        yield "Start"
        return "Finished"

    gen = generator()
    print(next(gen))  # Output: Start
    try:
        print(next(gen))  # This will raise StopIteration
    except StopIteration as e:
        print(f"Generator returned: {e.value}")  # Output: Generator returned: Finished

# yield from and close the generator

def generator_with_yield_from():
    def generator1():
        yield "Generator 1 - Start"
        yield from generator2()
        yield "Generator 1 - Middle"
        yield "Generator 1 - End"

    def generator2():
        yield "Generator 2 - Start"
        yield "Generator 2 - Middle"
        yield "Generator 2 - End"

    gen = generator1()
    for value in gen:
        print(value)

def generator_with_close():
    def generator():
        try:
            while True:
                value = yield
                print(f"Received: {value}")
        except GeneratorExit:
            print("Generator closed")

    gen = generator()
    next(gen)  # Start the generator
    gen.send("Hello")  # Output: Received: Hello
    gen.send("World")  # Output: Received: World
    gen.close()  # Output: Generator closed

def generator_with_throw():
    def generator():
        try:
            while True:
                value = yield
                print(f"Received: {value}")
        except ValueError as e:
            print(f"Generator caught an exception: {e}")

    gen = generator()
    next(gen)  # Start the generator
    gen.send("Hello")  # Output: Received: Hello
    gen.throw(ValueError, "An error occurred")  # Output: Generator caught an exception: An error occurred

def main():
    print("Generator function example:")
    generator_function()
    print("\nNormal function example:")
    normal_function()
    print("\nInfinite generator example:")
    infinite_generator()
    print("\nGenerator send value example:")
    generator_send_value()
    print("\nGenerator with return example:")
    generator_with_return()
    print("\nGenerator with yield from example:")
    generator_with_yield_from()
    print("\nGenerator with close example:")
    generator_with_close()
    # print("\nGenerator with throw example:")
    # generator_with_throw()

if __name__ == "__main__":
    main()