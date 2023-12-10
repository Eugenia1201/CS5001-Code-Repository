""" CS 5001 - Fall 2023 - Professor Shafer - Day 5 Lab "Time For School"
    New and improved!  Now with objects!

    Steps to get here from version 1:
    * add links across object types where we have pointers
    * use these links instead of always looking things up
    * add App model
"""

# DATA MODEL


class School:
    def __init__(self):
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
                        r = Room(self, input_fields[1], int(input_fields[2]))
                        self.all_rooms[input_fields[1]] = r
                    elif command == "course":
                        c = Course(self, input_fields[1], input_fields[2],
                                   input_fields[3])
                        self.all_courses[input_fields[1]] = c
                    else:  # student
                        s = Student(self, input_fields[1], input_fields[2],
                                    input_fields[3])
                        self.all_students.append(s)
        # Create cross-links
        for room_number, r in self.all_rooms.items():
            r.crosslink()
        for course_number, c in self.all_courses.items():
            c.crosslink()
        for s in self.all_students:
            s.crosslink()

    def get_room(self, room_number):
        return self.all_rooms[room_number]

    def get_course(self, course_number):
        return self.all_courses[course_number]

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
    def __init__(self, school, room_number, capacity):
        self.school = school
        self.room_number = room_number
        self.capacity = capacity
        self.courses = []

    def crosslink(self):
        for course_number, c in self.school.all_courses.items():
            if c.room_number == self.room_number:
                self.courses.append(c)

    def check_capacity(self):
        all_courses_ok = True
        for c in self.courses:
            number_of_students = len(c.students)
            if number_of_students > self.capacity:
                print(f"Room {self.room_number} (capacity {self.capacity})\
- {c.name} ({c.course_number}) has {number_of_students} students")
                all_courses_ok = False
        return all_courses_ok


class Course:
    def __init__(self, school, course_number, name, room_number):
        self.school = school
        self.course_number = course_number
        self.name = name
        self.room_number = room_number
        self.room = None
        self.students = []

    def crosslink(self):
        self.room = self.school.get_room(self.room_number)
        for s in self.school.all_students:
            if s.course_number == self.course_number:
                self.students.append(s)

    def report(self):
        print(f"{self.course_number}: {self.name} in Room {self.room_number}")
        for s in self.students:
            print(f"\t{s.name}")


class Student:
    def __init__(self, school, name, address, course_number):
        self.school = school
        self.name = name
        self.address = address
        self.course_number = course_number
        self.course = None

    def crosslink(self):
        self.course = self.school.get_course(self.course_number)

    def report(self):
        print(self.name)
        print("\t{self.address}")
        print(f"\t{self.course.name}")


# THE APPLICATION

class App:
    def __init__(self):
        pass

    def run(self):
        sc = School()
        sc.populate("Lab5data.txt")
        sc.report()


# MAIN PROGRAM

if __name__ == "__main__":

    app = App()
    app.run()
