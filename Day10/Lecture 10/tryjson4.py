"""Try JSON serializer."""

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


class DogList:
    """A list of dogs."""

    def __init__(self, dog1, dog2):
        """Initialize the list of dogs."""
        self.dog_list = [dog1.id, dog2.id]


if __name__ == "__main__":

    # make two dog lists
    fido = Dog("Fido")
    bingo = Dog("Bingo")
    dog_list1 = DogList(fido, bingo)
    dog_list2 = DogList(bingo, fido)

    # see if the object identities match
    print(dog_list1.dog_list[0] == dog_list2.dog_list[1])
    print(dog_list1.dog_list[1] == dog_list2.dog_list[0])

    # Encode the lists
    s1 = jsonpickle.encode(dog_list1)
    s2 = jsonpickle.encode(dog_list2)

    # Decode the lists back into Dog_Lists
    new_dog_list1 = jsonpickle.decode(s1)
    new_dog_list2 = jsonpickle.decode(s2)

    # see if the deseriallized object identities were preserved
    print()
    print(new_dog_list1.dog_list[0] == new_dog_list2.dog_list[1])
    print(new_dog_list1.dog_list[1] == new_dog_list2.dog_list[0])
    print(Dog.dogs[new_dog_list1.dog_list[0]] is
          Dog.dogs[new_dog_list2.dog_list[1]])
    print(Dog.dogs[new_dog_list1.dog_list[1]] is
          Dog.dogs[new_dog_list2.dog_list[0]])

    # print some stuff
    print(s1)
    print(new_dog_list1.dog_list[0])
    print(new_dog_list1.dog_list[1])
    print(Dog.dogs[new_dog_list1.dog_list[0]].name)
    print(Dog.dogs[new_dog_list1.dog_list[1]].name)
