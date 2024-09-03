'''
  Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
    than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
'''
s="Lol"
numl=[23,3,4,5,6,90]
number=23

#STRING TESTS
#EQUALITY INEQUALITY
print("\nIs s == 'Lol'? I predict True.")
print(s == 'Lol')

print("\nIs s == 'LOL'? I predict False.")
print(s == 'LOL')

#LOWER() TESTS
print("\nIs s.lower() == 'lol'? I predict True.")
print(s.lower() == 'lol')

print("\nIs s.lower() == 'LOL'? I predict False.")
print(s.lower() == 'LOL')


#NUMERICAL TESTS
#EQUALITY AND INEQUALITY
print("\nIs number == 23? I predict True.")
print(number == 23)

print("\nIs number == 13? I predict False.")
print(number == 13)

print("\nIs number != 23? I predict False.")
print(number != 23)

print("\nIs number != 22? I predict True.")
print(number != 22)

#LESSER THAN AND LESSER THAN OR EQUAL TO
print("\nIs number < 28? I predict True.")
print(number < 28)

print("\nIs number < 8? I predict False.")
print(number < 8)

print("\nIs number <= 23? I predict True.")
print(number <= 23)

print("\nIs number <= 8? I predict False.")
print(number <= 8)

#GRETATER THAN AND GREATER THAN OR EQUAL TO

print("\nIs number > 8? I predict True.")
print(number > 8)

print("\nIs number > 28? I predict False.")
print(number > 28)

print("\nIs number >= 23? I predict True.")
print(number >= 23)

print("\nIs number >= 28? I predict False.")
print(number >= 28)

#USING KEYWORD 'AND' AND KEYWORD 'OR'
print("\nIs number==23 and number>? I predict True.")
print(number==23 and number>2)

print("\nIs number==20 and number>2? I predict False.")
print(number==20 and number>2)

print("\nIs number==23 or number<2? I predict True.")
print(number==23 or number<2)

print("\nIs number==20 or number>0? I predict False.")
print(number==20 or number>90)


#ELEMENT IN AND NOT IN A LIST
print("\nIs number in numl? I predict True.")
print(number in numl)

print("\nIs 20 in num? I predict False.")
print(20 in numl)

print("\nIs number not in numl? I predict False.")
print(number not in numl)

print("\nIs 20 in numl? I predict True.")
print(20 not in numl)
