"""
The rectangle class which has height & width
"""


class Rectangle:
    """
    Represents a rectangle
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        Return the area
        """
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter
        """
        return 2 * (self.width + self.height)

    def __repr__(self):
        return f"[width': {self.width} 'height': {self.height}]"

    class NestedClass:
        """
        Example Nested Class
        """

        def __init__(self, data):
            self.data = data

        def process_data(self):
            """
            A toy function
            """

            return len(self.data)

        def process_data_v2(self):
            """
            A toy function
            """

            return len(self.data) + 1

        def __repr__(self):
            return f"[data': {self.data}]"
