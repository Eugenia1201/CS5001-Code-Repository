"""Generate data for Project5-Extension1 and write it into a file
"""

import random
project5_extension1_data = \
    "/Users/eugenia/Documents/CS5001/Day5/Project 5/project5_extension1_data.txt"

#CREATION FUNCTIONS
#   Each takes parameters and returns a dictionary of the proper type

def new_hall(hall_number, available_seats):
    return dict(hall_number=hall_number, available_seats=available_seats)

def new_movie(name, genre, hall_number):
    return dict(name=name, genre=genre, hall_number=hall_number)

def new_audience(name, occupation, age, movied_watched):
    return dict(name=name,occupation=occupation,age=age,movied_watched=movied_watched)

#WRITING FUNCTIONS
#   Each takes a dictionary entry of a given type and returns it in a string

def show_hall(h):
    return f"HALL/{h['hall_number']}/{h['available_seats']}"

def show_movie(m):
    return f"MOVIE/{m['name']}/{m['genre']}/{m['hall_number']}"

def show_audience(a):
    return f"AUDIENCE/{a['name']}/{a['occupation']}/{a['age']}/{a['movied_watched']}"

#MAIN PROGRAM
if(__name__ == "__main__"):

    names = ["Emma", "Liam", "Olivia", "Noah", "Ava", "Isabella", "Sophia", "Mia", "Charlotte", "Amelia",
             "Harper", "Evelyn", "Abigail", "Emily", "Elizabeth", "Sofia", "Ella", "Madison", "Scarlett", "Grace",
             "William", "James", "Oliver", "Benjamin", "Elijah", "Lucas", "Henry", "Alexander", "Sebastian", "Joseph",
             "Samuel", "Matthew", "David", "Daniel", "Mason", "Michael", "Andrew", "Ethan", "Nicholas", "Anthony"]

    movies = {"The Shawshank Redemption": "Drama",  "The Godfather": "Crime",  "Pulp Fiction": "Crime",
             "The Dark Knight": "Action",  "Forrest Gump": "Drama", "Schindler's List": "Biography",
              "The Lord of the Rings: The Return of the King": "Fantasy", "Inception": "Sci-Fi",
              "The Matrix": "Sci-Fi", "The Avengers": "Action" }
            
    occupations = ["Teacher","Doctor", "Engineer","Accountant","Chef","Police Officer",
                    "Graphic Designer","Electrician","Writer","Software Developer"]

    #make halls
    all_halls = []
    for i in range(1,4):
        r = new_hall("A"+str(i),10)
        all_halls.append(r)
    for i in range(4, 6):
        r = new_hall("A"+str(i), 20)
        all_halls.append(r)
    
    #make movies
    all_movies = []
    for movie in movies:
        movie_name = movie
        movie_genre = movies.get(movie)
        hall = all_halls[random.randrange(len(all_halls))]
        m = new_movie(movie, movie_genre, hall['hall_number'])
        all_movies.append(m)

    #make audience
    all_audiences = []
    for i in range(40):
        name = names[random.randrange(len(names))]
        occupation = occupations[random.randrange(len(occupations))]
        age = random.randrange(20,56)
        movie_watched = all_movies[random.randrange(len(all_movies))]
        a = new_audience(name,occupation,age,movie_watched['name'])
        all_audiences.append(a)
    
    #write output file
    with open(project5_extension1_data, "w", newline="") as output_file:
        for h in all_halls:
            output_file.write(show_hall(h) + "\n")
        for m in all_movies:
            output_file.write(show_movie(m) + "\n")
        for a in all_audiences:
            output_file.write(show_audience(a) + "\n")
        


