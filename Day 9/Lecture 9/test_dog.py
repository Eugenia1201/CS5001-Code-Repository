"""Unit test for raised exceptions"""

import unittest
import dog


class Test_Dog(unittest.TestCase):

    def setUp(self) -> None:
        self.dog = dog.Dog()

    def test_eat(self):
        self.assertFalse(self.dog.fed)

        self.dog.eat("dog food")
        self.assertTrue(self.dog.fed)

    def test_bark(self):
        with self.assertRaises(Exception) as context:
            self.dog.bark()
        self.assertTrue(isinstance(context.exception, AttributeError))


if __name__ == "__main__":
    unittest.main()
