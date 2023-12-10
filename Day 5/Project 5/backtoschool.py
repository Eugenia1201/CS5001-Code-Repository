"""CS 5001_Project5_Kaiqi Zhang_18 Oct 2023 """

import random

Project5Data = \
    "/Users/eugenia/Documents/CS5001/Day5/Project 5/Project5data.txt"

# Delcare as global variables

all_rooms = {}
all_courses = {}
all_students = {}
all_faculty = {}
all_sections = {}
new_section_number = 315


# CREATION FUNCTIONS
#   Each takes parameters and returns a dictionary of the proper type

def new_room(room_number, capacity):
    return dict(room_number=room_number, capacity=capacity)


def new_course(course_number, name):
    return dict(course_number=course_number, name=name)


def new_student(name, address, phone, sections_taking):
    return dict(name=name, address=address, phone=phone,
                sections_taking=sections_taking)


def new_faculty(name, address, phone, sections_taught):
    return dict(name=name, address=address, phone=phone,
                sections_taught=sections_taught)


def new_section(section_number, course_number, room_number, weekday):
    return dict(section_number=section_number, course_number=course_number,
                room_number=room_number, weekday=weekday)

# PRINTING FUNCTIONS
#   Upon calling, each function prints a report of corresponding data type


def print_all_students():
    """fetch data items for students in multiple dictionairies and print them
    out in a formatted manner
    """

    print("\n\n\nSTUDENT REPORT")
    print("-" * 30)

    for key in all_students:
        student_name = all_students.get(key)['name']
        student_phone = all_students.get(key)['phone']
        student_address = all_students.get(key)['address']

        print(f"\n{student_name}, {format_phone_number(student_phone)}")

        print(f"     {format_address(student_address)}")

        for item in all_students.get(key)['sections_taking']:
            curr_course_number = all_sections.get(item, {}).get(
                'course_number', "Unknown Course Number")
            curr_course_name = all_courses.get(
                curr_course_number, {}).get('name', "Unknown Course")

            curr_section_day = all_sections.get(
                item, {}).get('weekday', "Unknown Weekday")
            curr_room_number = all_sections.get(
                item, {}).get('room_number', "Unknown Room")
            print(
                f"     {curr_course_name} - Section {item} -\
                    {curr_section_day}- Room {curr_room_number}")


def print_all_faculty():
    """fetch data items for faculty in multiple dictionairies and print them
    out in a formatted manner
    """

    print("\n\n\nFACULTY REPORT")
    print("-" * 30)
    for key in all_faculty:
        faculty_name = all_faculty.get(key)['name']
        faculty_phone = all_faculty.get(key)['phone']
        faculty_address = all_faculty.get(key)['address']

        print(f"\n{faculty_name}, {format_phone_number(faculty_phone)}")

        print(f"     {format_address(faculty_address)}")

        for item in all_faculty.get(key)['sections_taught']:
            curr_course_number = all_sections.get(item, {}).get(
                'course_number', "Unknown Course Number")
            curr_course_name = all_courses.get(
                curr_course_number, {}).get('name', "Unknown Course")

            curr_section_day = all_sections.get(
                item, {}).get('weekday', "Unknown Weekday")
            curr_room_number = all_sections.get(
                item, {}).get('room_number', "Unknown Room")
            print(
                f"     {curr_course_name} - Section {item} -\
                {curr_section_day} - Room {curr_room_number}")


def print_all_courses():
    """fetch data items for courses in multiple dictionairies and print them
    out in a formatted manner
    """
    print("\n\n\nCOURSE REPORT")
    print("-" * 30)
    for course_key in all_courses:
        print(
            f"\n{all_courses.get(course_key)['course_number']}-\
                {all_courses.get(course_key)['name']}")
        section_list = []
        for section_key in all_sections:
            if all_sections.get(section_key).get("course_number")\
                  == course_key:
                section_list.append(section_key)
        for section in section_list:
            print(
                f"     Section {section} -\
                    {all_sections.get(section)['weekday']} - Room \
                        {all_sections.get(section)['room_number']} ")


def print_all_sections():
    """fetch data items for sections in multiple dictionairies and print them
    out in a formatted manner
    """
    print("\n\n\nSECTION REPORT")
    print("-" * 30)

    for section_key in all_sections:
        course_number = all_sections.get(section_key)['course_number']
        print(
            f"\nSection {section_key} of {course_number}-\
                {all_courses.get(course_number)['name']} meets\
                    {all_sections.get(section_key)['weekday']} in Room\
                    {all_sections.get(section_key)['room_number']}")

        for faculty_key in all_faculty:
            if section_key in all_faculty.get(faculty_key)['sections_taught']:
                print(f"     Taught by {faculty_key}")

        for student_key in all_students:
            if section_key in all_students.get(student_key)['sections_taking']:
                print(f"     {student_key}")


# HELPER FUNCTIONS
#   Each funciton verifies user input to different questions
def get_valid_address():
    """check if the input has 3 parts and separared by commas
    """
    while True:
        address = (input("please type in your adderss in the order of street,\
                         city and state: "))
        parts = address.split(',')
        if len(parts) == 3 and all(part.strip() for part in parts):
            return address
        else:
            print(
                "Invalid address format. Please enter a valid address with 3\
                    parts separated by commas.")


def get_valid_phone():
    """check if the input data is integer and the length is 10
    """
    while True:
        phone = input("please type in your phone number(10 digits): ")
        if phone.isdecimal() and len(phone) == 10:
            return phone
        else:
            print("Invalid phone number format. Please enter a 10-digit phone\
                  number.")


