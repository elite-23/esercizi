'''
1. Create a Playlist:

Write a function called create_playlist() that accepts a playlist name and a variable number of song titles. 
The function should return a dictionary with the playlist name and a set of songs. 
Call the function with different numbers of songs to demonstrate flexibility.
Example: create_playlist("Road Trip", {"Song 1", "Song 2"})

Write a function called add_like() that accepts a dictionary, the name of a playlist, 
and a boolean value indicating whether it is liked (True or False). 
This function should return an updated dictionary.
Example: add_like(dictionary, “Road Trip”, liked=True)
'''

def create_playlist(name:str, *song_title:str):
    playlist={"name":name,"songs":[]}
    for i in song_title:
        playlist["songs"].append(i)
    playlist["songs"]=set(playlist["songs"])
    return playlist

print("\nES.1.1")
print(create_playlist("Free time","Dramaturgy","Avant","Kaikai Kitan"))


def add_like(likes:dict, name:str, like:bool):
    likes[name]=like
    return likes

print("\nES.1.2")
print(add_like({"This is Eve":True, "Sad songs":False}, "Free time", True))


'''
2. Book Collection:

Write a function called add_book() that accepts an author's name and a variable number of book titles authored by them. 
This function should return a dictionary where the author's name is the key and the value is a list of their books. 
Demonstrate this function by adding books for different authors.
Example: add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"])

Write a function called delete_book() that accepts a dictionary and the name of the author from whom to remove all details. 
This function should return an updated dictionary.
Example: delete_book(dictionary, “Mark Twain”)
'''

def add_book(author:str, *books:str):
    bibliography={author:books}
    return bibliography

print("\nES.2.1")

bibliography={}
bibliography.update(add_book("J. K. Rowling","Harry Potter e la pietra filosofale","Harry Potter e la camera dei segreti,",
                             "Harry Potter e il prigioniero di Azkaban,","Harry Potter e il calice di fuoco,",
                             "Harry Potter e l'Ordine della Fenice", "Harry Potter e il principe mezzosangue",
                             "Harry Potter e i doni della morte"))
print(bibliography)

bibliography.update(add_book("H.P. Lovecraft","Il richiamo di chthulhu","Alle montagne della follia").items())
print(bibliography)


def delete_book(bibliografy:dict, name:str):
    bibliografy.pop(name)
    return bibliografy

print("\nES.2.2")
print (delete_book(bibliography, "J. K. Rowling"))


'''
3. Personal Info:

Write a build_profile() function that accepts the name , surname,  occupation, location, and age  of a person. 
Make occupation, location, and age optional parameters. Use this function to create profiles for different people, 
demonstrating how it handles these optional parameters.
Example: build_profile("John", "Doe", occupation="Developer", location="USA", age=30)
'''

def build_profile(name:str, surname:str, 
                 occupation:str = None, location:str =None, age:int = None):
    profile={"name":name,"surname":surname}
    
    if occupation!=None:
        profile["occupation"]=occupation
    if location!=None:
        profile["location"]=location
    if age!=None:
        profile["age"]=age
    
    return profile

print("\nES.3")
print(build_profile("John", "Doe", occupation="Developer", location="USA", age=30))
print(build_profile("Jinwo", "Sung", occupation="Hunter", location="South Korea"))
print(build_profile("Mario", "Rossi", occupation="Baker"))



'''
4. Event Organizer:

Write a function called plan_event() that accepts an event name, a list of participants, and an hour. 
The function should return a dictionary that includes the event name and a list of the participants. 
Call this function with varying numbers of participants to plan different events.
Example: plan_event("Code Workshop", ["Alice", "Bob", "Charlie"],”4pm”)

Write a function called modify_event() that accepts a dictionary, an event name, and new details to modify an already planned event.
Example: modify_event(dictionary, "Code Workshop", ["Alice", "Bob", "Charlie"], ”4pm”)
'''


def plan_event(name:str, participants:list, hour:str):
    return {name:participants}

print("\nES.4.1")
events={}
events.update(plan_event("Brunch",["Pippo","Pluto","Paperino"],"12am"))
print(events)
events.update(plan_event("The -inos",["Gino","Tino","Pino","Fino"],"7pm"))
print(events)
events.update(plan_event("Alone time",["Me"],"2am"))
print(events)


def modify_event(old_events:dict ,name:str, participants:list, hour:str):
    return(old_events.update({name:participants}))

print("\nES.4.2")
modify_event(events, "Brunch",["Pippo","Topolino"],"12am")
print(events)

modify_event(events, "The -inos",["Gino","Tino","Pino","Fino","Lino"],"7pm")
print(events)

modify_event(events, "Alone time",["Me","Myself"],"2am")
print(events) 



'''
5. Shopping List:

Write a function called create_shopping_list() that accepts a store name and any number of items as arguments. 
It should return a dictionary with the store name and a set of items to buy there. 
Test the function with different stores and item lists.
Example: create_shopping_list("Grocery Store", {"Milk", "Eggs", "Bread"})

Write a function called print_shopping_list() that accepts a dictionary and a store name, 
then prints each item from that store's shopping list.
Example: print_shopping_list(dictionary, "Grocery Store")
'''

print("\nES.5.1")
def create_shopping_list(store_name :str, *item :str):
    items_set=[]
    for i in item:
        items_set.append(i)
    return {"name":store_name,"items":set(items_set)}

print(create_shopping_list("Grocery Store", "Milk", "Eggs", "Bread"))
print(create_shopping_list("Conad", "Cookies", "Sausage", "Meat","Ice Cream"))
print(create_shopping_list("Super Elite", "Milk", "Eggs", "Bread","Pizza","Mozzarella"))

print("\nES.5.2")
def print_shopping_list(shopping_list :dict, store_name :str):
    print("The shopping list of the",store_name,"is:")
    for i in shopping_list.values():
        print(i)
    print()

print_shopping_list({1:"Milk",2:"Bread"},"Grocery store")
print_shopping_list({1:"Milk",2:"Bread",3:"Pizza"},"Super Elite")
print_shopping_list({1:"Milk",2:"Bread",3:"Cookies",4:"Ice cream"},"Conad")