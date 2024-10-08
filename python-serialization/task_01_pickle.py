#!/usr/bin/python3
import pickle
""""""


class CustomObject():
    """"""
    name = ""
    age = 0
    is_student = False

    def __init__(self, name, age, is_student) -> None:
        self.name = name
        self.age = age
        self.is_student = is_student
        pass

    def display(self):
        """"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))
        
    def serialize(self, filename):
        """"""
        if not filename:
            print("Invalid filename")

        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """"""
        if not filename:
            print("Invalid filename")
            return None
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            print("File not found")
            return None

# Create an instance of CustomObject
obj = CustomObject(name="John", age=25, is_student=True)
print("Original Object:")
obj.display()

# Serialize the object
obj.serialize("object.pkl")

# Deserialize the object into a new instance
new_obj = CustomObject.deserialize("object.pkl")
print("\nDeserialized Object:")
new_obj.display()