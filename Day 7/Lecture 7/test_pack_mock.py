""" Testing Pack and Dog Using Mock
"""

import unittest
import unittest.mock
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

    @unittest.mock.patch.object(pack.Pack, "share_food")
    def test_eat_share(self, mock_share_food):
        self.pack = pack.Pack(pack.Dog)
        self.assertFalse(self.pack.fed)

        this_dog = self.pack.members[0]
        this_dog.eat("dog food", True)
        mock_share_food.assert_called_with("dog food")


if __name__ == "__main__":
    unittest.main()
