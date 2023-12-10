"""Try JSON serializer."""

import jsonpickle


class Dog:
    """A dog."""

    def __init__(self, name):
        """Initialize the dog."""
        self.name = name


class DogList:
    """A list of dogs."""

    def __init__(self, dog1, dog2):
        """Initialize the list of dogs."""
        self.dog_list = [dog1, dog2]


if __name__ == "__main__":

    # make two dog lists
    fido = Dog("Fido")
    bingo = Dog("Bingo")
    dog_list1 = DogList(fido, bingo)
    dog_list2 = DogList(bingo, fido)

    # see if the object identities match
    print(dog_list1.dog_list[0] is dog_list2.dog_list[1])
    print(dog_list1.dog_list[1] is dog_list2.dog_list[0])

    # Encode the lists
    s1 = jsonpickle.encode(dog_list1)
    s2 = jsonpickle.encode(dog_list2)

    # Decode the lists back into Dog_Lists
    new_dog_list1 = jsonpickle.decode(s1)
    new_dog_list2 = jsonpickle.decode(s2)

    # see if the deseriallized object identities were preserved
    print(new_dog_list1.dog_list[0] is new_dog_list2.dog_list[1])
    print(new_dog_list1.dog_list[1] is new_dog_list2.dog_list[0])
