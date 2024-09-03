#Luca Cavalleri
'''
8-1. Message: Write a function called display_message() that prints one sentence telling everyone 
what you are learning about in this chapter. Call the function, and make sure the message displays correctly.
'''

def display_message():
    print("In this chapter, I'm learning about funcions.")

print("\nES.8.1")
display_message()


'''
8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. 
The function should print a message, such as "One of my favorite books is Alice in Wonderland". 
Call the function, making sure to include a book title as an argument in the function call.
'''

def favorite_book(title:str):
    print("One of my favorite books is",title)

print("\nES.8.2")
favorite_book("Cthulhu, I racconti del mito")


'''
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message 
that should be printed on the shirt. The function should print a sentence summarizing the size of 
the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. 
Call the function a second time using keyword arguments.
'''

def make_shirt(size,text):
    print("We'll make a shirt size:",size,"with the text '",text,"' printed on it.")

print("\nES.8.3")
make_shirt("L","Positional arguments call.")
make_shirt(text="Keyword arguments call.",size="M")

'''
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
'''

def make_shirt(text,size="L"):
    print("We'll make a shirt size:",size,"with the text '",text,"' printed on it.")

print("\nES.8.4")
make_shirt("I love Python")
make_shirt("I love Python","M")
make_shirt("Keep calm and code","S")


'''
8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. 
The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. 
Call your function for three different cities, at least one of which is not in the default country.
'''

def describe_city(city,country="Italy"):
    print(city,"is in",country)

print("\nES.8.5")
describe_city("Rome")
describe_city("Milan")
describe_city("New York","USA")


'''
8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. 
The function should return a string formatted like this: "Santiago, Chile". 
Call your function with at least three city-country pairs, and print the values that are returned.
'''

def city_country(city,country):
    return(city,",",country)

print("\nES.8.6")
print(city_country("Tokyo","Japan"))
print(city_country("Milan","Italy"))
print(city_country("Los Angeles","USA"))


'''
8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. 
The function should take in an artist name and an album title, and it should return a dictionary containing these 
two pieces of information. Use the function to make three dictionaries representing different albums. 
Print each return value to show that the  dictionaries are storing the album information correctly. 
Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 
Make at least one new function call that includes the number of songs on an album.
'''

def make_album(artist,album,songs=None):
    if songs==None:
        dictionary={"Artist":artist,"album":album}
    else:
        dictionary={"Artist":artist,"album":album,"songs":songs}
    return dictionary

print("\nES.8.7")
print(make_album("Eve","Smile"))
print(make_album("Wilbur Soot","Your city gave me asthma"))
print(make_album("The Living Tombstone","My ordinary life",1))


'''
8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist 
and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
Be sure to include a quit value in the while loop.
'''

print("\nES.8.8")
loop=True
while loop:
    ans=input("Do you wanna make an album? Y/N")
    if ans.upper()=="Y":
        print("Here is the album you created:",make_album(input("Enter the name of the artist: "),input("Enter the name of the album: ")))
    elif ans.upper()=="N":
        loop=False
    else:
        print("Please enter Y or N as an answer")


'''
8-9. Messages: Make a list containing a series of short text messages. 
Pass the list to a function called show_messages(), which prints each text message.
'''

print("\nES.8.9")
texts=["Hello, how are you?","I'm so happy.","I hate this.","Do you know what i'm thinking about?"]
def show_messages(messages: list):
    for i in messages:
        print(i)

show_messages(texts)


'''
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
Write a function called send_messages() that prints each text message and moves each message 
to a new list called sent_messages as it’s printed. 
After calling the function, print both of your lists to make sure the messages were moved correctly.
'''

print("\nES.8.10")
texts=["Hello, how are you?","I'm so happy.","I hate this.","Do you know what i'm thinking about?"]
def send_messages(messages: list):
    sent_messages=[]
    for i in messages:
        print(i)
        sent_messages.append(i)
    
    return sent_messages

sent=send_messages(texts)
print(texts,sent)


'''
8-11. Archived Messages: Start with your work from Exercise 8-10. 
Call the function send_messages() with a copy of the list of messages. 
After calling the function, print both of your lists to show that the original list has retained its messages.
'''

print("\nES.8.11")
copy=texts.copy()
send_messages(copy)
print(texts)
print(copy)


'''
8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
The function should have one parameter that collects as many items as the function call provides, 
and it should print a summary of the sandwich that’s being ordered. 
Call the function three times, using a different number of arguments each time.
'''

print("\nES.8.12")
def make_sandwich(*ingredients):
    print("The sandwitch will have:")
    for i in ingredients:
        print(i)
    print()

make_sandwich("bread","ham")
make_sandwich("bread","ham","cheese","mayonase")
make_sandwich("bread","ham","mayonase")


'''
8-13. User Profile:  Build a profile of yourself by calling build_profile(), 
using your first and last names and three other key-value pairs that describe you. 
All the values must be passed to the function as parameters. 
The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"
'''

print("\nES.8.13")
def build_profile(firstN,lastN,age,height,weight):
    print(firstN,lastN,", age",age,", height",height,", weight",weight)

build_profile("Luca","Cavalleri","21","1,78","84")


'''
8-14. Cars: Write a function that stores information about a car in a dictionary. 
The function should always receive a manufacturer and a model name. 
It should then accept an arbitrary number of keyword arguments. 
Call the function with the required information and two other name-value pairs, such as a color or an optional feature. 
Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) 
Print the dictionary that’s returned to make sure all the information was stored correctly. 
'''

print("\nES.8.14")
def make_car(manufacturer, model, color, plate):
    return {"manufacturer":manufacturer,"model":model,"color":color,"plate":plate}

car = make_car('subaru', 'outback', color='blue', plate="SS354XX")
print(car)


'''
8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. 
Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
'''

print("\nES.8.15")
import printing_models


'''
8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. 
Import the function into your main program file, and call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
'''

print("\nES.8.16")
import lez4_4
from lez4_4 import convert_to_title
from lez4_4 import convert_to_title as conv
import lez4_4 as l4_4
from lez4_4 import *


'''
8-17. Styling Functions: Choose any three programs you wrote for this chapter, and make sure they 
follow the styling guidelines described in this section.
'''

print("\nES.8.17")

def make_car(
        manufacturer, model, color, 
        plate):
    return {
        "manufacturer":manufacturer,
        "model":model,
        "color":color,
        "plate":plate
        }


def build_profile(
        firstN, lastN, age, height,
        weight):
    print(firstN, lastN, ", age", age, 
          ", height", height, ", weight" ,weight)


def make_sandwich(*ingredients):
    print("The sandwitch will have:")
    
    for i in ingredients:
        print(i)
    print()
