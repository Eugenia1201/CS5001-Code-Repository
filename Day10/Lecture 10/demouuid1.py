"""Try UUIDs as object IDs."""

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

    # look at the dogs
    print(jsonpickle.encode(fido, indent=2))
    print(jsonpickle.encode(bingo, indent=2))

    # look at the dog dictionary
    print(jsonpickle.encode(Dog.dogs, indent=2))
