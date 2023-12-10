"""CS 5001 - 23fall - Project 8 - "The MyTime Class" - Kaiqi Zhang - 8 Nov 2023
"""


class MyTime:

    # def __init__(self, hrs=0, mins=0, secs=0):
    #     """ Create a MyTime object initialized to hrs, mins, secs """
    #     self.hours = hrs
    #     self.minutes = mins
    #     self.seconds = secs

    def __init__(self, hrs=0, mins=0, secs=0):
        """ Create a new MyTime object initialized to hrs, mins, secs.
           The values of mins and secs may be outside the range 0-59,
           but the resulting MyTime object will be normalized.
        """

        # Calculate total seconds to represent
        totalsecs = hrs*3600 + mins*60 + secs
        self.hours = totalsecs // 3600        # Split in h, m, s
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def __str__(self):
        """ print out the string representation of MyTime object """
        return print("({0}: {1}: {2})".format(self.hours, self.minutes,
                                              self.seconds))

    def increment(self, seconds):
        """ increate the time by given seconds """
        self.seconds += seconds

        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1

        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1

    def to_seconds(self):
        """ Return the number of seconds represented
            by this instance
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    # def after(self, time2):
    #     """ Return True if I am strictly greater than time2 """
    #     if self.hours > time2.hours:
    #         return True
    #     if self.hours < time2.hours:
    #         return False

    #     if self.minutes > time2.minutes:
    #         return True
    #     if self.minutes < time2.minutes:
    #         return False
    #     if self.seconds > time2.seconds:
    #         return True

    #     return False
    def after(self, time2):
        """ Return True if I am strictly greater than time2 """
        return self.to_seconds() > time2.to_seconds()

    def __add__(self, other):
        """ Create and return a new MyTime object after adding up the time """
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

    def __sub__(self, other):
        """ Create and return a new MyTime object after subtracting the time"""
        return MyTime(0, 0, self.to_seconds() - other.to_seconds())


# ======21.1 MyTime=====
# time1 = MyTime(11, 59, 30)
# print(str(time1))


# ======21.2 Pure functions======
# def add_time(t1, t2):
#     h = t1.hours + t2.hours
#     m = t1.minutes + t2.minutes
#     s = t1.seconds + t2.seconds
#     if s >= 60:
#         s -= 60
#         m += 1
#     if m >= 60:
#         m -= 60
#         h += 1
#     sum_t = MyTime(h, m, s)
#     return sum_t


# current_time = MyTime(9, 14, 30)
# bread_time = MyTime(3, 35, 0)
# done_time = add_time(current_time, bread_time)
# print(done_time)


# ======21.3 Modifiers======
# def increment(t, seconds):
#     t.seconds += seconds

#     while t.seconds >= 60:
#         t.seconds -= 60
#         t.minutes += 1

#     while t.minutes >= 60:
#         t.minutes -= 60
#         t.hours += 1


# ======21.4 Converting increment to a method======
# current_time = MyTime(20, 48, 38)
# current_time.increment(500)
# print(current_time)


# ======21.5 An "Aha!" insight======
# def add_time(t1, t2):
#     secs = t1.to_seconds() + t2.to_seconds()
#     return MyTime(0, 0, secs)


# current_time = MyTime(9, 54, 30)
# bread_time = MyTime(3, 35, 0)
# done_time = add_time(current_time, bread_time)
# print(done_time)


# ======21.8 Operator overloading======
# t1 = MyTime(1, 15, 42)
# t2 = MyTime(3, 50, 30)
# t3 = t1 + t2
# print(t3)


# ======21.9 Polymorphism======
# def multadd(x, y, z):
#     return x * y + z

# p1 = Point(3, 4)
# p2 = Point(5, 7)
# print(multadd(3, 2, 1))
# print(multadd(2, p1, p2))
# print(multadd(p1, p2, 1))


def front_and_back(front):
    """ print out a list twice, forward and backward """
    import copy
    back = copy.copy(front)
    back.reverse()
    print(str(front) + str(back))


my_list = [1, 2, 3, 4]
front_and_back(my_list)
