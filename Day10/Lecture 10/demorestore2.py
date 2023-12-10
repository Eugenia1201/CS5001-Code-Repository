"""Try persistence with JSON."""

import jsonpickle
import uuid


class Dog:
    """A dog."""

    dogs = dict()

    def __init__(self, name):
        """Initialize the dog."""
        self.name = name
        self.id = uuid.uuid4()
        Dog.dogs[self.id] = self


if __name__ == "__main__":
    with open("persist2.json", "r", newline="") as in_file:
        s1 = in_file.read()
        dict1 = jsonpickle.decode(s1)

        s2 = jsonpickle.encode(dict1, indent=2)
        print(s2)

        Dog.dogs = dict1
        s3 = jsonpickle.encode(Dog.dogs, indent=2)
        print(s3)
