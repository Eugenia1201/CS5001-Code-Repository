
import random


""" Dump data for Lab 5 into a file
"""


#  CREATION FUNCTIONS
#    Each takes parameters and returns a dictionary of the proper type

def new_room(room_number, capacity):
    return dict(room_number=room_number, capacity=capacity)


def new_course(course_number, name, room_number):
    return dict(course_number=course_number, name=name,
                room_number=room_number)


def new_student(name, address, course_number):
    return dict(name=name, address=address,
                course_number=course_number)


# WRITING FUNCTIONS
#   Each takes a dictionary entry of a given type and returns it in a string


def show_room(r):
    return f"ROOM/{r['room_number']}/{r['capacity']}"


def show_course(c):
    return f"COURSE/{c['course_number']}/{c['name']}/{c['room_number']}"


def show_student(s):
    return f"STUDENT/{s['name']}/{s['address']}/{s['course_number']}"


# CONFIG

N_ROOMS = 3
N_STUDENTS = 24

# MAIN PROGRAM

if (__name__ == "__main__"):

    names = ["Abba", "Bibi", "Coco", "Dada", "Elle", "Fafa", "Goog", "Hihi",
             "Illi", "Jojo", "Kuku", "Lala", "Momo", "Nene", "Oppo", "Popo",
             "Ququ", "RaRa", "Soso", "Tutu", "Ullu", "Vava", "Wowo", "Xixi",
             "Yaya", "Zozo"]

    streets = ["Main Street, Seattle, WA", "Fifth Avenue, Issaquah, WA",
               "University Avenue, Seattle, WA", "Terry Avenue N, Seattle, WA"]

    course_names = ["Astronomy", "Biology", "Chemistry", "Design", "Economics"]

    # make rooms
    all_rooms = []
    for i in range(N_ROOMS):
        # room numbers are 401, 402, ...
        # capacity of all rooms is 5
        r = new_room(401+i, 5)
        all_rooms.append(r)

    # make courses
    all_courses = []
    for i in range(len(course_names)):
        # course numbers are 101, 102, ...
        # random room
        course_number = 101 + i
        room = all_rooms[random.randrange(len(all_rooms))]
        c = new_course(course_number, course_names[i], room['room_number'])
        all_courses.append(c)

    # make students
    all_students = []
    for _ in range(N_STUDENTS):
        # name is random first name and random last name
        # address is random number followed by a random street
        # course is randomly picked
        name = names[random.randrange(len(names))]\
            + " " + names[random.randrange(len(names))]
        address = str(random.randrange(1000)) + " "\
            + streets[random.randrange(len(streets))]
        course = all_courses[random.randrange(len(all_courses))]
        s = new_student(name, address, course['course_number'])
        all_students.append(s)

    # write output file
    with open("Lab5data.txt", "w", newline="") as output_file:
        for r in all_rooms:
            output_file.write(show_room(r) + "\n")
        for c in all_courses:
            output_file.write(show_course(c) + "\n")
        for s in all_students:
            output_file.write(show_student(s) + "\n")