def get_valid_course_number():
    """check if the input course number is an exisiting one
    """
    while True:
        user_course_number = input("please type in your course number: ")
        if user_course_number in list(all_courses):
            return user_course_number
        else:
            print(
                "Invalid course number. Please enter a valid course number.")


def get_valid_faculty_member():
    """check if the input faculty member is an exisiting one
    """
    while True:
        user_falculty_name = input("please type in faculty member name: ")
        if user_falculty_name in all_faculty:
            return user_falculty_name
        else:
            print(
                "Invalid faculty member name. Please enter a valid faculty\
                    member.")


def get_valid_room_member():
    """check if the input room number is an exisiting one
    """
    while True:
        user_room_number = input("please type in room number: ")
        if user_room_number in all_rooms:
            return user_room_number
        else:
            print(
                "Invalid room number. Please enter the correct room number.")


# ADD NEW ENTRY FUNCTIONS

def add_new_student():
    """Ask the user to enter student's name, address and phone number; verify
    the input, create a new date entry and update the exisiting all_students
    dictionary
    """
    global all_students
    student_name = input("please type in your name")
    student_address = get_valid_address()
    student_phone = get_valid_phone()
    all_students.update({student_name: new_student(
        student_name, student_address, student_phone, [])})
    # print new report
    print_updated_s_report = input(
        "Student record created. Enter 'yes' to view the new report:")
    if print_updated_s_report == "yes":
        print_all_students()


def add_new_faculty():
    """Ask the user to enter faculty's name, address and phone number; verify
    the input, create a new date entry and update the exisiting all_faculty
    dictionary
    """
    global all_faculty
    new_faculty_name = input("please type in your name")
    new_faculty_address = get_valid_address()
    new_faculty_phone = get_valid_phone()
    all_faculty.update({new_faculty_name: new_faculty(
        new_faculty_name, new_faculty_address, new_faculty_phone, [])})
    # print new report
    print_updated_f_report = input(
        "Faculty record created. Enter 'yes' to view the new report:")
    if print_updated_f_report == "yes":
        print_all_faculty()


def add_new_section():
    """Ask the user to enter section number, course number, faculty name, room
    number and weekday; verify the input, create a new date entry and update
    the exisiting all_sections dictionary
    """
    global all_sections
    global new_section_number
    new_section_number += 1
    new_course_number = get_valid_course_number()
    new_faculty_name = get_valid_faculty_member()
    new_room_number = get_valid_room_member()
    weekday = input("Weekday: ")
    all_sections.update({str(new_section_number): new_section(
        str(new_section_number), new_course_number, new_room_number, weekday)})

    # pick students randomly and add them to the section
    num_student = random.randint(5, 9)
    selected_students = random.sample(all_students.keys(), num_student)
    # append new section number to selected students
    for selected_student in selected_students:
        all_students.get(selected_student)[
            'sections_taking'].append(str(new_section_number))
    # append new section number to corresponding faculty
    for faculty_key in all_faculty:
        if faculty_key == new_faculty_name:
            all_faculty.get(faculty_key)['sections_taught'].append(
                str(new_section_number))
    # print new report
    print_updated_s_report = input(
        "Section record created. Enter 'yes' to view the new report:")
    if print_updated_s_report == "yes":
        print_all_sections()


# REFORMATING FUNCTIONS
#   each takes the orignal value as the input and return a formatted one

def format_address(original_address):
    """funtion to reformat address

    Args:
        original_address (string): original address, 3 parts separared by
        commas

    Returns:
        string: replace the first "," with ";"
    """
    return original_address.replace(",", ";", 1)


def format_phone_number(phone_number):
    """function to reformat phone number

    Args:
        phone_number (string): original phone number, 10-digit long

    Returns:
        string: reformat the phone number with area code wrapped in "()",
        and telephone prefix and line number separated by "-".
    """
    return "({}) {}-{}".format(phone_number[:3], phone_number[3:6],
                               phone_number[6:])


# Populate data model
with open(Project5Data, "r", newline="") as input_file:
    keep_reading = True
    while (keep_reading):
        input_line = input_file.readline()
        fields = input_line.strip().split("/")
        if input_line == "":
            keep_reading = False
        else:
            if (fields[0] == "ROOM"):
                all_rooms.update(
                    {fields[1]: new_room(fields[1], int(fields[2]))})

            elif (fields[0] == "COURSE"):
                all_courses.update(
                    {fields[1]: new_course(fields[1], fields[2])})

            elif (fields[0] == "STUDENT"):
                total_sections_taking = fields[4].split(",")
                all_students.update({fields[1]: new_student(
                    fields[1], fields[2], fields[3], total_sections_taking)})

            elif (fields[0] == "FACULTY"):
                total_sections_taught = fields[4].split(",")
                all_faculty.update({fields[1]: new_faculty(
                    fields[1], fields[2], fields[3], total_sections_taught)})

            elif (fields[0] == "SECTION"):
                all_sections.update({fields[1]: new_section(
                    fields[1], fields[2], fields[3], fields[4])})


# MAIN PROGRAM

if (__name__ == "__main__"):
    print(all_rooms)
    print(all_courses)
    print(all_students)
    print(all_faculty)
    print(all_sections)

    LOOP_CONTINUE = True
    while LOOP_CONTINUE:
        input_string = input("please type in your command:").lower()
        if input_string == "report":
            print_all_students()
            print_all_faculty()
            print_all_courses()
            print_all_sections()
        elif input_string == "student":
            add_new_student()
        elif input_string == "faculty":
            add_new_faculty()
        elif input_string == "section":
            add_new_section()
        elif input_string == "bye":
            LOOP_CONTINUE = False
        else:
            print("Invalid input!")
