def read_school_data(filename):
    all_rooms = {}
    all_courses = {}
    all_students = []

    with open(filename, "r", newline="") as input_file:
        while (input_line := input_file.readline()) != "":
            input_line = input_line.strip()
            fields = input_line.split("/")
            data_type = fields[0]

            if data_type == "ROOM":
                room_number, capacity = fields[1], int(fields[2])
                room_data = {"room_number": room_number, "capacity": capacity}
                all_rooms[room_number] = room_data

            elif data_type == "COURSE":
                course_number, course_name, room_number = fields[1], fields[2],
                fields[3]
                course_data = {"course_number": course_number,
                               "name": course_name, "room_number": room_number}
                all_courses[course_number] = course_data

            elif data_type == "STUDENT":
                student_name, address, course_number = fields[1], fields[2],
                fields[3]
                student_data = {"name": student_name, "address": address,
                                "course_number": course_number}
                all_students.append(student_data)

    return all_rooms, all_courses, all_students


# Call the function to read the data and create the data model
all_rooms, all_courses, all_students = \
    read_school_data("/Users/eugenia/Documents/CS5001/Day5/Lab5/Lab5data.txt")

print(all_rooms)

print("\nSTUDENT REPORT")
print("===============")

for student in all_students:
    course_number = student["course_number"]
    course_name = all_courses.get(course_number, {}).get("name",
                                                         "Unknown Course")
    print(f"Student's Name: {student['name']}")
    print(f"Student's Address: {student['address']}")
    print(f"Course Name: {course_name}\n")

print("\nCOURSE REPORT")
print("===============")

for course_number, course_info in all_courses.items():
    students_in_course = [s['name'] for s in all_students if s['course_number']
                          == course_number]
    student_list = "\n".join(students_in_course)
    print(f"Course Number: {course_info['course_number']} - \
          {course_info['name']} in Room {course_info['room_number']}")
    print(student_list)

# Print a couple of blank lines
print("\n\n")

# Print the header
print("ROOM CAPACITY CHECK")
print("===================")

# Iterate through courses to check room capacity
for course_number, course_info in all_courses.items():
    room_number = course_info["room_number"]
    room_capacity = all_rooms.get(room_number, {}).get("capacity", 0)
    enrolled_students = len([s for s in all_students if s["course_number"]
                             == course_number])

    print(f"Course Number: {course_info['course_number']} - \
          {course_info['name']} in Room {room_number}")
    print(f"Enrolled Students: {enrolled_students}")
    print(f"Room Capacity: {room_capacity}")

    if enrolled_students > room_capacity:
        print(f"WARNING: Too many students for this room! Students: \
               {enrolled_students}, Capacity: {room_capacity}")
    else:
        print("Room capacity is sufficient.")

    print("=" * 30)

# Check if all courses are within capacity
if all(enrolled_students <= room_capacity for course_number, course_info in
       all_courses.items()):
    print("All courses are within the room's capacity.")
