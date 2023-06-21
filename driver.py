"""
The driver code for IO capture
"""

import io_capture

modules = io_capture.decorate_directory_modules("example_projects")
example = modules["example"]


def perform_calls():
    """
    Perform IO-capturing calls
    """

    example.sum_v3({1: "one", 2: "two", 3: "three"})
    example.sum_v4({1, 2, 3, 4, 5, 6.6, -7.7})

    example.sum_v2([1.2, 2, 3.4, 5.5, 3, -1.1])
    example.sum_v2({1.2, 2, 3.4, 5.5, 3, -1.1})

    example.add(2, 5)
    example.add(2, 3)
    example.multiply(4, 5)

    person1 = example.Person("Alice", 25)
    person2 = example.Person("Bob", 30)
    person1.introduce()
    person2.introduce()

    rectangle1 = example.Rectangle(4, 5)
    rectangle2 = example.Rectangle(3, 6)
    rectangle1.area()
    rectangle2.perimeter()

    # # Function calls with functions as parameters
    example.apply_operation(example.add, 200, 300)
    example.apply_operation(example.multiply, 4000, 5000)

    # # Function calls with dictionaries
    dictionary = {"name": "Alice", "age": 25}
    example.apply_operation(
        lambda x, y: example.Person(**x).introduce(), dictionary, None
    )

    example.foo_baz(5)

    obj = example.MyClass()
    obj.my_method(5)


# capture IO from the calls
perform_calls()

# Print the recorded calls
for i, call in enumerate(io_capture.calls):
    print(f"Call {i+1}:")
    print("Function:", call["function"])
    print("Inputs:", call["inputs"])
    print("Output:", call["output"])
    print()
