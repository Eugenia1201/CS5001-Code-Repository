"""CS 5001_Project5_Extension1_Kaiqi Zhang_21 Oct 2023 """

import re
Extensiondata = \
    "/Users/eugenia/Documents/CS5001/Day5/Project 5/\
        project5_extension1_data.txt"


# declaring global variables
all_halls = {}
all_movies = {}
all_audiences = {}
pattern = r'^A\d+$'
valid_movie_genres = ["Action", "Adventure", "Animation", "Comedy", "Crime",
                      "Drama", "Fantasy", "Horror", "Mystery", "Romance",
                      "Science Fiction", "Thriller", "Western",
                      "Documentary", "Family", "Musical", "War",
                      "Biography", "History", "Sport"]

# CREATION FUNCTIONS
#   Each takes parameters and returns a dictionary of the proper type


def new_hall(hall_number, available_seats):
    return dict(hall_number=hall_number, available_seats=available_seats)


def new_movie(name, genre, hall_number):
    return dict(name=name, genre=genre, hall_number=hall_number)


def new_audience(name, occupation, age, movie_watched):
    return dict(name=name, occupation=occupation, age=age,
                movie_watched=movie_watched)

# PRINTING FUNCTIONS
#   Upon calling, each function prints a report of corresponding data type


def print_hall_report():
    """fetch data items for halls in multiple dictionairies and print them
    out in a formatted manner
    """
    print("\n\nHALL REPORT")
    print("--------------------")
    for hall in all_halls:
        print(
            f"\nHall {all_halls.get(hall)['hall_number']} \
                \n{all_halls.get(hall)['available_seats']} Seats Available ")

        for movie in all_movies:
            if hall == all_movies.get(movie)["hall_number"]:
                print(f"Movie for today: '{movie}'")


def print_movie_report():
    """fetch data items for movies in multiple dictionairies and print
    them out in a formatted manner
    """
    print("\n\nMOVIE REPORT")
    print("--------------------")
    for movie in all_movies:
        hall_played = all_movies.get(movie)['hall_number']
        audience_watched = 0
        movies_watched_list = []
        print(
            f"\nMovie: '{movie}'\nGenre: {all_movies.get(movie)['genre']} \
                \nPlayed in hall: {hall_played}")
        for audience in all_audiences:
            movies_watched_list.append(
                all_audiences.get(audience)['movie_watched'])
            if movie in movies_watched_list and movie == all_audiences\
               .get(audience)['movie_watched']:
                audience_watched += 1

        # Calculating occupancy rate for all exisiting halls
        if hall_played in all_halls:
            occupancy_rate = (audience_watched / all_halls.get(hall_played)
                              ['available_seats'])*100
        else:
            occupancy_rate = 0
        print(
            f"Audience watched: {audience_watched}\
                \nOccupancy Rate:{occupancy_rate}%")


def print_audience_report():
    """fetch data items for audience in multiple dictionairies and print them
    out in a formatted manner
    """
    print("\n\nAUDIENCE REPORT")
    print("--------------------")
    for audience in all_audiences:
        movie_watched_today = all_audiences.get(audience)['movie_watched']
        hall_played = all_movies.get(movie_watched_today)['hall_number']
        occupation = all_audiences.get(audience)['occupation']
        print(
            f"\n{audience} watched '{movie_watched_today}' today in hall\
                {hall_played}.")
        for movie in all_movies:
            if movie == movie_watched_today:
                fav_genre = all_movies.get(movie)['genre']
                print(
                    f"{audience} is a {occupation}. \n{audience}'s favorite\
                        genre is {fav_genre}.")


# ADD NEW ENTRY FUNCTIONS
def add_new_hall():
    """Ask the user to enter hall_number and available seats; verify the input,
       create a new date entry and update the exisiting all_halls dictionary
    """
    global all_halls
    new_hall_number = get_valid_hall_number()
    new_available_seats = get_valid_available_seats()
    all_halls.update({new_hall_number: new_hall(
        new_hall_number, new_available_seats)})
    # print new report
    print_updated_h_report = input(
        "New hall record created. Enter 'yes' to view the new report:")
    if print_updated_h_report == "yes":
        print_hall_report()


