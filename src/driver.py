"""
The driver code for IO capture
"""

import sys
from os.path import abspath, dirname
from example_project import example, person, rectangle
import io_capture

# Adjust the path to include the sibling directory
sibling_dir = abspath(dirname(dirname(__file__)))
sys.path.append(sibling_dir)


# decorating all the modules
for key, value in io_capture.decorate_directory_modules("example_project").items():
    globals()[key] = value


def perform_calls():
    """
    Perform IO-capturing calls
    """
    # pylint: disable=E0602
    # The line above is for dynamic var generation err handling (research code only!)

    example.sum_v3({1: "one", 2: "two", 3: "three"})
    example.sum_v4({1, 2, 3, 4, 5, 6.6, -7.7})

    example.sum_v2([1.2, 2, 3.4, 5.5, 3, -1.1])
    example.sum_v2({1.2, 2, 3.4, 5.5, 3, -1.1})

    example.add(2, 5)
    example.add(2, 3)
    example.multiply(4, 5)

    person1 = person.Person("Alice", 25)
    person2 = person.Person("Bob", 30)
    student1 = person.Student("Tom", 23)
    person1.introduce()
    person2.introduce()
    student1.introduce()

    person_list = [person1, person2, student1]

    for p in person_list:
        p.introduce()

    rectangle1 = rectangle.Rectangle(4, 5)
    rectangle2 = rectangle.Rectangle(3, 6)
    rectangle1.area()
    rectangle2.perimeter()

    # # Function calls with functions as parameters
    example.apply_operation(example.add, 200, 300)
    example.apply_operation(example.multiply, 4000, 5000)

    # # Function calls with dictionaries
    dictionary = {"name": "Alice", "age": 25}
    example.apply_operation(
        lambda x, y: person.Person(**x).introduce(), dictionary, None
    )

    example.foo_baz(2)

    obj = example.MyClass()
    obj.my_method(5)

    example.sum_v5(1, 2, 3, 4, 5, 6, key=100, keykey=200, keykeykey=300)
    example.do_nothing_v1()
    example.do_something_v1()
    example.do_something_v2(1)
    example.do_something_v2(1, -1)

    example.apply_operation(example.add, 200, 300)

    rectangle1 = rectangle.Rectangle(100, 1000)
    nested_class1 = rectangle1.NestedClass([1, 2, 3])
    nested_class2 = rectangle2.NestedClass([4, 5, 6])
    nested_class1.process_data()
    nested_class2.process_data()


# capture IO from the calls
perform_calls()


# Print the recorded calls
for i, call in enumerate(io_capture.calls):
    print(f"Call {i+1}:")
    print("Function:", call["function"])
    print("Inputs:", call["inputs"])
    print("Output:", call["output"])
    print()
