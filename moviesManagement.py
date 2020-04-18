"""
Python program to manage movies such as adding,watching,deleting,searching.
Author:Chinmay Bharadwaj
Some notes:
-Enter'a' is  add movie,'l' to see the movie,'f' find the movie, and 'q' to quit the program

Tasks/Steps:
[X]:Where to store the movie
[X]:Show user the menu and select the option
[X]:Allow the user to add movie
[X]:Show all their movies
[]:Find the movie
[X]:Stop running the program when user enters 'q'

"""
#main list holding data of the all movies
movies= []

"""
This list movies contains all the user data
the data stored are in the below format
movie=[
    {
        'name':'str',
        'director':'str',
        'year':number
    }..........
]
"""

#funtion to display the menu
def menu():
    user_input=input("Enter 'a' is to add movie,'l' to see the movie,'f' find the movie, and 'q' to quit the program:  ")
    user_input=user_input.lower()
    while user_input!='q':
        if user_input=='a':
            addMovies()
        elif user_input=='l':
            showMovies()
            print("")
        elif user_input=='f':
            findMovies()
            
        else:
            print("Unknown key please try again")
        user_input=input("Enter 'a' is to add movie,'l' to see the movie,'f' find the movie, and 'q' to quit the program:  ")


#Function to add movie to the movie list
def addMovies():
    print("----------adding----------")
    name=input("Enter the name of the movie  :")
    director=input("Enter the name of the director :")
    year=input("Enter the year in which it was released  :")
    movies.append(
        {
            'name':name,
            'director':director,
            'year':year
        }
    )
#function which shows the list of movies
def showMovies():
    print("----------printing---------- ")
    for mov in movies:
        showMovieDetail(mov)
        print("--------------------")

#Function to print movie detail by passing the list of the movies as a parameter       
def showMovieDetail(mov):
    print(f"Name : {mov['name']}")
    print(f"Director : {mov['director']}")
    print(f"Year : {mov['year']}")
    

#function to find movies 
def findMovies():
    find_by=input("Enter the attribute to search by  :")
    value=input("Enter the value of the attributes  :")
    mov_list=find_by_attributes(movies,value,lambda x: x[find_by])
    show_movies(mov_list)

#print the attribute of the movies present in the list
def show_movies(movie_list):
    print("----------printing the search result----------\n")
    for mov in movie_list:
        showMovieDetail(mov)
        print("-----------------------")
#function which searches the movie and appends it to the list
def find_by_attributes(items,expected,finder):
    found=[]
    for i in items:
        if finder(i)== expected:
            found.append(i)
    return found


menu()