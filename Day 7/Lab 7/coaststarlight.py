import enum


class Station(enum.Enum):
    SEATTLE = 1
    PORTLAND = 2
    SAN_JOSE = 3
    LOS_ANGELES = 4


class CoastStarlight:
    def __init__(self):
        self.location = Station.SEATTLE
        self.clock = 6

    def all_aboard(self):
        if self.location is None:
            return
        elif self.location == Station.LOS_ANGELES:
            self.location = None
        else:
            self.location = Station(self.location.value+1)
            self.clock = (self.clock % 12) + 1

    def set_clock(self, time):
        if 0 <= time <= 12:
            self.clock = time
        elif time > 12:
            self.clock = (time % 12)
        else:
            self.clock = 0


# Main Program
train = CoastStarlight()
print(train.location, train.clock)
train.all_aboard()
print(train.location, train.clock)
train.all_aboard()
print(train.location, train.clock)
train.all_aboard()
print(train.location, train.clock)
train.all_aboard()
print(train.location, train.clock)
