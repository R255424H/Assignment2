#Scenario: You have a base class Shape with a method calculate_area(). You then create a
#derived class Rectangle that inherits from Shape. The Rectangle class needs to implement
#its own calculate_area() method, but you also want to utilize some initialization logic from
#the Shape class&#39;s constructor.
#Demonstrate how to use the super() function within the Rectangle class&#39;s
#calculate_area() method (even if the shape class area method does nothing) to call the
#Shape class&#39;s constructor (__init__).

class Shape:
    def __init__(self):
        print("Shape initialized.")

    def calculate_area(self):
        # Placeholder method
        print("Calculating area in Shape (base class).")
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        # Normally, we'd call super().__init__() here, but for the demo, we skip it here.
        super().__init__()
        self.width = width
        self.height = height

    def calculate_area(self):
        # Call the Shape's constructor from here using super()
        super().__init__()  # This is unusual, but allowed
        print("Calculating area in Rectangle.")
        return self.width * self.height


# Example usage:
rect = Rectangle(5, 10)
area = rect.calculate_area()
print("Area:", area)