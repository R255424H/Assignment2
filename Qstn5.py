# Import required modules
from abc import ABC, abstractmethod

# Step 1: Define the Abstract Base Class
class FileHandler(ABC):
    @abstractmethod
    def read(self, filepath):
        """Read data from a file."""
        pass

    @abstractmethod
    def write(self, filepath, data):
        """Write data to a file."""
        pass


# Step 2: Create a concrete class for handling text files
class TextFileHandler(FileHandler):
    def read(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()

    def write(self, filepath, data):
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(data)


# Step 3: Create a concrete class for handling binary files
class BinaryFileHandler(FileHandler):
    def read(self, filepath):
        with open(filepath, 'rb') as file:
            return file.read()

    def write(self, filepath, data):
        with open(filepath, 'wb') as file:
            file.write(data)


# Step 4: Example usage
if __name__ == "__main__":
    # Using TextFileHandler
    text_handler = TextFileHandler()
    text_handler.write("example.txt", "Hello, this is a text file!")
    print("Text File Content:", text_handler.read("example.txt"))

    # Using BinaryFileHandler
    binary_handler = BinaryFileHandler()
    binary_handler.write("example.bin", b'\xDE\xAD\xBE\xEF')
    print("Binary File Content:", binary_handler.read("example.bin"))
