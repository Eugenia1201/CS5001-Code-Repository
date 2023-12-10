""" Testing Dog
"""

import unittest
import dog


class Test_Dog(unittest.TestCase):

    def setUp(self):
        self.dog = dog.Dog()

    def test_eat(self):
        self.assertFalse(self.dog.fed, "Dog started with fed True")

        self.dog.eat("dog food")
        self.assertTrue(self.dog.fed, "After eat, fed is False")


if __name__ == "__main__":
    unittest.main()
    