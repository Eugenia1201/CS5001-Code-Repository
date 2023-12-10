""" CS 5001 - Fall 2023 - Professor Shafer - Day 5 Lab "Time For School"
"""

# DATA MODEL
all_rooms = dict()
all_courses = dict()
all_students = []


# POPULATE DATA MODEL

def populate_data_model(filename):
    """Populate complete data model

    Args:
        filename (string): filename of the data file
    """
    with open(filename, "r", newline="") as input_file:
        while (input_line := input_file.readline()) != "":
            input_fields = input_line.strip().split("/")
            command = input_fields[0].lower()
            if command == "room":
                r = new_room(input_fields[1], int(input_fields[2]))
                all_rooms[input_fields[1]] = r
            elif command == "course":
                c = new_course(input_fields[1], input_fields[2],
                               input_fields[3])
                all_courses[input_fields[1]] = c
            else:  # student
                s = new_student(input_fields[1], input_fields[2],
                                input_fields[3])
                all_students.append(s)


def new_room(room_number, capacity):
    """Create new room

    Args:
        room_number (string): Number of the room
        capacity (int): How many students can fit in the room

    Returns:
        dictionary: student description
    """
    return dict(room_number=room_number, capacity=capacity)


def new_course(course_number, name, room_number):
    """Create new course

    Args:
        course_number (string): Number of the course
        name (string): Course name
        room_number (string): Number of the room for this course

    Returns:
        dictionary: course description
    """
    return dict(course_number=course_number, name=name,
                room_number=room_number)


def new_student(name, address, course_number):
    """Create new student

    Args:
        name (string): Student's name
        address (string): Student's address (street address, city, state)
        course_number (string): Number of the student's course

    Returns:
        dictionary: student description
    """
    return dict(name=name, address=address,
                course_number=course_number)


# REPORTING

def report_students():
    """Print report on students
    """
    print()
    print()
    print("STUDENT REPORT")
    for s in all_students:
        print(f"{s['name']}")
        print(f"\t{s['address']}")
        print(f"\t{all_courses[s['course_number']]['name']}")


def report_courses():
    """Print report on courses
    """
    print()
    print()
    print("COURSE REPORT")
    for course_number, c in all_courses.items():
        print(f"{c['course_number']}: {c['name']} in Room {c['room_number']}")
        for s in all_students:
            if s['course_number'] == c['course_number']:
                print(f"\t{s['name']}")


def report_rooms():
    """Print report on rooms
    """
    print()
    print()
    print("ROOM CAPACITY CHECK")
    all_rooms_ok = True
    for room_number, r in all_rooms.items():
        for course_number, c in all_courses.items():
            if c['room_number'] == r['room_number']:
                number_of_students = 0
                for s in all_students:
                    if s['course_number'] == c['course_number']:
                        number_of_students += 1
                if number_of_students > r['capacity']:
                    print(f"Room {r['room_number']} (capacity {r['capacity']})\
    - {c['name']} ({c['course_number']}) has {number_of_students} students")
                    all_rooms_ok = False
    if all_rooms_ok:
        print("All rooms are within capacity limit")


if __name__ == "__main__":

    populate_data_model("Lab5data.txt")
    report_students()
    report_courses()
    report_rooms()
