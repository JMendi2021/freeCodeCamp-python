print("-----------------------------------\nLists\n-----------------------------------")
#Lists
"""
Lists is a collection of related values (Can be any data type) surrounded by Square Brackets. For example
"""
print("")
exampleList = [5, 4, True, 2.01, 1, "This is a string!"] #This is how you create an List! An array would use {}
print("Print the content of a List!")
print("This is inside exampleList: ", exampleList)

print("\nUsing a For Loop to iterate through each element!")
for i in exampleList: #We can use a FOR LOOP to iterate through each elements.
    print(i)

print("\nThe size of exampleList (using len()) is: ", len(exampleList)) #Returns the size of a List

"""
You can access elements in a list using its index. Modifying them is also possible
"""
print("\nAccessing elements in a List (Index 5")
print(exampleList)
print("\nIndex 5 stores: " + exampleList[5]) #Accesing an element

"""
Lists are Mutable, meaning that we can change an element on a list. Strings are example of immutable where you can't change a character in it. You require to make a whole new string
"""
exampleList[5] = "Now it's this string!" #Modifying an element
print("Modifying Index 5\nIndex 5 stores: ", exampleList[5])

"""
The range() function creates an list from 0 to n-1 (Incremental) which we used for FOR LOOPS
"""
exampleList2 = [x for x in range(4)] #This is list comprehension
print("Ways to use FOR Loops\nExample 1:")
for number in exampleList2:
    print(number)
print("Example 2:")
for i in range(len(exampleList2)): #This is an Index Loop where range() returns a list of numbers from 0 to n-1
    print(exampleList2[i])

"""
You can use the concatenating operator (+) to append a list to another list! Much like for strings
"""
a = [1,2,3]
b = [4,5,6]
c = a + b
print("Concatenating Lists a and b: ", c)

"""
You can also get a specific section of a List using listName[Index1:Index2]
"""
print("First 2 elements of List C: ",c[:2]) #We want all numbers up to, and not including, index 2
print("Get the 2 elements starting from index 3 of List C: ", c[2:4]) #Include elements from Index 2 and to, but not including, Index 4
print("Last elements of List C from index 4: ", c[4:])

"""
Other List Methods: https://docs.python.org/3/tutorial/datastructures.html
"""

exampleList3 = list() #This is how we create an empty list
exampleList3.append(3)
exampleList3.append("Hello")
exampleList3.append(True)
print("\nDeclaring an empty list and adding to it: ", exampleList3)

"""
There are many useful methods for Lists, which we can help with a lot of things. These methods takes in a List of purely just numbers:
    min - gets the smallest
    max - gets the biggest
    sum - gets the sum of all the numbers in the list
"""

"""
Let's say that we want to go through a string. We can use the split() method to break the string into pieces and produce a list of strings.
"""
stringExample = "This is a test!"
stringList = stringExample.split() #This splits each word whereever there is a space (Which is the default delimiter)
print("\nString: ", stringExample, "\nSplitting a String and printing it:", stringList) #Now we can iterate through each element
"""
The delimiter tells the program how we want to split the word. It means that anything after a delimiter character is what we want to store in the List.
Say that the delimiter is ';' then the follow string ('1;2     ;3;;;4') will be split to: [1, 2     , 3, 4]7
    If there is no character after a delimiter then it is not included
"""
print("\n\n")
print("-----------------------------------\nDictionaries\n-----------------------------------")
#Dictionaries
"""
Dictionaries is a data type where we store values in a sort of 'key-value- pair -> They're like HashMaps in Java
    Instead of accesing and modifying values through their index, we do it using their assigned Keys
    Uses curly brackets, commas and colons.
    
"""

exampleDict = dict() #Creating an empty dictionary
exampleDict2 = {
    1:"Monday",
    2:"Tuesday",
    3:"Wednesday",
    4:"Tursday", #Intentional spelling mistake
    5:"Friday",
    6:"Saturday",
    7:"Sunday"
}
print("Printing entire dictionary 1: ", exampleDict)
print("Printing entire dictionary 2: ", exampleDict2)
print("\nAccessing values through key:")
print(exampleDict2[4]) #Should print out 'Tursday'
exampleDict2[4] = "Thursday" #Fixing spelling mistake
print(exampleDict2[4])

print("\nAdding new key:value to dictionaries:")
print(exampleDict)
exampleDict["Test"] = "Hello world!" #We add the Key "Test" with value "Hello World"
print(exampleDict)

"""
Histograms are common uses of dictionaries where we store the labels as keys and how many times they occur in their respective values
"""
print("\nUsing dictionaries for counting")
counts = dict()
letters = ['a','b','a','d','d']
for name in letters:
    counts[name] = counts.get(name, 0) + 1 #get() method takes two parameters and returns the value of corresponding key or it returns the second parameter if it does not exist
print(counts)

"""
An error occur if we attempt to access a key that is not in the dictionary (It doesn't exist.).
    We use the 'in' operator to check if the key is in the dictionary before we use any other codes
"""
print("\nAccessing non existent keys")
try:
    print(exampleDict2[8])
except:
    print("ERROR") #Key 8 doesn't exist!

if 8 in exampleList2: #'in' checks if 8 exists in exampleList2 so we don't necessary need to use a try-except
    print(exampleDict2[8])
else:
     print("KEY DOES NOT EXISTS")

"""
Like Lists, we can use Definite Loops with Dictionaries.
"""
print("\n\nPrint the dictionary using FOR Loops")
for day in exampleDict2: #It will only take out the keys
    print(day, exampleDict2[day])

"""
You are able to get a list of keys, values or both!
"""
print("\n\nPrinting the Keys of a Dictionary as a list")
print(list(exampleDict2)) #Prints out the keys of a Dictionary
print(exampleDict2.keys()) #Prints out the keys of a Dictionary

print("\nPrinting values of a Dictionary as a list")
print(exampleDict2.values()) #Prints out the values of a Dictionary

print("\nPrinting keys and values of a dictionary as a list")
print(exampleDict2.items()) #Prints out the keys and values of a Dictionary

"""
Instead of relying on a single variable for a FOR loop, we can use two of them. One for the key and the other for the value using the list generated from item()!
"""
print("\n\nPrinting dictionary using item()")
for number, day in exampleDict2.items():
    print(number, day)
