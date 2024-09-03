# Luca Cavalleri
# 18/04/2024

#2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. 
#Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

name: str="Dario"
print(f"ES.2.3\nCiao {name} ti va di imparare un po di python oggi?")


#2-4. Name Cases: Use a variable to represent a person’s name, 
#and then print that person’s name in lowercase, uppercase, and title case.

nameb: str="pippo"
print("\nES.2.4\nStampo il nome scritto minuscolo:",nameb.lower(),
      "\nmaiuscolo:",nameb.upper(),
      "\niniziale maiuscola:", nameb[0].upper()+nameb[1:len(nameb)])


#2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. 
#Your output should look something like the following, including the quotation marks: Albert Einstein once said, 
#“A person who never made a mistake never tried anything new.”

print('\nEs 2.5\nJ. Robert Oppenheimer once said:\n"Now I\'ve become death, the destroyer of worlds."')


#2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person.
# Then compose your message and represent it with a new variable called message. Print your message. 

famous_person="J. Robert Oppenheimer"
message=f'\nES.2.6\n{famous_person} once said:\n"Now I\'ve become death, the destroyer of worlds."'
print(message)


'''2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). 
Assign the value 'python_notes.txt' to a variable called filename. 
Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.'''

filename="python_notes.txt"
print("\nES.2.8\n",filename.removesuffix(".txt"))


'''3-1. Names: Store the names of a few of your friends in a list called names. 
Print each person’s name by accessing each element in the list, one at a time.'''

print("\nES.3.1\n")
friends=["Alessia","Samuel","Tiziano","Gianluca","Claudia"]
for i in friends:
    print(i)


'''3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, 
print a message to them. The text of each message should be the same, 
but each message should be personalized with the person’s name.'''

print("\nES.3.2\n")
for i in friends:
    print("Te se ama ",i," <3")


'''3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, 
and make a list that stores several examples. Use your list to print a series of statements about these items, 
such as “I would like to own a Honda motorcycle.”'''

print("\nES.3.3\n")
type=["Citroen","Ferrari","BMW"]

for i in type:
    print("I love driving around in the city, with my",i,".")
    print("I'd love to buy a ",i,"some day.")
    print("I dont care about the engine i simply love ",i," cars.")
    

'''3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? 
Make a list that includes at least three people you’d like to invite to dinner. 
Then use your list to print a message to each person, inviting them to dinner.'''

print("\nES.3.4\n")
dinner=["Albert Einstein","Marilyn Monroe","Hitodeka Miyazaky"]
for i in dinner:
    print("Dear ",i,"\nyou are invited to dinner.")


'''3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, 
 you need to send out a new set of invitations. You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program, 
    stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.'''

print("\nES.3.5\nAlbert Einstein can't come to dinner.")
dinner.remove("Albert Einstein")
dinner.append("Leclerc")
for i in dinner:
    print("Dear ",i,"\nyou are invited to dinner.")


'''3-6. More Guests: You just found a bigger dinner table, so now more space is available. 
Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. 
    Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.'''

