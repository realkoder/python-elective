
def getChars():
   return [chr(char) for char in range(ord('A'), ord('Z') + 1) if char not in range(ord('F'), ord('O') + 1, 2)]

#print(getChars())

colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']
exclude = [('Black', 'm'), ('White', 's')]

def getBlackWhiteList():
   return [(color, size) for color in colors for size in sizes if (color, size) not in exclude]

#print(getBlackWhiteList())

def evenNumList():
   return [num for num in range(0, 21, 2)]

def squarredNums():
   return [num**2 for num in range(1, 11)]

#print(squarredNums())

def getVowelsForString(string):
   vowels = "aeiouæøåAEIOUÆØÅ"
   return [char for char in string if char in vowels]

#print(getVowelsForString("HEJ MED DIG MAN - HVA SÅ dær"))

# Create a list of common elements in two given lists. (could this be done with the use of another datastructure?)



# Create a list of words from a given string that have more than 4 and less than 8 letters
def listOfWordsWithGivenLength(string):
   return [word for word in string.split() if len(word) > 4 and len(word) < 8]

#print(listOfWordsWithGivenLength("Dette er en tester af metoden"))

# Create a function that takes a string as a parameter and returns a list.
# The function should remove all vowels and sort the consonants in alphabetic order, and the return the result.
def stringToList(string):
   vowels = "aeiouæøåAEIOUÆØÅ "
   return sorted([char for char in string if char not in vowels])

#print(stringToList("hej med dig"))

# Create a list of strings with names in it. (l = [‘Claus’, ‘Ib’, ‘Per’])
# Sort this list by using the sorted() build in function.
l = ["Claus", "Ib", "a", "bo", "Per"]
print(sorted(l))
# Sort the list in reversed order.
print(sorted(l, reverse=True))

# Sort the list on the lenght of the name.
print(sorted(l, key=len))

# Sort the list based on the last letter in the name.
print(sorted(l, key=lambda str: str[-1]))

# Sort the list in a way that the names that has an ‘a’ in it should be sorted first (still alphabetically).
print(sorted(l, key=lambda str: (0, str) if 'a' in str else (1, str)))




s = 'This is just a sample text that could have been a million times longer.\n\nYours Johnny'
# Count the number of characters including blank spaces.
print(len(s))

# Count the number of characters excluding blank spaces.
print("Len without blank spaces: " + str(len([char for char in s if char >='A' and char <= 'z'])))

# Count the number of words
print(len(s.split()))