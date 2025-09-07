#Scenario: You have a function process_sound(sound_object) that expects an object with a
#make_sound() method. You have two classes, Dog and Cat, both of which implement the
#make_sound() method, but in different ways.

#Provide example code demonstrating how the process_sound() function can work with
#both Dog and Cat objects without needing to know their specific types.

# Define the process_sound function
def process_sound(sound_object):
    # Calls the make_sound() method, without knowing the type
    sound = sound_object.make_sound()
    print(f"The sound is: {sound}")

# Define the Dog class
class Dog:
    def make_sound(self):
        return "Woof!"

# Define the Cat class
class Cat:
    def make_sound(self):
        return "Meow!"

# Create instances
dog = Dog()
cat = Cat()

# Use the process_sound function with both
process_sound(dog)  # Output: The sound is: Woof!
process_sound(cat)  # Output: The sound is: Meow!