def add_new_movie():
    """Ask the user to enter movie name, genre, and which hall to show; verify
    the input, create a new date entry and update the exisiting all_movies
    dictionary
    """
    global all_movies
    new_movie_name = input(
        "please type in the movie name: ")
    new_movie_genre = get_valid_new_movie_genre()
    new_movie_show_in_hall = get_valid_hall_number()
    all_movies.update({new_movie_name: new_movie(
        new_movie_name, new_movie_genre, new_movie_show_in_hall)})
    # print new report
    print_updated_m_report = input(
        "New movie record created. Enter 'yes' to view the new report:")
    if print_updated_m_report == "yes":
        print_movie_report()


def add_new_audience():
    """Ask the user to enter audience name, occupation, age and movie watched;
    verify the input, create a new date entry and update the exisiting
    all_audiences dictionary
    """
    new_audience_name = input("please type in audience name: ")
    new_audience_occupation = get_valid_occupation()
    new_audience_age = get_valid_age()
    new_movie_watched = get_valid_movie_watched()
    all_audiences.update({new_audience_name: new_audience(
        new_audience_name, new_audience_occupation, new_audience_age,
        new_movie_watched)})
    # print new report
    print_updated_a_report = input(
        "New audience record created. Enter 'yes' to view the new report:")
    if print_updated_a_report == "yes":
        print_audience_report()

# HELPER FUNCTIONS
#   Each funciton verifies user input to different questions


def get_valid_hall_number():
    """check if the hall number input by the user is in correct format
    """
    while True:
        new_hall = input(
            "please type in the hall number in the format 'A{n}': ")
        if re.match(pattern, new_hall):
            return new_hall
        else:
            print("Invalid hall number. Please enter a hall number in\
                  'A{n}' format.")


def get_valid_available_seats():
    """check if the available seats input by the user is in correct format
    and data range
    """
    while True:
        new_available_seats = input(
            "please type in the available_seats for this hall: ")
        if new_available_seats.isdecimal() and 10 <= \
           int(new_available_seats) <= 40:
            return new_available_seats
        else:
            print(
                "Invalid available seats. Please enter a integer value between\
                    10 and 40.")


def get_valid_new_movie_genre():
    """check if the movie genre input by the user is an avaible option
    """
    while True:
        new_movie_genre = input("please type in the movie genre: ").lower()
        for genre in valid_movie_genres:
            if new_movie_genre == genre.lower():
                return new_movie_genre
        else:
            print(
                "Invalid movie genre. Please enter a valid movie genre.")


def get_valid_occupation():
    """check if the audience occupation input by the user is an avaible option
    """
    while True:
        new_audience_occupation = input(
            "please type in audience occupation: ").lower()
        for audience in all_audiences:
            if new_audience_occupation == \
               all_audiences.get(audience)['occupation'].lower():
                return new_audience_occupation
        else:
            print(
                "Invalid occupation. Please enter a valid occupation.")


def get_valid_age():
    """check if the audience age input by the user is numerical value
    """
    while True:
        new_audience_age = input("please type in audience age: ")
        if new_audience_age.isdecimal():
            return new_audience_age
        else:
            print(
                "Invalid age. Please enter a valid age in integer format.")


def get_valid_movie_watched():
    """check if the movie entered by the user is currently showing in theaters
    """
    while True:
        new_movie_watched = input(
            "please type in the movie watched(first letter in capital): ")
        for movie in all_movies:
            if new_movie_watched == movie:
                return new_movie_watched
        else:
            print(
                "Invalid movie name. Please enter a valid movie name.")


# Populate data model
with open(Extensiondata, "r", newline="") as input_file:
    keep_reading = True
    while (keep_reading):
        input_line = input_file.readline()
        fields = input_line.strip().split("/")
        if input_line == "":
            # keep_reading = False
            break
        else:
            if (fields[0] == "HALL"):
                all_halls.update(
                    {fields[1]: new_hall(fields[1], int(fields[2]))})

            elif (fields[0] == "MOVIE"):
                all_movies.update(
                    {fields[1]: new_movie(fields[1], fields[2], fields[3])})

            elif (fields[0] == "AUDIENCE"):
                all_audiences.update({fields[1]: new_audience(
                    fields[1], fields[2], fields[3], fields[4])})

# MAIN PROGRAM
if (__name__ == "__main__"):
    LOOP_CONTINUE = True
    while LOOP_CONTINUE:
        input_string = input("please type in your command: ").lower()
        if input_string == "report":
            print_hall_report()
            print_movie_report()
            print_audience_report()
        elif input_string == "hall":
            add_new_hall()
        elif input_string == "movie":
            add_new_movie()
        elif input_string == "audience":
            add_new_audience()
        elif input_string == "bye":
            LOOP_CONTINUE = False
        else:
            print("Invalid input!")
