""" Testing Pack and Dog
"""

import unittest
import pack


class Test_Pack(unittest.TestCase):

    def setUp(self):
        self.pack = pack.Pack(pack.Dog)

    def test_init(self):
        self.assertFalse(self.pack.fed)
        for member in self.pack.members:
            self.assertFalse(member.fed)

    def test_share_food(self):
        self.pack.share_food("dog food")
        self.assertTrue(self.pack.fed)
        for member in self.pack.members:
            self.assertTrue(member.fed)


class Test_Dog(unittest.TestCase):

    def test_eat(self):
        self.dog = pack.Dog(None)
        self.assertFalse(self.dog.fed, "Dog started with fed True")

        self.dog.eat("dog food", False)
        self.assertTrue(self.dog.fed, "After eat, Dog fed is False")

    def test_eat_share(self):
        self.pack = pack.Pack(pack.Dog)
        self.assertFalse(self.pack.fed)

        this_dog = self.pack.members[0]
        this_dog.eat("dog food", True)
        self.assertTrue(self.pack.fed)
        for dog in self.pack.members:
            self.assertTrue(dog.fed)


if __name__ == "__main__":
    unittest.main()
