import unittest
import coaststarlight


class Test_Location(unittest.TestCase):
    def test_init_location(self):
        c = coaststarlight.CoastStarlight()
        self.assertEqual(c.location, coaststarlight.Station.SEATTLE,
                         "Train should start in Seattle")

    def test_all_location(self):
        c = coaststarlight.CoastStarlight()

        # Move the train through all stations
        c.all_aboard()
        self.assertEqual(c.location, coaststarlight.Station.PORTLAND,
                         "The train's second stop is Portland")
        c.all_aboard()
        self.assertEqual(c.location, coaststarlight.Station.SAN_JOSE,
                         "The train's third stop is San Jose")
        c.all_aboard()
        self.assertEqual(c.location, coaststarlight.Station.LOS_ANGELES,
                         "The train's fourth stop is Los Angeles")
        c.all_aboard()
        self.assertEqual(c.location, None,
                         "The train should be in None")
        # Calling all_aboard() again should not change the location from None
        c.all_aboard()
        self.assertEqual(c.location, None,
                         "The train should be in None")


class Test_Clock(unittest.TestCase):
    def test_init_clock(self):
        c = coaststarlight.CoastStarlight()
        self.assertEqual(c.clock, 6,
                         "Clock is initialized to 6")

    def test_clock_updates(self):
        c = coaststarlight.CoastStarlight()

        # Check clock updates with all_broad() being called:
        c.all_aboard()
        self.assertEqual(c.clock, 7,
                         "Clock updates to 7 when moving to next station")
        c.all_aboard()
        self.assertEqual(c.clock, 8,
                         "Clock updates to 8 when moving to next station")
        c.all_aboard()
        self.assertEqual(c.clock, 9,
                         "Clock updates to 9 when moving to next station")
        c.all_aboard()
        self.assertEqual(c.clock, 9,
                         "Clock stays at 9")
        c.all_aboard()
        self.assertEqual(c.clock, 9,
                         "Clock stays at 9")

    def test_set_clock(self):
        c = coaststarlight.CoastStarlight()

        # Check clock is updated to the new value when set_clock() is called:
        c.set_clock(9)
        self.assertEqual(c.clock, 9,
                         "Clock should be set to 9")

        # Check clock updates with all_broad() being called:
        c.all_aboard()
        self.assertEqual(c.clock, 10,
                         "Clock updates to 10 when all_board() is called")

        # Check the closck reset from 13 back to 1:
        c.set_clock(13)
        self.assertEqual(c.clock, 1,
                         "Clock should be reset to 1 ")


if __name__ == "__main__":
    unittest.main()
