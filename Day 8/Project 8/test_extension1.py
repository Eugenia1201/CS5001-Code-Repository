import unittest
import extension1


class Test_Rectangle(unittest.TestCase):
    def test_area(self):
        r = extension1.Rectangle(extension1.Point(0, 0), 10, 5)
        self.assertEqual(r.area(), 50,
                         "The area of the rectangle should be 50")

    def test_perimeter(self):
        r = extension1.Rectangle(extension1.Point(0, 0), 10, 5)
        self.assertEqual(r.perimeter(), 30,
                         "The perimeter of the rectangle should be 30")

    def test_flip(self):
        r = extension1.Rectangle(extension1.Point(100, 50), 10, 5)
        r.flip()
        self.assertEqual(r.width, 5,
                         "The width after flip should be 5")
        self.assertEqual(r.height, 10,
                         "The height after flip should be 10")

    def test_contains(self):
        r = extension1.Rectangle(extension1.Point(0, 0), 10, 5)
        self.assertTrue(r.contains(extension1.Point(0, 0)))
        self.assertTrue(r.contains(extension1.Point(3, 3)))
        self.assertFalse(r.contains(extension1.Point(3, 7)))
        self.assertFalse(r.contains(extension1.Point(3, 5)))
        self.assertTrue(r.contains(extension1.Point(3, 4.9999)))
        self.assertFalse(r.contains(extension1.Point(-3, -3)))

    def test_collision(self):
        r1 = extension1.Rectangle(extension1.Point(0, 0), 10, 5)
        r2 = extension1.Rectangle(extension1.Point(10, 5), 10, 5)
        self.assertFalse(r1.collision_detection(r2))


if __name__ == "__main__":
    unittest.main()