print("\nES.3.6\nYOOOO bigger table found")
dinner.insert(0,"Pippo")
dinner.insert(len(dinner)//2,"Lillo")
dinner.append("Gino")
for i in friends:
    print("Dear ",i,"\nyou are invited to dinner.")


'''3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner,
 and now you have space for only two guests.
• Start with your program from Exercise 3-6. 
    Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. 
    Each time you pop a name from your list, 
    print a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. 
    Print your list to make sure you actually have an empty list at the end of your program.'''

print("\nES.3.7\nOnly 2 people for dinner now.")
while len(dinner)>2:
    print("I'm sorry",dinner.pop(),"I have no space and you can't come.")
print("You are still invited",dinner[0])
print("You are still invited",dinner[1])
del(dinner[0])
del(dinner[0])
print(dinner)


'''3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order.
Print the list to show that its order has changed.'''

print("\nES.3.8")
locations=["Roma","Parigi","New York","Tokyo","London"]
print(locations)
print(sorted(locations))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations=sorted(locations)
print(locations)
locations=sorted(locations, reverse=True)
print(locations)



'''3-9. Dinner Guests: Working with one of the programs from Exercises 3, 
use len() to print a message indicating the number of people you’re inviting to dinner.'''

print("\nEs.3.9")
dinner=["Albert Einstein","Marilyn Monroe","Hitodeka Miyazaky"]
print("Sto invitando ",len(dinner)," persone.")


'''3-10. Every Function: Think of things you could store in a list. 
For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.'''

print("\nES.3.10")
games=["Outer Wilds","Undertale","Metal Gear Saga","God of War"]
games.append("Elden Ring")
games=sorted(games)
games.reverse
print(games)
for i in range(len(games)):
    print(games[i])
    games[i]=games[i].upper()
    if i%2==0:
        games.pop(i)
        games.insert(i,"League of Legends")
    else:
        games[i]=games[i].lower()
games.remove("outer wilds")
print(games)



'''6-1. Person: Use a dictionary to store information about a person you know. 
Store their first name, last name, age, and the city in which they live. 
You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.'''

print("\nES.6.1")
me={"first_name":"Luca","last_name":"Cavalleri","age":21,"city":"Santa Marinella"}
for i in me.values():
    print(i)


'''6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. 
Think of five names, and use them as keys in your dictionary. 
Think of a favorite number for each person, and store each as a value in your dictionary. 
Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.'''

print("\nES.6.2")
fave_nums={"Pino":3,"Franco":10,"Tiziano":13,"Luca":23}
for i,j in fave_nums.items():
    print("Il numero preferito di ",i," è ",j)


'''6-3. Glossary: A Python dictionary can be used to model an actual dictionary. 
However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous chapters. 
    Use these words as the keys in your glossary, and store their meanings as values.
• Print each word and its meaning as neatly formatted output. 
    You might print the word followed by a colon and then its meaning, 
    or print the word on one line and then print its meaning indented on a second line. 
    Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.'''

print("\nES.6.3")
Glossary={"iteratori":"Strumenti logici in programmazione che iteran (ciclano) il codice al loro interno per x volte decise da un range o una condizione.",
          "variabile":"Un contenitore, utilizzato nella rogrammazione in modo da salvare dati e potervi accedere in seguito, ce ne sono vari tipi in base a cosa si vuole salvare.",
          "liste":"un tipo di variabile all'interno della quale possono veir salvate piu varibili, e venr chiamate singolarmente in base al loro indice nella lista."}
for i,j in fave_nums.items():
    print(i,":\n\t",j)


'''6-7. People: Start with the program you wrote for Exercise 6-1. 
Make two new dictionaries representing different people, and store all three dictionaries in a list called people. 
Loop through your list of people. As you loop through the list, print everything you know about each person.'''

print("\nES.6.7")
Pino={"first_name":"Pino","last_name":"Rossi","age":45,"city":"Roma"}
Gino={"first_name":"Gino","last_name":"Verdi","age":65,"city":"Milano"}
people=[me,Pino,Gino]
for i in people:
    print("Nome: ",i["first_name"],"\nCognome",i["last_name"],"\nEtà",i["age"],"\nCittà:",i["city"],"\n")

'''6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. 
In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. 
Next, loop through your list and as you do, print everything you know about each pet. '''

print("\nES.6.8")
pet1={"animal_name":"Leone","animal_type":"Dog","owner":"Claudia"}
pet2={"animal_name":"Kuro","animal_type":"Cat","owner":"Leonardo"}
pet3={"animal_name":"Pyx","animal_type":"Parrot","owner":"Harold"}
pets=[pet1,pet2,pet3]
for i in pets:
    print("Nome: ",i["animal_name"],"\nAnimale:",i["animal_type"],"\nNome padrone:",i["owner"],"\n")


'''6-9. Favorite Places: Make a dictionary called favorite_places. 
Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. 
To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. 
Loop through the dictionary, and print each person’s name and their favorite places.'''

print("\nES.6.9")
favorite_places={"Mario":["stadio","faro","piscina"],"Luigi":["cascatelle","parco","pyrgo"],"Tino":["acquedotto","bar","università"]}
for i,j in favorite_places.items():
    print("\nI posti preferiti di",i,"sono:")
    print(*j,sep=", ")


'''6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. 
Then print each person’s name along with their favorite numbers.'''

print("\nES.6.10")
fave_nums["Franco"]=[3,44,99]
fave_nums["Luca"]=[23,7,13]
fave_nums["Pino"]=[10,77,17]
fave_nums["Tiziano"]=[13,5,90]
for i,j in fave_nums.items():
    print("\nI numeri preferiti di",i,"sono:")
    print(*j,sep=", ")


'''6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
Create a dictionary of information about each city and include the country that the city is in, its approximate population, 
and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. 
Print the name of each city and all of the information you have stored about it.'''


cities={"Roma":{"country":"Italy","population":"4,332,000","fun_fact":"There are more than 2000 fountains in Rome."},
        "New York":{"country":"USA","population":"7,931,147","fun_fact":"Times square has 238 billboards."},
        "Tokyo":{"country":"Japan","population":"37,115,035","fun_fact":"There are anti-suicide lights in Tokyo’s metro stations."}}
for i,j in cities.items():
    print("\nThe informations about",i,"are:")
    print("\ncountry:",j["country"],"\npopulation number:",j["population"],"\nfun fact:",j["fun_fact"],)

'''6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. 
Use one of the example programs from this chapter, and extend it by adding new keys and values, 
changing the context of the program, or improving the formatting of the output.'''

cities["Roma"]["surface_area"]="1.285 km^2"
cities["New York"]["surface_area"]="783,8 km^2"
cities["Tokyo"]["surface_area"]="2.194 km^2"
for i,j in cities.items():
    print("\nThe informations about",i,"are:")
    print("\ncountry:",j["country"],"\npopulation number:",j["population"],"\nfun fact:",j["fun_fact"],"\nsurface area:",j["surface_area"])
