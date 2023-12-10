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

    # make two dogs
    fido = Dog("Fido")
    bingo = Dog("Bingo")

    s1 = jsonpickle.encode(Dog.dogs, indent=2)

    with open("persist2.json", "w") as out_file:
        # print(s1, file=out_file)
        out_file.write(s1)
