"""Demo of jsonpickle."""

import jsonpickle


class Dog:
    """A canine animal."""

    def __init__(self, name, food):
        """Initialize the Dog."""
        self.name = name
        self.food = food


if __name__ == "__main__":
    d = Dog("Fido", "dog food")
    json_1 = jsonpickle.encode(d)
    print(json_1)

    e = jsonpickle.decode(json_1)
    print(e)
    print(e.__dict__)
