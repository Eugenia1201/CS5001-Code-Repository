""" CS 5001 - Fall 2023 - Professor Shafer - Day 5 Lab "Time For School"
    New and improved!  Now with objects!

    Steps to get here from original Lab code:
    * Create classes for room, course, student
    * Add __init__ for each of these classes
    * Use classes in populating data model
    * Add School class
    * Move populating code into School class
"""

# DATA MODEL


class School:
    def __init__(self, filename=""):
        self.all_rooms = dict()
        self.all_courses = dict()
        self.all_students = []

    def populate(self, filename=""):
        self.all_rooms.clear()
        self.all_courses.clear()
        self.all_students.clear()

        # Populate data model
        if filename != "":
            with open(filename, "r", newline="") as input_file:
                while (input_line := input_file.readline()) != "":
                    input_fields = input_line.strip().split("/")
                    command = input_fields[0].lower()
                    if command == "room":
                        r = Room(input_fields[1], int(input_fields[2]))
                        self.all_rooms[input_fields[1]] = r
                    elif command == "course":
                        c = Course(input_fields[1], input_fields[2],
                                   input_fields[3])
                        self.all_courses[input_fields[1]] = c
                    else:  # student
                        s = Student(input_fields[1], input_fields[2],
                                    input_fields[3])
                        self.all_students.append(s)

    def report(self):
        print()
        print()
        print("STUDENT REPORT")
        for s in self.all_students:
            s.report()
        print()
        print()
        print("COURSE REPORT")
        for course_number, c in self.all_courses.items():
            c.report()
        print()
        print()
        print("ROOM CAPACITY CHECK")
        all_rooms_ok = True
        for room_number, r in self.all_rooms.items():
            this_room_ok = r.check_capacity()
            if not this_room_ok:
                all_rooms_ok = False
        if all_rooms_ok:
            print("All rooms are within capacity limit")


class Room:
    def __init__(self, room_number, capacity):
        self.room_number = room_number
        self.capacity = capacity

    def check_capacity(self):
        all_courses_ok = True
        for course_number, c in school.all_courses.items():
            if c.room_number == self.room_number:
                number_of_students = 0
                for s in school.all_students:
                    if s.course_number == c.course_number:
                        number_of_students += 1
                if number_of_students > self.capacity:
                    print(f"Room {self.room_number} (capacity {self.capacity})\
- {c.name} ({c.course_number}) has {number_of_students} students")
                    all_courses_ok = False
        return all_courses_ok


class Course:
    def __init__(self, course_number, name, room_number):
        self.course_number = course_number
        self.name = name
        self.room_number = room_number

    def report(self):
        print(f"{self.course_number}: {self.name} in Room {self.room_number}")
        for s in school.all_students:
            if s.course_number == self.course_number:
                print(f"\t{s.name}")


class Student:
    def __init__(self, name, address, course_number):
        self.name = name
        self.address = address
        self.course_number = course_number

    def report(self):
        print(self.name)
        print("\t" + self.address)
        print(f"\t{school.all_courses[self.course_number].name}")


# MAIN PROGRAM


if __name__ == "__main__":

    school = School()
    school.populate("Lab5data.txt")
    school.report()
